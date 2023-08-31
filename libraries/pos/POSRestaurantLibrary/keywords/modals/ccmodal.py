from datetime import timedelta
from enum import Enum

from robot.api.deco import keyword

from libraries.pos.POSRestaurantLibrary.dto.ccmodaldetails import CreditCardModalDetails
from libraries.pos.POSRestaurantLibrary.locators.frame import POS_RESTAURANT_FRAME
from libraries.pos.POSRestaurantLibrary.locators.modals import ccmodal
from libraries.pos.POSRestaurantLibrary.locators import restaurantlanding
from autocore.bases import WebLibraryComponent
from autocore.web.webactions import sleep


def _parse_date(date_str: str):
    month: str = date_str.split("/")[0].strip()
    year: str = date_str.split("/")[1].strip()
    if month.startswith("0"):
        month = month.replace("0", "")
    year = f"20{year}"
    return month, year


class CCFieldNames(Enum):
    CC_NUM = "CARD NUMBER"
    EXPI_DATE = "EXPIRATION DATE"
    CVV = "CVV"
    ZIP = "ZIP"


class CreditCardModalKeywords(WebLibraryComponent):

    @keyword(tags=("CreditCardModal", "ModalKeywords"))
    def fillout_credit_card_modal(self, credit_card_charge: str = None, cash_charge: str = None,
                                  tip: str = None, card_number: str = None, expi_date: str = None,
                                  cvv: str = None, postal_code: str = None, action: str = 'SUBMIT'):
        """Fillout the credit card modal using the provided information.

        - ``credit_card_charge``: the amount to be charged in the credit card
        - ``cash_charge``: the amount to be paid in cash
        - ``tip``: tip amount
        - ``card_number``: the card number
        - ``expi_date``: the expiration date of the card. must be in mm/yy format. E.g. 01/28
        - ``cvv``: the cvv or cvc of the card
        - ``postal_code``: postal code or the zip code
        - ``action``: the action to be performed. Below are the accepted values:
        -- ``NO_ACTION``: No action will be performed
        -- ``SUBMIT``: The default value. Will submit the form.
        -- ``CANCEL``: Will cancel filling out the form.
        -- ``CLEAR``: Will clear the credit card fields.
        -- ``UPDATE``: Will click the update credit card button
        -- ``PAY_CASH_INSTEAD``: Will click the pay cash instead button
        -- ``ADD_ON_PAY_CASH``: Will click the add on pay cash button
        -- ``ADD_ON_PAY_CREDIT_CARD``: Will click the add on pay credit card button
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(locator=ccmodal.MODAL)
            if credit_card_charge is not None:
                self.web.delete_text_via_keys(locator=ccmodal.CC_CHARGE_FLD)
                self.web.type_number(locator=ccmodal.CC_CHARGE_FLD, number=credit_card_charge)
                self.web.press_enter(locator=ccmodal.CC_CHARGE_FLD)
            if cash_charge is not None:
                def fillout_cash_charge():
                    self.web.delete_text_via_keys(locator=ccmodal.CASH_CHARGE_FLD)
                    self.web.type_number(locator=ccmodal.CASH_CHARGE_FLD, number=cash_charge)
                    self.web.press_enter(locator=ccmodal.CASH_CHARGE_FLD)
                    sleep(seconds=0.5)
                
                orig_cc_charge = self.web.get_value(locator=ccmodal.CC_CHARGE_FLD)
                fillout_cash_charge()
                
                new_cc_charge = self.web.get_value(locator=ccmodal.CC_CHARGE_FLD)
                try_count = 5
                while orig_cc_charge == new_cc_charge:
                    if try_count == 0:
                        break
                    fillout_cash_charge()
                    new_cc_charge = self.web.get_value(locator=ccmodal.CC_CHARGE_FLD)
                    try_count -= 1
                
            if tip is not None:
                self.web.delete_text_via_keys(locator=ccmodal.TIP_CHARGE_FLD)
                self.web.type_number(locator=ccmodal.TIP_CHARGE_FLD, number=tip)
                self.web.press_enter(locator=ccmodal.TIP_CHARGE_FLD)

            self.web.switch_to_default_content()
            for i in range(15):
                self.web.select_frame(locator=POS_RESTAURANT_FRAME)
                if self.web.is_visible(locator=ccmodal.EXISTING_CARD_NUMBER,
                                        timeout=timedelta(seconds=0.2)):
                    self.__perfom_action_on_existing_card_modal(action=action)
                    break

                if self.web.is_visible(locator=ccmodal.NON_PROPAY_CC_NUMBER,
                                        timeout=timedelta(seconds=0.2)):
                    if card_number is not None:
                        self.web.input_text(locator=ccmodal.NON_PROPAY_CC_NUMBER, text=card_number)
                    if expi_date is not None:
                        self.web.input_text(locator=ccmodal.NON_PROPAY_EXPI_DATE, text=expi_date)
                    if cvv is not None:
                        self.web.input_text(locator=ccmodal.NON_PROPAY_CVC, text=cvv)
                    if postal_code is not None:
                        self.web.input_text(locator=ccmodal.NON_PROPAY_ZIP, text=postal_code)
                    self.__perform_action_on_non_propay_form(action=action)
                    break

                self.web.select_frame(locator=ccmodal.PROPAY_IFRAME)
                if self.web.is_visible(locator=ccmodal.PROPAY_CARD_NUMBER,
                                        timeout=timedelta(seconds=0.2)):
                    self.web.switch_to_default_content()
                    self.web.select_frame(locator=POS_RESTAURANT_FRAME)
                    self.web.select_frame(locator=ccmodal.PROPAY_IFRAME)
                    if card_number is not None:
                        self.web.input_text(locator=ccmodal.PROPAY_CARD_NUMBER, text=card_number)
                    if expi_date is not None:
                        month, year = _parse_date(expi_date)
                        self.web.select_by_value(locator=ccmodal.PROPAY_EXP_MONTH_SELECT, value=month)
                        self.web.select_by_value(locator=ccmodal.PROPAY_EXP_YEAR_SELECT, value=year)
                    if cvv is not None:
                        self.web.input_text(locator=ccmodal.PROPAY_CVV, text=cvv)
                    if postal_code is not None:
                        self.web.input_text(locator=ccmodal.PROPAY_POSTAL_CODE, text=postal_code)
                    self.__perform_action_on_propay_form(action=action)
                    break
                self.web.switch_to_default_content()

            self.web.switch_to_default_content()
            self.web.select_frame(locator=POS_RESTAURANT_FRAME)
            self.__perform_action_on_cc_modal(action=action)

        except Exception as e:
            raise e
        finally:
            self.web.switch_to_default_content()

    def __perform_action_on_propay_form(self, action: str):
        action = action.upper()
        if action == 'NO_ACTION':
            return
        elif action == 'CANCEL':
            self.web.click(locator=ccmodal.PROPAY_CANCEL)
        elif action == 'SUBMIT':
            self.web.capture_page_screenshot()
            self.web.click(locator=ccmodal.PROPAY_SUBMIT)

        self.web.switch_to_default_content()
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        self.web.wait_until_not_visible(locator=ccmodal.MODAL)
        self.web.select_frame(locator=ccmodal.PROPAY_IFRAME)

    def __perform_action_on_non_propay_form(self, action: str):
        action = action.upper()
        if action == 'NO_ACTION':
            pass
        elif action == 'CANCEL':
            self.web.click(locator=ccmodal.NON_PROPAY_CANCEL)
            self.web.wait_until_not_visible(locator=ccmodal.MODAL)
        elif action == 'SUBMIT':
            self.web.capture_page_screenshot()
            self.web.click(locator=ccmodal.NON_PROPAY_DONE)
            self.web.wait_until_not_visible(locator=ccmodal.MODAL)
        elif action == 'CLEAR':
            self.web.click(locator=ccmodal.NON_PROPAY_CLEAR)

    def __perfom_action_on_existing_card_modal(self, action: str):
        action = action.upper()
        if action == 'NO_ACTION':
            pass
        elif action == "CANCEL":
            self.web.click(locator=ccmodal.EXISTING_CLOSE)
            self.web.wait_until_not_visible(locator=ccmodal.MODAL)
        elif action == "SUBMIT":
            self.web.click(locator=ccmodal.EXISTING_DONE)
            self.web.wait_until_not_visible(locator=ccmodal.MODAL)
        elif action == "UPDATE":
            self.web.click(locator=ccmodal.EXISTING_UPDATE_CARD_BTN)
            self.web.wait_until_visible(locator=ccmodal.MODAL)

    def __perform_action_on_cc_modal(self, action: str):
        action = action.upper()
        if action == 'NO_ACTION':
            pass
        elif action == 'PAY_CASH_INSTEAD':
            self.web.click(locator=ccmodal.PAY_CASH_INSTEAD_BTN)
            self.web.wait_until_not_visible(locator=ccmodal.MODAL)
        elif action == 'ADD_ON_PAY_CASH':
            self.web.click(locator=ccmodal.ADD_ON_PAY_CASH_BTN)
            self.web.wait_until_visible(locator=ccmodal.MODAL)
        elif action == 'ADD_ON_PAY_CREDIT_CARD':
            self.web.click(locator=ccmodal.ADD_ON_PAY_CREDIT_CARD)
            self.web.wait_until_visible(locator=ccmodal.MODAL)

    @keyword(tags=("CreditCardModal", "ModalKeywords"))
    def get_credit_card_modal_details(self, include_hints: bool = False, include_visible_fields: bool = False,
                                      _: CreditCardModalDetails = None) -> CreditCardModalDetails:
        """Get the details displayed in the credit card modal and return it as an object of `CreditCardModalDetails`.

        - ``include_hints``: If ``True``, will include the repeat messages & error messages visible in the form. Default is ``False``.
        - ``include_visible_fields``: If ``True``, will include the visible field in the form(CARD NUMBER, EXPIRATION DATE, CVV, ZIP). Default is ``False``.
        """
        card_number = None
        expi_date = None
        cvv = None
        postal_code = None
        propay_err_msg = None
        propay_cc_num_err_msg = None
        propay_cvv_err_msg = None
        non_pp_cc_num_err_msg = None
        non_pp_expi_date_err_msg = None
        non_pp_cvv_err_msg = None
        non_pp_zip_err_msg = None
        non_pp_repeat_expi = None
        non_pp_repeat_cvv = None
        non_pp_repeat_zip = None
        visible_fields = []
        existing_card_number = None

        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(locator=ccmodal.MODAL)
            cc_charge = self.web.get_value(locator=ccmodal.CC_CHARGE_FLD)
            cash_charge = self.web.get_value(locator=ccmodal.CASH_CHARGE_FLD)
            tip = self.web.get_value(locator=ccmodal.TIP_CHARGE_FLD)
            modal_info = self.web.get_text(locator=ccmodal.CONFIRM_INFO_BOX, normalize=True)

            self.web.switch_to_default_content()
            for i in range(15):
                self.web.select_frame(locator=POS_RESTAURANT_FRAME)
                if self.web.is_visible(locator=ccmodal.NON_PROPAY_CC_NUMBER,
                                        timeout=timedelta(seconds=0.2)):
                    card_number = self.web.get_value(locator=ccmodal.NON_PROPAY_CC_NUMBER)
                    expi_date = self.web.get_value(locator=ccmodal.NON_PROPAY_EXPI_DATE).replace(" ",
                                                                                                                  "")
                    cvv = self.web.get_value(locator=ccmodal.NON_PROPAY_CVC)
                    postal_code = self.web.get_value(locator=ccmodal.NON_PROPAY_ZIP)

                    if include_hints:
                        non_pp_cc_num_err_msg, non_pp_expi_date_err_msg, non_pp_cvv_err_msg, non_pp_zip_err_msg, non_pp_repeat_expi, non_pp_repeat_cvv, non_pp_repeat_zip = self.__get_non_propay_form_input_hints()

                    if include_visible_fields:
                        visible_fields = self.__get_non_propay_form_visible_fields()
                    break

                if self.web.is_visible(locator=ccmodal.EXISTING_CARD_NUMBER,
                                        timeout=timedelta(seconds=0.2)):
                    existing_card_number = self.web.get_text(locator=ccmodal.EXISTING_CARD_NUMBER)

                self.web.select_frame(locator=ccmodal.PROPAY_IFRAME)
                if self.web.is_visible(locator=ccmodal.PROPAY_CARD_NUMBER,
                                        timeout=timedelta(seconds=0.2)):
                    self.web.switch_to_default_content()
                    self.web.select_frame(locator=POS_RESTAURANT_FRAME)
                    self.web.select_frame(locator=ccmodal.PROPAY_IFRAME)
                    card_number = self.web.get_value(locator=ccmodal.PROPAY_CARD_NUMBER)
                    expi_month = self.web.get_first_selected_option(
                        locator=ccmodal.PROPAY_EXP_MONTH_SELECT)
                    if len(expi_month) == 1:
                        expi_month = f"0{expi_month}"

                    expi_year = self.web.get_first_selected_option(
                        locator=ccmodal.PROPAY_EXP_YEAR_SELECT)
                    expi_year = expi_year[-2:]
                    expi_date = f"{expi_month}/{expi_year}"

                    cvv = self.web.get_value(locator=ccmodal.PROPAY_CVV)
                    postal_code = self.web.get_value(locator=ccmodal.PROPAY_POSTAL_CODE)

                    # error messages
                    if include_hints:
                        propay_err_msg, propay_cc_num_err_msg, propay_cvv_err_msg = self.__get_propay_form_input_hints()

                    if include_visible_fields:
                        visible_fields = self.__get_propay_form_visible_fields()

                    break

            details = CreditCardModalDetails(modal_info=modal_info,
                                             cc_charge=cc_charge,
                                             cash_charge=cash_charge,
                                             tip=tip,
                                             card_number=card_number,
                                             expi_date=expi_date,
                                             cvv=cvv,
                                             postal_code=postal_code,
                                             propay_err_msg=propay_err_msg,
                                             propay_cc_num_err_msg=propay_cc_num_err_msg,
                                             propay_cvv_err_msg=propay_cvv_err_msg,
                                             non_propay_repeat_zip=non_pp_repeat_zip,
                                             non_propay_repeat_cvv=non_pp_repeat_cvv,
                                             non_propay_repeat_expi=non_pp_repeat_expi,
                                             non_propay_cc_num_err_msg=non_pp_cc_num_err_msg,
                                             non_propay_expi_date_err_msg=non_pp_expi_date_err_msg,
                                             non_propay_cvv_err_msg=non_pp_cvv_err_msg,
                                             non_propay_postal_code_err_msg=non_pp_zip_err_msg,
                                             visible_fields=visible_fields,
                                             existing_card_number=existing_card_number)
        except Exception as e:
            raise e
        finally:
            self.web.switch_to_default_content()
        self.logger.debug(details)
        return details

    def __get_propay_form_input_hints(self):
        propay_err_msg = None
        propay_cc_num_err_msg = None
        propay_cvv_err_msg = None

        if self.web.is_visible(locator=ccmodal.PROPAY_VALIDATION_MSG,
                                timeout=timedelta(seconds=0.2)):
            propay_err_msg = self.web.get_text(
                locator=ccmodal.PROPAY_VALIDATION_MSG)
        if self.web.is_visible(locator=ccmodal.PROPAY_CARD_NUMBER_VALIDATION_MSG,
                                timeout=timedelta(seconds=0.2)):
            propay_cc_num_err_msg = self.web.get_text(
                locator=ccmodal.PROPAY_CARD_NUMBER_VALIDATION_MSG)
        if self.web.is_visible(locator=ccmodal.PROPAY_CVV_VALIDATION_MSG,
                                timeout=timedelta(seconds=0.2)):
            propay_cvv_err_msg = self.web.get_text(
                locator=ccmodal.PROPAY_CVV_VALIDATION_MSG)
        return propay_err_msg, propay_cc_num_err_msg, propay_cvv_err_msg

    def __get_non_propay_form_input_hints(self):
        non_pp_cc_num_err_msg = None
        non_pp_expi_date_err_msg = None
        non_pp_cvv_err_msg = None
        non_pp_zip_err_msg = None
        non_pp_repeat_expi = None
        non_pp_repeat_cvv = None
        non_pp_repeat_zip = None

        if self.web.is_visible(locator=ccmodal.NON_PROPARY_CC_NUM_ERR_MSG,
                                timeout=timedelta(seconds=0.2)):
            non_pp_cc_num_err_msg = self.web.get_text(
                locator=ccmodal.NON_PROPARY_CC_NUM_ERR_MSG)

        if self.web.is_visible(locator=ccmodal.NON_PROPAY_EXPI_DATE_ERR_MSG,
                                timeout=timedelta(seconds=0.2)):
            non_pp_expi_date_err_msg = self.web.get_text(
                locator=ccmodal.NON_PROPAY_EXPI_DATE_ERR_MSG)

        if self.web.is_visible(locator=ccmodal.NON_PROPAY_CVV_ERR_MSG,
                                timeout=timedelta(seconds=0.2)):
            non_pp_cvv_err_msg = self.web.get_text(locator=ccmodal.NON_PROPAY_CVV_ERR_MSG)

        if self.web.is_visible(locator=ccmodal.NON_PROPAY_ZIP_ERR_MSG,
                                timeout=timedelta(seconds=0.2)):
            non_pp_zip_err_msg = self.web.get_text(locator=ccmodal.NON_PROPAY_ZIP_ERR_MSG)

        if self.web.is_visible(locator=ccmodal.NON_PROPAY_REPEAT_EXPI,
                                timeout=timedelta(seconds=0.2)):
            non_pp_repeat_expi = self.web.get_text(locator=ccmodal.NON_PROPAY_REPEAT_EXPI)

        if self.web.is_visible(locator=ccmodal.NON_PROPAY_REPEAT_CVV,
                                timeout=timedelta(seconds=0.2)):
            non_pp_repeat_cvv = self.web.get_text(locator=ccmodal.NON_PROPAY_REPEAT_CVV)

        if self.web.is_visible(locator=ccmodal.NON_PROPAY_REPEAT_ZIP,
                                timeout=timedelta(seconds=0.2)):
            non_pp_repeat_zip = self.web.get_text(locator=ccmodal.NON_PROPAY_REPEAT_ZIP)

        return non_pp_cc_num_err_msg, non_pp_expi_date_err_msg, non_pp_cvv_err_msg, non_pp_zip_err_msg, non_pp_repeat_expi, non_pp_repeat_cvv, non_pp_repeat_zip

    def __get_propay_form_visible_fields(self):
        visible_fields = []
        if self.web.is_visible(locator=ccmodal.PROPAY_CARD_NUMBER, timeout=timedelta(seconds=0.2)):
            visible_fields.append(CCFieldNames.CC_NUM.value)

        if self.web.is_visible(locator=ccmodal.PROPAY_EXP_YEAR_SELECT,
                                timeout=timedelta(seconds=0.2)) \
                and self.web.is_visible(locator=ccmodal.PROPAY_EXP_MONTH_SELECT,
                                         timeout=timedelta(seconds=0.2)):
            visible_fields.append(CCFieldNames.EXPI_DATE.value)

        if self.web.is_visible(locator=ccmodal.PROPAY_CVV, timeout=timedelta(seconds=0.2)):
            visible_fields.append(CCFieldNames.CVV.value)

        if self.web.is_visible(locator=ccmodal.PROPAY_POSTAL_CODE, timeout=timedelta(seconds=0.2)):
            visible_fields.append(CCFieldNames.ZIP.value)

        return visible_fields

    def __get_non_propay_form_visible_fields(self):
        visible_fields = []
        if self.web.is_visible(locator=ccmodal.NON_PROPAY_CC_NUMBER, timeout=timedelta(seconds=0.2)):
            visible_fields.append(CCFieldNames.CC_NUM.value)

        if self.web.is_visible(locator=ccmodal.NON_PROPAY_EXPI_DATE,
                                timeout=timedelta(seconds=0.2)):
            visible_fields.append(CCFieldNames.EXPI_DATE.value)

        if self.web.is_visible(locator=ccmodal.NON_PROPAY_CVC, timeout=timedelta(seconds=0.2)):
            visible_fields.append(CCFieldNames.CVV.value)

        if self.web.is_visible(locator=ccmodal.NON_PROPAY_ZIP, timeout=timedelta(seconds=0.2)):
            visible_fields.append(CCFieldNames.ZIP.value)

        return visible_fields

    @keyword(tags=("CreditCardModal", "ModalKeywords"))
    def credit_card_modal_should_not_be_visible(self):
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            is_visible = self.web.is_visible(locator=ccmodal.CC_CHARGE_FLD, timeout=timedelta(seconds=3))
            if self.web.attribute_contains(locator=restaurantlanding.CREDIT_CARD_BTN, attribute="class", exp_value="selected"):
                is_visible = self.web.is_visible(locator=ccmodal.CC_CHARGE_FLD, timeout=timedelta(seconds=5))
            self.asserts.assert_false(is_visible, desc="Credit Card Modal Should Not Be Visible.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()