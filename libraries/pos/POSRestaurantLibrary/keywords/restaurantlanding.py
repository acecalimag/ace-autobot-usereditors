from robot.api.deco import keyword
from libraries.pos.POSRestaurantLibrary.dto.orderbilldetails import OrderBillDetails
from libraries.pos.POSRestaurantLibrary.dto.selecteddishdetails import SelectedDishDetails
from libraries.pos.POSRestaurantLibrary.locators import restaurantlanding
from libraries.pos.POSRestaurantLibrary.locators.frame import POS_RESTAURANT_FRAME
from autocore.bases import WebLibraryComponent
from libraries.pos.config import POS_RESTAURANT_DISPLAY_AREA


class RestaurantLandingKeywords(WebLibraryComponent):

    @keyword(tags=("RestaurantKeywords",))
    def get_order_bill_details(self) -> OrderBillDetails:
        """Get the order bill details and return it as `OrderBillDetails` object.

        Pre-requisite: To use this keyword make sure that a restaurant is open. See `Open Restaurant In POS Homepage`.

        Examples:
            | ${details}    |   Get Order Bill Details              |
            | Log           |   ${details}[discount]                |
            | ${details}    |   Get Order Bill Details              |
            | Log           |   ${details}[total]                   |
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(locator=restaurantlanding.GRAND_TOTAL)
            details = OrderBillDetails(
                discount=self.web.get_value(
                    locator=restaurantlanding.DISCOUNT),
                subtotal=self.web.get_text(
                    locator=restaurantlanding.SUBTOTAL).split("$")[1],
                tax=self.web.get_text(
                    locator=restaurantlanding.TAX_AMOUNT).replace("$", ""),
                delivery=self.web.get_value(
                    locator=restaurantlanding.DELIVERY_FEE),
                total=self.web.get_text(
                    locator=restaurantlanding.GRAND_TOTAL).split('$')[1]
            )
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

        self.logger.debug(details)
        return details

    @keyword(tags=("RestaurantKeywords",))
    def click_add_order_quantity_button(self):
        """Click add order quantity button.

        Pre-requisite: To use this keyword make sure that a restaurant is open. See `Open Restaurant In POS Homepage`.
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(
                locator=restaurantlanding.ADD_ORDER_QTY_BTN)
            self.web.click(locator=restaurantlanding.ADD_ORDER_QTY_BTN)
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("RestaurantKeywords",))
    def click_minus_order_quantity_button(self):
        """Click minus order quantity button.

         Pre-requisite: To use this keyword make sure that a restaurant is open. See `Open Restaurant In POS Homepage`.
         """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(
                locator=restaurantlanding.MINUS_QUANTITY_BTN)
            self.web.click(locator=restaurantlanding.MINUS_QUANTITY_BTN)
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("RestaurantKeywords",))
    def click_save_order_button(self):
        """Click save order button.

        Pre-requisite: To use this keyword make sure that a restaurant is open. See `Open Restaurant In POS Homepage`.
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(locator=restaurantlanding.SAVE)
            self.web.click(locator=restaurantlanding.SAVE)
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("RestaurantKeywords",))
    def click_home_button(self):
        """Click home button.

        Pre-requisite: To use this keyword make sure that a restaurant is open. See `Open Restaurant In POS Homepage`.
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(locator=restaurantlanding.HOME_BTN)
            self.web.click(locator=restaurantlanding.HOME_BTN)
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("RestaurantKeywords",))
    def click_credit_card_button(self):
        """Click credit card button.

        Pre-requisite: To use this keyword make sure that a restaurant is open. See `Open Restaurant In POS Homepage`.
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(
                locator=restaurantlanding.CREDIT_CARD_BTN)
            self.web.click(locator=restaurantlanding.CREDIT_CARD_BTN)
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("RestaurantKeywords",))
    def click_send_button(self):
        """Click send order button.

        Pre-requisite: To use this keyword make sure that a restaurant is open. See `Open Restaurant In POS Homepage`.
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(locator=restaurantlanding.SEND_BTN)
            self.web.click(locator=restaurantlanding.SEND_BTN)
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("RestaurantKeywords", "RestaurantDisplayAreaKeywords"))
    def wait_until_restaurant_display_area_is_visible(self, en_name: str):
        """Wait until the restaurant display area is visible.
        Will check that the correct restaurant is opened using the provided ``en_name``.

        Pre-requisite: Use this keyword when opening a restaurant. See `Open Restaurant In POS Homepage`.
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(
                locator=restaurantlanding.DISPLAY_AREA_RESTAURANT_COMMENT, timeout=POS_RESTAURANT_DISPLAY_AREA)

            res_name_id: str = "resName"
            js_script_show = f"document.getElementById('{res_name_id}').style.display = 'block'"
            js_script_hide = f"document.getElementById('{res_name_id}').style.display = 'none'"

            self.web.execute_javascript(js_script_show)
            act_res_name = self.web.get_text(locator=f"id:{res_name_id}")
            self.web.execute_javascript(js_script_hide)

            if act_res_name != en_name:
                raise Exception(
                    f"Opened restaurant is incorrect. Should be [ {en_name} ] but opened [ {act_res_name} ].")

        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("RestaurantKeywords", "OrderDisplayKeywords"))
    def get_details_of_the_selected_dishes(self, _: SelectedDishDetails = None) -> list[SelectedDishDetails]:
        """Get the details of the selected dishes from the order display area and return is as an object of `SelectedDishDetails`.

        Pre-requisite: To use this keyword make sure that a restaurant is open. See `Open Restaurant In POS Homepage`.

        Examples:
            | ${details}    |   Get Details Of The Selected Dishes              |
            | Log           |   ${details}[quantity]                            |
            | ${details}    |   Get Details Of The Selected Dishes              |
            | Log           |   ${details}[price]                               |
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(
                locator=restaurantlanding.ORDER_DISPLAY)
            item_count = self.web.count(
                locator=restaurantlanding.ORDER_ITEM_DIV)

            details = []
            for i in range(1, item_count + 1):
                details.append(
                    SelectedDishDetails(
                        quantity=self.web.get_text(
                            locator=restaurantlanding.ORDER_QUANTITY_INDEXED_TPL.format(i)),
                        size=self.web.get_text(
                            locator=restaurantlanding.ORDER_SIZE_INDEXED_TPL.format(i)),

                        description=self.web.get_text(
                            locator=restaurantlanding.ORDER_DESCRIPTION_INDEXED_TPL.format(i)),

                        price=self.web.get_text(
                            locator=restaurantlanding.ORDER_PRICE_INDEXED_TPL.format(i)).replace("$", "")
                    )
                )
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
        self.logger.debug(details)
        return details

    @keyword(tags=("RestaurantKeywords", "CustomerOrderFormKeywords"))
    def click_add_sub_order_button(self):
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.click(locator=restaurantlanding.NEW_SUB_ORDER_BTN)
            self.web.wait_until_visible(locator=restaurantlanding.SUB_ORDERS_BANNER)
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
            
    @keyword(tags=("RestaurantKeywords", "CustomerOrderFormKeywords"))
    def open_more_display_area(self):
        """Open the restaurant more display area if not yet open.

        Pre-requisite: To use this keyword make sure that a restaurant is open. See `Open Restaurant In POS Homepage`.
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(locator=restaurantlanding.MORE_BTN)
            if not self.web.attribute_ends_with(locator=restaurantlanding.MORE_BTN, attribute="class",
                                                 exp_value="selected"):
                self.web.click(locator=restaurantlanding.MORE_BTN)
                self.web.wait_until_not_visible(locator=moreorderlist.ORDER_LIST_LOADER_IMG)
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()