from datetime import timedelta
from robot.api.deco import keyword
from libraries.pos.POSRestaurantLibrary.dto.orderdetails import DisplayedOrders, OrderDetails
from libraries.pos.POSRestaurantLibrary.locators.frame import POS_RESTAURANT_FRAME
from libraries.pos.POSRestaurantLibrary.locators import restaurantlanding, moreorderlist, morelanding
from autocore.bases import WebLibraryComponent
from autocore.coreutils import format_phone_number
from autocore.web.webactions import sleep


class OrderListKeywords(WebLibraryComponent):

    @keyword(tags=("RestaurantKeywords", "OrderListKeywords"))
    def view_details_of_order(self, oid: str = None, phone_number: str = None, header: str = None, _: OrderDetails = None) -> OrderDetails:
        """Select an order from the order list (More display > Order list) and return the details as an object of `OrderDetails`.

        - ``oid``: priority to use in locating the order
        - ``phone_number`` and ``header``: if ``oid`` was not provided, these will be used to locate the order.
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.__open_more_display()
            self.__wait_until_orders_are_displayed()
            successfully_selected = False
            try_count = 5

            while not successfully_selected:
                if try_count == 0:
                    break

                if oid is not None:
                    self.logger.info(f"SELECTING ORDER BY ID: {oid}")
                    if phone_number is None:
                        text = self.web.get_text(
                            locator=moreorderlist.ORDER_DESC_USING_ID(oid))
                        _, _, act_phone = self.__parser_order_btn_text(text)
                        phone_number = format_phone_number(act_phone)

                    self.__select_order_with_id(el_id=oid)

                    if self.__is_opened_order_correct(phone_number=phone_number):
                        successfully_selected = True
                    self.logger.info(
                        f"DONE SELECTING ORDER BY ID: {oid}. Is successful: {successfully_selected}")
                else:
                    order_count = self.web.count(
                        locator=moreorderlist.ORDERS)
                    for i in range(1, order_count + 1):

                        oid = self.web.get_attribute(
                            locator=moreorderlist.ORDERS_DIV(i), attribute='id')
                        text = self.web.get_text(
                            locator=moreorderlist.ORDER_DESC(i))
                        self.logger.debug(f"OID: {oid}")
                        self.logger.debug(f"Order button text: {text}")

                        act_header, time, act_phone = self.__parser_order_btn_text(
                            text)
                        act_phone = format_phone_number(act_phone)
                        # use phone number and header to select
                        if phone_number is not None and header is not None:
                            phone_number = format_phone_number(phone_number)
                            if phone_number == act_phone and header == act_header:
                                self.__select_order_with_id(el_id=oid)
                                if self.__is_opened_order_correct(phone_number=phone_number):
                                    successfully_selected = True
                                break
                        # user phone number only to select
                        elif phone_number is not None and header is None:
                            phone_number = format_phone_number(phone_number)
                            if phone_number == act_phone:
                                self.__select_order_with_id(el_id=oid)
                                if self.__is_opened_order_correct(phone_number=phone_number):
                                    successfully_selected = True
                                break

                        # use header only to select
                        elif phone_number is None and header is not None:
                            if header == act_header:
                                phone_number = act_phone
                                self.__select_order_with_id(el_id=oid)
                                if self.__is_opened_order_correct(phone_number=phone_number):
                                    successfully_selected = True
                                break

                try_count -= 1

                if not successfully_selected:
                    sleep(seconds=2)

            if not successfully_selected:
                raise Exception("No order was selected.")

            details = self.__get_details(
                order_id=oid, phone_number=phone_number)

        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

        self.logger.debug(details)
        return details

    @keyword(tags=("RestaurantKeywords", "OrderListKeywords"))
    def get_displayed_orders(self, _: DisplayedOrders = None) -> DisplayedOrders:
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.__open_more_display()
            self.__wait_until_orders_are_displayed()
            orders_count = self.web.count(
                locator=moreorderlist.SENT_ORDERS)
            sent_orders = [self.web.get_attribute(locator=moreorderlist.SENT_ORDERS_DIV(i), attribute="id")
                           for i in range(1, orders_count + 1)]
            saved_orders_count = self.web.count(
                locator=moreorderlist.SAVED_ORDERS)
            saved_orders = [self.web.get_attribute(locator=moreorderlist.SAVED_ORDERS_DIV(i), attribute="id") for i
                            in range(1, saved_orders_count + 1)]
            canceled_orders_count = self.web.count(
                locator=moreorderlist.CANCELLED_ORDERS)
            canceled_orders = [
                self.web.get_attribute(locator=moreorderlist.CANCELLED_ORDERS_DIV(i), attribute="id") for i in
                range(1, canceled_orders_count + 1)]
            details = DisplayedOrders(sent_orders=sent_orders, cancelled_orders=canceled_orders, saved_orders=saved_orders)
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
        self.logger.debug(details)
        return details

    def is_sent_order(self, oid: str) -> bool:
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            locator = f"id:{oid}"
            is_sent_order = self.web.attribute_contains(locator=locator, attribute="class", exp_value="status_new")
            self.logger.info(f"ID button class: {self.web.get_attribute(locator=locator, attribute='class')}")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
        return is_sent_order

    def __is_opened_order_correct(self, phone_number: str):
        self.web.wait_until_visible(locator=morelanding.PHONE)
        self.web.wait_until_text_is_not_empty(
            locator=morelanding.PHONE)
        result = phone_number.strip().replace(" ", "") in self.web.get_text(
            locator=morelanding.PHONE).strip().replace(" ", "")
        self.logger.info(f"Is the correct order open? {result}")
        return result

    def __open_more_display(self):
        if not self.web.attribute_ends_with(locator=restaurantlanding.MORE_BTN, attribute="class",
                                             exp_value="selected"):
            self.web.click(locator=restaurantlanding.MORE_BTN)
            sleep(seconds=1)
            self.web.wait_until_not_visible(
                moreorderlist.ORDER_LIST_LOADER_IMG)

    def __wait_until_orders_are_displayed(self):
        self.web.wait_until_visible(locator=moreorderlist.ORDER_AREA)

        display_count = 2
        max_retry = 30

        while display_count > 0:
            self.logger.info(
                f"Wait until order are displayed. Remaining retry: {max_retry}. Display count: {display_count}")
            if max_retry == 0:
                break
            if self.web.is_visible(locator=moreorderlist.ORDER_LIST_LOADER_IMG, timeout=timedelta(seconds=0.2)):
                self.web.wait_until_not_visible(
                    moreorderlist.ORDER_LIST_LOADER_IMG)

            if len(self.web.find_elements(locator=moreorderlist.ORDERS)) > 0:
                display_count -= 1
            else:
                sleep(seconds=1)
            max_retry -= 1

    def __select_order_with_id(self, el_id: str):
        self.web.wait_until_not_visible(
            moreorderlist.ORDER_LIST_LOADER_IMG)
        self.web.wait_until_visible(locator=f"id:{el_id}")

        try_count = 5
        while not self.web.attribute_ends_with(locator=f"id:{el_id}", attribute="class", exp_value="selected"):
            if try_count == 0:
                raise Exception(f"Cannot select order with id: {el_id}.")
            self.web.click(locator=f"id:{el_id}")
            sleep(seconds=0.2)
            try_count -= 1

    def __get_details(self, order_id: str, phone_number: str) -> OrderDetails:
        self.logger.info("*********GETTING DETAILS*********")
        self.web.wait_until_text_is_not_empty(
            locator=morelanding.TIME_DISPLAY)
        self.web.wait_until_text_contains(locator=morelanding.PHONE, exp_value=phone_number,
                                           ignore_case=True, ignore_space=True)

        self.web.wait_until_found(
            locator=morelanding.ORDER_NUMBER)
        order_number = self.web.get_text(
            locator=morelanding.ORDER_NUMBER)

        self.web.wait_until_found(
            locator=morelanding.ORDER_VERSION)
        order_version = self.web.get_text(
            locator=morelanding.ORDER_VERSION)

        create_time = self.web.get_text(
            locator=morelanding.TIME_DISPLAY)

        self.web.wait_until_visible(locator=morelanding.AGENT)
        self.web.wait_until_text_is_not_empty(
            locator=morelanding.AGENT, timeout=timedelta(seconds=2))
        agent = self.web.get_text(locator=morelanding.AGENT)

        self.web.wait_until_text_is_not_empty(locator=morelanding.PAYMENT_TYPE,
                                               timeout=timedelta(seconds=2))
        payment_type = self.web.get_text(
            locator=morelanding.PAYMENT_TYPE)
        if "(" in payment_type and ")" in payment_type:
            tip = payment_type.split("(")[1].replace(")", "").strip()
            payment_type = payment_type.split("(")[0].strip()
        else:
            tip = None

        self.web.wait_until_text_is_not_empty(locator=morelanding.ORDER_TYPE,
                                               timeout=timedelta(seconds=2))
        order_type = self.web.get_text(
            locator=morelanding.ORDER_TYPE)

        self.web.wait_until_text_is_not_empty(locator=morelanding.ORDER_STATUS,
                                               timeout=timedelta(seconds=2))
        ord_status = self.web.get_text(
            locator=morelanding.ORDER_STATUS)

        self.web.wait_until_text_is_not_empty(
            locator=morelanding.PHONE, timeout=timedelta(seconds=2))
        phone = self.web.get_text(locator=morelanding.PHONE)

        new_cust = False
        if "(NW)" in phone:
            phone = phone.replace("(NW)", "").strip()
            new_cust = True

        if "/" in phone:
            phone1 = phone.split("/")[0].strip()
            phone2 = phone.split("/")[1].strip()
        else:
            phone1 = phone
            phone2 = None

        cust_name = None
        if self.web.is_visible(locator=morelanding.CUSTOMER_NAME, timeout=timedelta(seconds=0.1)):
            self.web.wait_until_text_is_not_empty(locator=morelanding.CUSTOMER_NAME,
                                                   timeout=timedelta(seconds=2))
            cust_name = self.web.get_text(
                locator=morelanding.CUSTOMER_NAME)

        street1 = None
        address_type = None
        if self.web.is_visible(locator=morelanding.STREET1, timeout=timedelta(seconds=0.1)):
            self.web.wait_until_text_is_not_empty(locator=morelanding.STREET1,
                                                   timeout=timedelta(seconds=2))
            street1 = self.web.get_text(
                locator=morelanding.STREET1)
            if street1.endswith("(hse)"):
                street1 = street1.removesuffix("(hse)").strip()
                address_type = "hse"
            elif street1.endswith("(apt)"):
                street1 = street1.removesuffix("(apt)")
                address_type = "apt"
            elif street1.endswith("(biz)"):
                street1 = street1.removesuffix("(biz)")
                address_type = "biz"

        street2 = None
        if self.web.is_visible(locator=morelanding.STREET2, timeout=timedelta(seconds=0.1)):
            self.web.wait_until_text_is_not_empty(locator=morelanding.STREET2,
                                                   timeout=timedelta(seconds=2))
            street2 = self.web.get_text(
                locator=morelanding.STREET2)

        city = None
        if self.web.is_visible(locator=morelanding.CITY, timeout=timedelta(seconds=0.1)):
            self.web.wait_until_text_is_not_empty(locator=morelanding.CITY,
                                                   timeout=timedelta(seconds=2))
            city = self.web.get_text(locator=morelanding.CITY)

        order_remark = None
        if self.web.is_visible(locator=morelanding.ORDER_REMARK, timeout=timedelta(seconds=0.1)):
            self.web.wait_until_text_is_not_empty(locator=morelanding.ORDER_REMARK,
                                                   timeout=timedelta(seconds=2))
            order_remark = self.web.get_text(
                locator=morelanding.ORDER_REMARK)

        estimated_time = None
        if self.web.is_visible(locator=morelanding.ESTIMATED_TIME, timeout=timedelta(seconds=0.1)):
            self.web.wait_until_text_is_not_empty(locator=morelanding.ESTIMATED_TIME,
                                                   timeout=timedelta(seconds=2))
            estimated_time = self.web.get_text(
                locator=morelanding.ESTIMATED_TIME)

        conf_note = None
        if self.web.is_visible(locator=morelanding.CONF_NOTE, timeout=timedelta(seconds=0.1)):
            self.web.wait_until_text_is_not_empty(locator=morelanding.CONF_NOTE,
                                                   timeout=timedelta(seconds=2))
            conf_note = self.web.get_text(
                locator=morelanding.CONF_NOTE)

        rush_comment = None
        if self.web.is_visible(locator=morelanding.RUSH_COMMENT, timeout=timedelta(seconds=0.1)):
            self.web.wait_until_text_is_not_empty(locator=morelanding.RUSH_COMMENT,
                                                   timeout=timedelta(seconds=2))
            rush_comment = self.web.get_text(
                locator=morelanding.RUSH_COMMENT)

        void_comment = None
        if self.web.is_visible(locator=morelanding.VOID_COMMENT, timeout=timedelta(seconds=0.1)):
            self.web.wait_until_text_is_not_empty(locator=morelanding.VOID_COMMENT,
                                                   timeout=timedelta(seconds=2))
            void_comment = self.web.get_text(
                locator=morelanding.VOID_COMMENT)

        return OrderDetails(oid=order_id, order_number=order_number, order_version=order_version,
                            create_time=create_time, agent=agent, payment_type=payment_type, tip=tip,
                            order_type=order_type, order_status=ord_status, phone1=phone1, phone2=phone2,
                            customer_name=cust_name, street1=street1, street2=street2, city=city,
                            order_remark=order_remark, conf_note=conf_note, rush_comment=rush_comment,
                            void_comment=void_comment, address_type=address_type, new_cust=new_cust,
                            estimated_time=estimated_time)

    @keyword(tags=("RestaurantKeywords", "OrderListKeywords", "AssertionKeywords"))
    def details_of_order_should_be(self, act_order_details: OrderDetails,
                                   exp_phone1: str = None,
                                   exp_order_number: str = None,
                                   exp_order_version: str = None,
                                   exp_agent: str = None,
                                   exp_payment_type: str = None,
                                   exp_order_type: str = None,
                                   exp_order_status: str = None,
                                   exp_phone2: str = None,
                                   exp_cust_name: str = None,
                                   exp_street: str = None,
                                   exp_street2: str = None,
                                   exp_address_type: str = None,
                                   exp_city: str = None,
                                   exp_order_remark: str = None,
                                   exp_conf_note: str = None,
                                   exp_tip: str = None,
                                   exp_estimated_time: str = None,
                                   exp_new_cust_status: bool = None,
                                   exp_rush_comment: str = None,
                                   exp_void_comment: str = None
                                   ):
        sa = self.asserts.SoftAssert()

        if exp_phone1 is not None:
            sa.assert_equal(
                actual=act_order_details['phone1'], exp=exp_phone1, desc="Phone1.")
        if exp_order_number is not None:
            sa.assert_equal(
                actual=act_order_details['order_number'], exp=exp_order_number, desc="Order number.")
        if exp_order_version is not None:
            sa.assert_equal(
                actual=act_order_details['order_version'], exp=exp_order_version, desc="Order version.")
        if exp_agent is not None:
            sa.assert_equal(
                actual=act_order_details['agent'], exp=exp_agent, desc="Agent.")
        if exp_payment_type is not None:
            sa.assert_equal(
                actual=act_order_details['payment_type'], exp=exp_payment_type, desc="Payment type.")
        if exp_order_type is not None:
            sa.assert_equal(
                actual=act_order_details['order_type'], exp=exp_order_type, desc="Order type.")
        if exp_order_status is not None:
            sa.assert_equal(
                actual=act_order_details['order_status'], exp=exp_order_status, desc="Order status.")
        if exp_phone2 is not None:
            sa.assert_equal(
                actual=act_order_details['phone2'], exp=exp_phone2, desc="Phone2.")
        if exp_cust_name is not None:
            sa.assert_equal(
                actual=act_order_details['customer_name'], exp=exp_cust_name, desc="Customer name.")
        if exp_street is not None:
            sa.assert_equal(
                actual=act_order_details['street1'], exp=exp_street, desc="Street1.")
        if exp_street2 is not None:
            sa.assert_equal(
                actual=act_order_details['street2'], exp=exp_street2, desc="Street2.")
        if exp_address_type is not None:
            sa.assert_equal(
                actual=act_order_details['address_type'], exp=exp_address_type, desc="Address type.")
        if exp_city is not None:
            sa.assert_equal(
                actual=act_order_details['city'], exp=exp_city, desc="City.")
        if exp_order_remark is not None:
            sa.assert_equal(
                actual=act_order_details['order_remark'], exp=exp_order_remark, desc="Order remark.")
        if exp_conf_note is not None:
            sa.assert_equal(
                actual=act_order_details['conf_note'], exp=exp_conf_note, desc="Conf note.")
        if exp_tip is not None:
            sa.assert_equal(
                actual=act_order_details['tip'], exp=exp_tip, desc="Tip.")
        if exp_estimated_time is not None:
            sa.assert_equal(
                actual=act_order_details['estimated_time'], exp=exp_estimated_time, desc="Estimated time.")
        if exp_new_cust_status is not None:
            sa.assert_equal(
                actual=act_order_details['new_cust'], exp=exp_new_cust_status, desc="New customer status.")
        if exp_rush_comment is not None:
            sa.assert_equal(
                actual=act_order_details['rush_comment'], exp=exp_rush_comment, desc="Rush comment.")
        if exp_void_comment is not None:
            sa.assert_equal(
                actual=act_order_details['void_comment'], exp=exp_rush_comment, desc="Void comment.")
        sa.assert_that_date_format_is(date=act_order_details['create_time'], exp_format="%m/%d/%Y  %I:%M %p",
                                      desc="Create time format")
        sa.assert_that_text_is_not_empty(
            txt=act_order_details['create_time'], desc="Create time.")
        sa.assert_all()

    def __parser_order_btn_text(self, text: str):
        split_text: list[str] = text.split()
        self.logger.debug(f"SPLIT TEXT: {split_text}")
        if len(split_text) > 5:
            header = f"{split_text[0]} {split_text[1]} {split_text[2]}"
            time = f"{split_text[3]} {split_text[4]}"
            phone = f"{split_text[-2]} {split_text[-1]}"
        else:
            header = split_text[0]
            time = f"{split_text[1]} {split_text[2]}"
            phone = f"{split_text[-2]} {split_text[-1]}"
        self.logger.debug(f"Parsed: header={header} time={time} phone={phone}")
        return header, time, phone