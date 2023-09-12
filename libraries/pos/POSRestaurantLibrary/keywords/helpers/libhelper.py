from robot.api.deco import keyword
from libraries.pos.POSRestaurantLibrary.dto.ccmodaldetails import CreditCardModalDetails


class LibraryHelperKeywords:
    
    def __init__(self, library):
        from libraries.pos.POSRestaurantLibrary import POSRestaurantLibrary
        self.__lib: POSRestaurantLibrary = library
        
    @keyword(tags=("NavigationKeywords","Tasks")) 
    def navigate_from_restaurant_to_homepage(self):
        """This will navigate you from the restaurant view to the homepage.
        """
        self.__lib.click_home_button()
        self.__lib.take_action_on_confirm_modal(input_text='HOME', button='CONTINUE')
        self.__lib.wait_until_restaurants_are_visible_in_pos_homepage()
        
    @keyword(tags=("RestaurantKeywords","Tasks")) 
    def send_order(self) -> str:
        """This will send the order and go to more display view. Returns the order number.
        For split orders, only the main order number will be returned.
        """
        self.__lib.click_send_button()
        self.__lib.take_action_on_util_modal(
            action='CONTINUE', check_visibility=True)
        modal_details = self.__lib.take_action_on_confirm_modal(
            button='MODIFY')
        return modal_details['order_number']

    @keyword(tags=("RestaurantKeywords","Tasks")) 
    def rush_order(self, oid: str, rush_reason: str = 'Order takes too long, please hurry up.'):
        """This will rush the order and wait until homepage is displayed.
        """
        self.__lib.view_details_of_order(oid=oid)
        self.__lib.click_rush_button_on_more_display_view()
        self.__lib.take_action_on_util_modal(action='YES', check_visibility=True)
        self.__lib.take_action_on_rush_order_modal(
            action='RUSH', option=rush_reason)
        self.__lib.take_action_on_info_modal(button='OK')
        self.__lib.wait_until_restaurants_are_visible_in_pos_homepage()

    @keyword(tags=("RestaurantKeywords","Tasks")) 
    def void_order(self, oid: str, void_reason: str = 'Customer has no money.'):
        """This will void the order."""
        self.__lib.view_details_of_order(oid=oid)
        self.__lib.click_void_button_on_more_display_view()
        self.__lib.take_action_on_confirm_modal(
            button='CONTINUE', check_visibility=True)
        self.__lib.take_action_on_void_order_modal(
            option=void_reason)
        self.__lib.take_action_on_info_modal(button='OK')
        
    @keyword(tags=("RestaurantKeywords","Tasks","Cleanup"))
    def force_void_order(self, phone_number: str, header: str):
        try_count = 2
        while try_count > 0:
            try:
                details = self.__lib.view_details_of_order(phone_number=phone_number, header=header)
                if self.__lib.is_sent_order(oid=details['oid']):
                    self.__lib.logger.info(f"Order {details['oid']} is a sent order. Trying to void.")
                    self.void_order(oid=details['oid'])
                    # This is intentional that we are not breaking the loop even if the order is not a sent orders 
                else:
                    self.__lib.logger.info(f"Order {details['oid']} is not a sent order.")
            except Exception:
                pass
            try_count -= 1
        
    @keyword(tags=("RestaurantKeywords","Tasks")) 
    def save_order(self, save_reason: str = 'Fax'):
        """Save the order and will go to more display view."""
        self.__lib.click_save_order_button()
        self.__lib.select_save_reason(option=save_reason)
        self.__lib.take_action_on_info_modal(button='MODIFY')

    @keyword(tags=("RestaurantKeywords","Tasks")) 
    def provide_credit_card_modal_details(self, cc_charge: str = None, cash_charge: str = None,
                                          tip: str = None, card_number: str = None, expi_date: str = None,
                                          cvv: str = None, postal_code: str = None, get_details_before: bool = False,
                                          get_details_after: bool = False, action: str = 'SUBMIT',
                                          _: CreditCardModalDetails = None) -> CreditCardModalDetails | None:
        """Fillout credit card details.
        - `get_details_before`: if ``True``, credit card modal details before filling out the form will be returned as `CreditCardModalDetails`.
        - `get_details_after`: if ``False``, credit card modal details after filling out the frome will be returned as `CreditCardModalDetails`.
        For acception ``action`` values, see `Fillout Credit Card Modal`.
        """
        self.__lib.click_credit_card_button()
        
        self.__lib.fillout_credit_card_modal(action='NO_ACTION') #This will only wait for the cc modal to be displayed
        
        self.__lib.take_action_on_confirm_modal(
            button='CONTINUE', check_visibility=True)

        details = None
        if get_details_before:
            details = self.__lib.get_credit_card_modal_details()

        if get_details_after:
            self.__lib.fillout_credit_card_modal(credit_card_charge=cc_charge, cash_charge=cash_charge, tip=tip, card_number=card_number,
                                                               expi_date=expi_date, cvv=cvv, postal_code=postal_code, action='NO_ACTION')
            details = self.__lib.get_credit_card_modal_details()
            self.__lib.fillout_credit_card_modal(action=action)
        else:
            self.__lib.fillout_credit_card_modal(credit_card_charge=cc_charge, cash_charge=cash_charge, tip=tip, card_number=card_number,
                                                               expi_date=expi_date, cvv=cvv, postal_code=postal_code, action=action)

        return details
