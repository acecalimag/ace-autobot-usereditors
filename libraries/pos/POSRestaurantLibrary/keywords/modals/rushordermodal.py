from robot.api.deco import keyword

from libraries.pos.POSRestaurantLibrary.dto.rushordermodaldetails import RushOrderModalDetails
from libraries.pos.POSRestaurantLibrary.locators.frame import POS_RESTAURANT_FRAME
from libraries.pos.POSRestaurantLibrary.locators.modals import rushordermodal
from autocore.bases import WebLibraryComponent
from autocore.web.webactions import sleep

class RushOrderModalKeywords(WebLibraryComponent):

    @keyword(tags=("RushOrderModalKeywords", "ModalKeywords"))
    def take_action_on_rush_order_modal(self, option: str = 'Order takes too long, please hurry up.',
                                        action: str = 'RUSH',
                                        _: RushOrderModalDetails = None) -> RushOrderModalDetails:
        """Takes action on the rush order modal and return the details as an object of `RushOrderModalDetails`.

        - ``option``: the remark reason to be selected
        - ``action``: the action to perform on the modal. Accepted values:
        -- ``RUSH``: will click the rush button
        -- ``CANCEL``: will click the cancel button
        -- ``NO_ACTION``: no action will be performed.
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(locator=rushordermodal.TITLE)
            title = self.web.get_text(locator=rushordermodal.TITLE, normalize=True)
            order_number = self.web.get_text(locator=rushordermodal.ORDER_NUMBER)
            if 'Order' in order_number:
                order_number = order_number.replace("Order", "").replace(" ", "")
            phone = self.web.get_text(locator=rushordermodal.CUST_PHONE)
            if "(NW)" in phone:
                phone = phone.replace("(NW)", "").strip()
            time = self.web.get_text(locator=rushordermodal.TIME)

            available_options = [i.get('label') for i in self.__get_options_details()]

            if option is not None:
                # Select option
                for i in self.__get_options_details():
                    option = option.lower().replace(" ", "")
                    if i.get('label_lower') == option:
                        try_count = 5
                        while option.lower().replace(" ", "") != self.web.get_value(
                                locator=rushordermodal.SELECTED_COMMENT, normalize=True).lower().replace(" ",
                                                                                                                 ""):
                            if try_count == 0:
                                break
                            self.web.click(locator=i.get('label_locator'))
                            sleep(seconds=0.2)
                            try_count -= 1

            selected_option = self.web.get_value(locator=rushordermodal.SELECTED_COMMENT, normalize=True)

            details = RushOrderModalDetails(
                title=title, order_number=order_number, time=time, selected_option=selected_option,
                available_options=available_options, cust_phone=phone
            )

            if action is not None:
                action = action.upper()
                if action == 'NO_ACTION':
                    pass
                elif action == 'RUSH':
                    self.web.click(locator=rushordermodal.RUSH_BTN)
                elif action == 'CANCEL':
                    self.web.click(locator=rushordermodal.CANCEL_BTN)
                else:
                    raise Exception(f"The provided action {action} is not supported.")
            else:
                raise Exception(f"The provided action {action} is not supported.")

        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
        self.logger.debug(details)
        return details

    def __get_options_details(self):
        self.web.wait_until_count_is_greater_than(locator=rushordermodal.COMMENT_LABELS, count=2)
        options_count = self.web.count(locator=rushordermodal.COMMENT_LABELS)
        options = []
        for i in range(1, options_count + 1):
            label_locator = rushordermodal.COMMENT_LABELS_INDEXED(i)
            label = self.web.get_text(locator=label_locator, normalize=True)
            label_lower = label.lower().replace(" ", "")
            options.append({
                "label_locator": label_locator,
                "label": label,
                "label_lower": label_lower
            })
        return options
