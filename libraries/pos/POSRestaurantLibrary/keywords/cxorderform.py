from datetime import timedelta
from robot.api.deco import keyword
from libraries.pos.POSRestaurantLibrary.dto.cxorderformdetails import CustomerOrderFormDetails
from libraries.pos.POSRestaurantLibrary.locators.modals import infomodal
from libraries.pos.POSRestaurantLibrary.locators import restaurantlanding
from libraries.pos.POSRestaurantLibrary.keywords.modals.datanotify import DataNotifyAlertKeywords
from libraries.pos.POSRestaurantLibrary.locators.frame import POS_RESTAURANT_FRAME
from autocore.bases import WebLibraryBase, WebLibraryComponent
from autocore.web.webactions import  sleep


def _get_numbers_only(text: str) -> str:
    text_copy = ""
    for i in text:
        if i.isnumeric():
            text_copy = text_copy + i
    return text_copy.strip()


class CxOrderFormKeywords(WebLibraryComponent):
    
    def __init__(self, library: WebLibraryBase, timeout: timedelta = ...):
        super().__init__(library, timeout)
        self.__data_notify_alert = DataNotifyAlertKeywords(library=library, timeout=timeout)

    @keyword(tags=("RestaurantKeywords", "CustomerOrderFormKeywords"))
    def fill_out_customer_order_form(
            self,
            order_type: str = None,
            phone_number1: str = None,
            phone_number2: str = None,
            name: str = None,
            street: str = None,
            address_type: str = None,
            address_2: str = None,
            city: str = None,
            order_remark: str = None,
            conf_note: str = None,
            call_skill: str = None,
            dismiss_alerts: bool = True,
            _: CustomerOrderFormDetails = None
    ) -> CustomerOrderFormDetails:
        """Fill out customer order form using the provided information.
        Dismisses alert that may pop up when filling out form by default, can be changed by setting ``dismiss_alerts`` to ``False``.

        - ``order_type`` (case-sensitive). Below are the accepted values.
        If needed to select more than one ``order_type``,separate it using ``|``.
        -- DELIVERY
        -- PICKUP
        -- ONLINE
        -- DELIVERY | ONLINE
        -- DELIVERY | PICKUP

        - ``address_type`` (case-sensitive). Below are the accepted values.
        -- BIZ
        -- HOUSE
        -- APT

        - ``call_skill`` (case-sensitive). Below are the accepted values.
        -- DF
        -- SP
        -- CH
        -- SB

        Pre-requisite: To use this keyword make sure that a restaurant is open. See `Open Restaurant In POS Homepage`.

        Return the provided arguments as `CustomerOrderFormDetails`.
        """
        if order_type is not None:
            order_type = order_type.replace(" ", "")
            if "|" in order_type:
                order_type_list = order_type.split("|")
            else:
                order_type_list = [order_type]

            for i in order_type_list:
                self.__select_order_type(order_type=i, dismiss_alerts=dismiss_alerts)
        else:
            order_type_list = None

        parameters = CustomerOrderFormDetails(
            selected_order_type=order_type_list,
            phone_number1=phone_number1,
            phone_number2=phone_number2,
            name=name,
            street=street,
            address_type=address_type,
            city=city,
            order_remark=order_remark,
            conf_note=conf_note,
            selected_call_skill=call_skill
        )

        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(locator=restaurantlanding.PHONE_NUMBER1_FLD)
            if phone_number1 is not None:
                phone_number1 = _get_numbers_only(phone_number1)
                self.__input_phone_number(locator=restaurantlanding.PHONE_NUMBER1_FLD,
                                          phone_number=phone_number1)
                self.web.wait_until_enabled(locator=restaurantlanding.NAME_FLD)
                if dismiss_alerts:
                    self.__data_notify_alert.close_data_notify_alerts_helper()

            if phone_number2 is not None:
                phone_number2 = _get_numbers_only(phone_number2)
                self.__input_phone_number(locator=restaurantlanding.PHONE_NUMBER2_FLD,
                                          phone_number=phone_number2)
                self.web.wait_until_enabled(locator=restaurantlanding.NAME_FLD)
                if dismiss_alerts:
                    self.__data_notify_alert.close_data_notify_alerts_helper()

            if name is not None:
                self.web.input_text(locator=restaurantlanding.NAME_FLD, text=name)

            if address_type is not None:
                self.__select_address_type(address_type)

            if street is not None:
                self.web.input_text(locator=restaurantlanding.STREET_FLD, text=street, press_enter=True)

            if address_2 is not None:
                self.web.input_text(locator=restaurantlanding.ADDRESS2_FLD, text=address_2)

            if city is not None:
                self.web.input_text(locator=restaurantlanding.CITY_FLD, text=city)

            if order_remark is not None:
                self.web.input_text(locator=restaurantlanding.ORDER_REMARK_FLD, text=order_remark)

            if conf_note is not None:
                self.web.input_text(locator=restaurantlanding.CONF_NOTE_FLD, text=conf_note)

            if call_skill is not None:
                if call_skill == 'DF':
                    if not self.web.is_selected(locator=restaurantlanding.CALL_SKILL_DF):
                        self.web.click(locator=restaurantlanding.CALL_SKILL_DF)
                elif call_skill == 'SP':
                    if not self.web.is_selected(locator=restaurantlanding.CALL_SKILL_SP):
                        self.web.click(locator=restaurantlanding.CALL_SKILL_SP)
                elif call_skill == 'CH':
                    if not self.web.is_selected(locator=restaurantlanding.CALL_SKILL_CH):
                        self.web.click(locator=restaurantlanding.CALL_SKILL_CH)
                elif call_skill == 'SB':
                    if not self.web.is_selected(locator=restaurantlanding.CALL_SKILL_SB):
                        self.web.click(locator=restaurantlanding.CALL_SKILL_SB)
                else:
                    raise Exception(f"Provided call skill [ {call_skill} ] is not supported.")
                
            if dismiss_alerts and self.web.is_visible(locator=infomodal.HEADER, timeout=timedelta(seconds=0.5)):
                self.web.click(locator=infomodal.OK_BTN)
                self.web.wait_until_not_visible(locator=infomodal.HEADER)

        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
        self.logger.debug(parameters)
        return parameters

    @keyword(tags=("RestaurantKeywords", "CustomerOrderFormKeywords"))
    def double_check_customer_order_form(self, form_details: CustomerOrderFormDetails):
        """Double check that the value of the customer order form is correct based on the value inputted using `Fill Out Customer Order Form`.

         Pre-requisite: To use this keyword make sure that a restaurant is open. See `Open Restaurant In POS Homepage`.
        """
        selected_order_type: list = form_details.get('selected_order_type')
        phone_number1 = form_details.get('phone_number1')
        phone_number2 = form_details.get('phone_number2')
        name = form_details.get('name')
        street = form_details.get('street')
        address_type = form_details.get('address_type')
        city = form_details.get('city')
        order_remark = form_details.get('order_remark')
        conf_note = form_details.get('conf_note')
        selected_call_skill = form_details.get('selected_call_skill')

        self.web.select_frame(locator=POS_RESTAURANT_FRAME)

        has_mistake = False
        mistake_fields = []
        try:
            if selected_order_type is not None:
                for i in selected_order_type:
                    if i == "DELIVERY":
                        self.web.wait_until_visible(locator=restaurantlanding.DELIVERY_BTN)
                        if not self.__is_element_selected(locator=restaurantlanding.DELIVERY_BTN):
                            has_mistake = True
                            mistake_fields.append('Order Type')
                            self.web.click(locator=restaurantlanding.DELIVERY_BTN)
                    elif i == "PICKUP":
                        self.web.wait_until_visible(locator=restaurantlanding.PICKUP_BTN)
                        if not self.__is_element_selected(locator=restaurantlanding.PICKUP_BTN):
                            has_mistake = True
                            mistake_fields.append('Order Type')
                            self.web.click(locator=restaurantlanding.PICKUP_BTN)
                    elif i == "ONLINE":
                        self.web.wait_until_visible(locator=restaurantlanding.ONLINE_BTN)
                        if not self.__is_element_selected(locator=restaurantlanding.ONLINE_BTN):
                            has_mistake = True
                            mistake_fields.append('Order Type')
                            self.web.click(locator=restaurantlanding.ONLINE_BTN)
                            self.__data_notify_alert.close_data_notify_alerts_helper()

            self.web.wait_until_visible(locator=restaurantlanding.PHONE_NUMBER1_FLD)
            if phone_number1 is not None:
                act_phone_number1 = self.web.get_value(locator=restaurantlanding.PHONE_NUMBER1_FLD)

                if _get_numbers_only(phone_number1) != _get_numbers_only(act_phone_number1):
                    has_mistake = True
                    mistake_fields.append('Phone number 1')
                    phone_number1 = _get_numbers_only(phone_number1)
                    self.__input_phone_number(locator=restaurantlanding.PHONE_NUMBER1_FLD,
                                              phone_number=phone_number1)
                    self.__data_notify_alert.close_data_notify_alerts_helper()

            if phone_number2 is not None:
                act_phone_number2 = self.web.get_value(locator=restaurantlanding.PHONE_NUMBER2_FLD)

                if _get_numbers_only(phone_number2) != _get_numbers_only(act_phone_number2):
                    has_mistake = True
                    mistake_fields.append('Phone number 2')
                    act_phone_number2 = _get_numbers_only(act_phone_number2)
                    self.__input_phone_number(locator=restaurantlanding.PHONE_NUMBER2_FLD,
                                              phone_number=act_phone_number2)
                    self.__data_notify_alert.close_data_notify_alerts_helper()

            if name is not None:
                act_name = self.web.get_value(locator=restaurantlanding.NAME_FLD)

                if act_name != name:
                    has_mistake = True
                    mistake_fields.append('Name')
                    self.web.input_text(locator=restaurantlanding.NAME_FLD, text=name)

            if street is not None:
                act_street = self.web.get_value(locator=restaurantlanding.STREET_FLD)

                if act_street != street:
                    has_mistake = True
                    mistake_fields.append('Street')
                    self.web.input_text(locator=restaurantlanding.STREET_FLD, text=act_street, press_enter=True)

            if address_type is not None:
                if address_type == "BIZ":
                    if not self.web.is_selected(locator=restaurantlanding.BIZ_ADDRESS_TYPE_BTN):
                        has_mistake = True
                        mistake_fields.append("Address Type")
                        self.web.click(locator=restaurantlanding.BIZ_ADDRESS_TYPE_BTN)
                elif address_type == "HOUSE":
                    if not self.web.is_selected(locator=restaurantlanding.HOUSE_ADDRESS_TYPE_BTN):
                        has_mistake = True
                        mistake_fields.append("Address Type")
                        self.web.click(locator=restaurantlanding.HOUSE_ADDRESS_TYPE_BTN)
                elif address_type == "APT":
                    if not self.web.is_selected(locator=restaurantlanding.APT_ADDRESS_TYPE_BTN):
                        has_mistake = True
                        mistake_fields.append("Address Type")
                        self.web.click(locator=restaurantlanding.APT_ADDRESS_TYPE_BTN)

            if city is not None:
                act_city = self.web.get_value(locator=restaurantlanding.CITY_FLD)

                if act_city != city:
                    has_mistake = True
                    mistake_fields.append("City")
                    self.web.input_text(locator=restaurantlanding.CITY_FLD, text=city)

            if order_remark is not None:
                act_order_remark = self.web.get_value(locator=restaurantlanding.ORDER_REMARK_FLD)

                if act_order_remark != order_remark:
                    has_mistake = True
                    mistake_fields.append("Order Remark")
                    self.web.input_text(locator=restaurantlanding.ORDER_REMARK_FLD, text=order_remark)

            if conf_note is not None:
                act_conf_note = self.web.get_value(locator=restaurantlanding.CONF_NOTE_FLD)

                if act_conf_note != conf_note:
                    has_mistake = True
                    mistake_fields.append("Conf Note")
                    self.web.input_text(locator=restaurantlanding.CONF_NOTE_FLD, text=conf_note)

            if selected_call_skill is not None:
                if selected_call_skill == 'DF':
                    if not self.web.is_selected(locator=restaurantlanding.CALL_SKILL_DF):
                        has_mistake = True
                        mistake_fields.append("Call Skill")
                        self.web.click(locator=restaurantlanding.CALL_SKILL_DF)
                elif selected_call_skill == 'SP':
                    if not self.web.is_selected(locator=restaurantlanding.CALL_SKILL_SP):
                        has_mistake = True
                        mistake_fields.append("Call Skill")
                        self.web.click(locator=restaurantlanding.CALL_SKILL_SP)
                elif selected_call_skill == 'CH':
                    if not self.web.is_selected(locator=restaurantlanding.CALL_SKILL_CH):
                        has_mistake = True
                        mistake_fields.append("Call Skill")
                        self.web.click(locator=restaurantlanding.CALL_SKILL_CH)
                elif selected_call_skill == 'SB':
                    if not self.web.is_selected(locator=restaurantlanding.CALL_SKILL_SB):
                        has_mistake = True
                        mistake_fields.append("Call Skill")
                        self.web.click(locator=restaurantlanding.CALL_SKILL_SB)

        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

        if has_mistake:
            self.logger.warn(
                f"There were changes in the following customer order form values {mistake_fields} as compared to the inputted values. An attempt to correct it was made.")

    @keyword(tags=("RestaurantKeywords", "CustomerOrderFormKeywords"))
    def get_customer_order_form_details(self, _: CustomerOrderFormDetails = None) -> CustomerOrderFormDetails:
        """Get the values of the customer order form and return it as `CustomerOrderFormDetails` object.

        Pre-requisite: To use this keyword make sure that a restaurant is open.
        See `Open Restaurant In POS Homepage`.

        Examples:
            | ${details}    |   Get Customer Order Form Details            |
            | Log           |   ${details}[selected_order_type]            |
            | ${details}    |   Get Customer Order Form Details            |
            | Log           |   ${details}[phone_number1]                  |
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            selected_order_type = []
            self.web.wait_until_visible(locator=restaurantlanding.DELIVERY_BTN)
            if self.__is_element_selected(locator=restaurantlanding.DELIVERY_BTN):
                selected_order_type.append('DELIVERY')
            self.web.wait_until_visible(locator=restaurantlanding.PICKUP_BTN)
            if self.__is_element_selected(locator=restaurantlanding.PICKUP_BTN):
                selected_order_type.append('PICKUP')
            if self.web.is_visible(locator=restaurantlanding.ONLINE_BTN, timeout=timedelta(seconds=1)):
                if self.__is_element_selected(locator=restaurantlanding.ONLINE_BTN):
                    selected_order_type.append('ONLINE')

            phone_number1 = self.web.get_value(locator=restaurantlanding.PHONE_NUMBER1_FLD)
            phone_number2 = self.web.get_value(locator=restaurantlanding.PHONE_NUMBER2_FLD)
            name = self.web.get_value(locator=restaurantlanding.NAME_FLD)
            street = self.web.get_value(locator=restaurantlanding.STREET_FLD)

            address_type = None
            if self.web.is_selected(locator=restaurantlanding.HOUSE_ADDRESS_TYPE_BTN):
                address_type = 'HOUSE'
            if self.web.is_selected(locator=restaurantlanding.BIZ_ADDRESS_TYPE_BTN):
                address_type = 'BIZ'
            if self.web.is_selected(locator=restaurantlanding.APT_ADDRESS_TYPE_BTN):
                address_type = 'APT'

            miles = self.web.get_value(locator=restaurantlanding.MILES)
            city = self.web.get_value(locator=restaurantlanding.CITY_FLD)
            order_remark = self.web.get_value(locator=restaurantlanding.ORDER_REMARK_FLD)
            conf_note = self.web.get_value(locator=restaurantlanding.CONF_NOTE_FLD)

            selected_call_skill = None
            if self.web.is_selected(locator=restaurantlanding.CALL_SKILL_DF):
                selected_call_skill = 'DF'
            if self.web.is_selected(locator=restaurantlanding.CALL_SKILL_SP):
                selected_call_skill = 'SP'
            if self.web.is_selected(locator=restaurantlanding.CALL_SKILL_SB):
                selected_call_skill = 'SB'
            if self.web.is_selected(locator=restaurantlanding.CALL_SKILL_CH):
                selected_call_skill = 'CH'

            details = CustomerOrderFormDetails(
                selected_order_type=selected_order_type,
                phone_number1=phone_number1,
                phone_number2=phone_number2,
                name=name,
                street=street,
                address_type=address_type,
                miles=miles,
                city=city,
                order_remark=order_remark,
                conf_note=conf_note,
                selected_call_skill=selected_call_skill
            )
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

        self.logger.debug(details)
        return details

    def __input_phone_number(self, locator: str, phone_number: str = None):
        self.web.click(locator=locator)
        self.web.delete_text_via_keys(locator=locator)
        self.web.type_number(locator=locator, number=phone_number)
        self.web.press_enter(locator=locator)
        sleep(seconds=1)

    def __select_address_type(self, address_type: str):
        if address_type == "BIZ":
            self.web.click(locator=restaurantlanding.BIZ_ADDRESS_TYPE_BTN)
        elif address_type == "HOUSE":
            self.web.click(locator=restaurantlanding.HOUSE_ADDRESS_TYPE_BTN)
        elif address_type == "APT":
            self.web.click(locator=restaurantlanding.APT_ADDRESS_TYPE_BTN)
        else:
            raise Exception(f"Provided address type [ {address_type} ] is not supported.")

    def __select_order_type(self, order_type: str, dismiss_alerts: bool):
        order_type = order_type.replace(" ", "")

        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            if order_type == "DELIVERY":
                self.web.wait_until_visible(locator=restaurantlanding.DELIVERY_BTN)
                if not self.__is_element_selected(locator=restaurantlanding.DELIVERY_BTN):
                    self.web.click(locator=restaurantlanding.DELIVERY_BTN)
            elif order_type == "PICKUP":
                self.web.wait_until_visible(locator=restaurantlanding.PICKUP_BTN)
                if not self.__is_element_selected(locator=restaurantlanding.PICKUP_BTN):
                    self.web.click(locator=restaurantlanding.PICKUP_BTN)
            elif order_type == "ONLINE":
                self.web.wait_until_visible(locator=restaurantlanding.ONLINE_BTN)
                if not self.__is_element_selected(locator=restaurantlanding.ONLINE_BTN):
                    self.web.click(locator=restaurantlanding.ONLINE_BTN)
                    if dismiss_alerts:
                        self.__data_notify_alert.close_data_notify_alerts_helper()
            else:
                raise Exception("Provided order type is not supported.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    def __is_element_selected(self, locator: str) -> bool:
        return self.web.attribute_ends_with(locator=locator, attribute="class", exp_value="selected")
