from datetime import timedelta
from robot.api.deco import keyword

from libraries.pos.POSRestaurantLibrary.locators.frame import POS_RESTAURANT_FRAME
from libraries.pos.POSRestaurantLibrary.locators.modals import datanotify
from autocore.bases import WebLibraryBase, WebLibraryComponent


class DataNotifyAlertKeywords(WebLibraryComponent):
    
    def __init__(self, library: WebLibraryBase, timeout: timedelta = ...):
        super().__init__(library, timeout)
        self.__FIRST_TIME_CUSTOMER: str = "First Time Customer, Ask Customer For Their Address."
        self.__ORDER_WITHIN_FOUR_HRS: str = "This customer has placed an order within 4 hours!"
        self.__ORDER_ALREADY_SENT: str = "The order is already sent! Please modify the order!"
        self.__MANAGER_USE_ONLY: str = "Manager Use Only"
        self.__WITH_PREVIOUS_CC_PAYMENT: str = 'This order previously had a credit card payment.Please ask customer,"Would you like to pay cash for the difference?"'
        self.__CC_MINIUM_MSG: str = "Order doesn\u2019t meet the Credit Card minimum."


    @keyword(tags=("AlertKeywords", "RestaurantKeywords"))
    def close_all_data_notify_alerts(self):
        """Close data notify alerts with close button.

        Pre-requisite: To use this keyword make sure that a restaurant is open.
        See `Open Restaurant In POS Homepage`.
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.close_data_notify_alerts_helper()
        except Exception as e:
            self.logger.warn(f"There was an exception when attempting to close data notify alerts. {str(e)}")
        finally:
            self.web.unselect_frame()
            
            
    def close_data_notify_alerts_helper(self):
        closeable_msgs: list = [
            self.__FIRST_TIME_CUSTOMER,
            self.__ORDER_WITHIN_FOUR_HRS,
            self.__ORDER_ALREADY_SENT,
            self.__MANAGER_USE_ONLY,
            self.__WITH_PREVIOUS_CC_PAYMENT
        ]

        for msg in closeable_msgs:
            try_count = 5
            while self.web.count(locator=datanotify.MESSAGE_TPL(msg=msg)) >= 0:
                if try_count == 0:
                    break
                try:
                    if self.web.is_visible(locator=datanotify.MESSAGE_TPL(msg=msg),
                                            timeout=timedelta(seconds=0.1)):
                        self.web.wait_until_visible(locator=datanotify.CLOSE_BTN_OF_TPL(msg=msg),
                                                    timeout=timedelta(seconds=0.2))
                        self.web.click(locator=datanotify.CLOSE_BTN_OF_TPL(msg=msg))
                except Exception as e:
                    self.logger.warn(f"There was an exception when attempting to close data notify alerts. {str(e)}")
                try_count -= 1


    @keyword(tags=("AlertKeywords", "RestaurantKeywords"))
    def take_action_on_credit_card_minimum_data_notify_alert(self, minimum_amt: str = None, close: bool = True):
        

        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(locator=datanotify.CC_MINIMUM)
            act_msg = self.web.get_text(locator=datanotify.CC_MINIMUM)
            self.logger.info(f"CC Minium message: {act_msg}")
            if minimum_amt is not None:
                exp_msg = f"{self.__CC_MINIUM_MSG} (${minimum_amt})"
                self.asserts.assert_equal(actual=act_msg, exp=exp_msg, desc="CC minimum alert.")
            
            if close:
                self.web.click(locator=datanotify.CC_MINIMUM_CLOSE_BTN)
                self.web.wait_until_not_visible(locator=datanotify.CC_MINIMUM)
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

