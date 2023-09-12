from robot.api.deco import keyword
from libraries.pos.POSRestaurantLibrary.dto.voidordermodal import VoidOrderModalDetails
from libraries.pos.POSRestaurantLibrary.locators.frame import POS_RESTAURANT_FRAME
from libraries.pos.POSRestaurantLibrary.locators.modals import voidordermodal
from autocore.bases import WebLibraryComponent
from autocore.web.webactions import sleep


class VoidOrderModalKeywords(WebLibraryComponent):

    @keyword(tags=("VoidOrderModalKeywords", "ModalKeywords"))
    def take_action_on_void_order_modal(self, option: str = 'Void by owner', action: str = 'VOID',
                                        _: VoidOrderModalDetails = None) -> VoidOrderModalDetails:
        """Takes action on the void order modal and return the details as an object of `VoidOrderModalDetails`.

        - ``option``: the remark reason to be selected
        - ``action``: the action to perform on the modal. Accepted values:
        -- ``VOID``: will click the void button
        -- ``CANCEL``: will click the cancel button
        -- ``NO_ACTION``: no action will be performed.
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(locator=voidordermodal.MODAL_TITLE)
            title = self.web.get_text(locator=voidordermodal.MODAL_TITLE, normalize=True)
            order_number = self.web.get_text(locator=voidordermodal.ORDER_NUMBER)
            if 'Order' in order_number:
                order_number = order_number.replace("Order", "").replace(" ", "")
            phone = self.web.get_text(locator=voidordermodal.CUST_PHONE)
            if "(NW)" in phone:
                phone = phone.replace("(NW)", "").strip()
            time = self.web.get_text(locator=voidordermodal.TIME)

            if option is not None:
                try_count = 5
                while self.web.get_value(locator=voidordermodal.SELECTED_COMMENT,
                                          normalize=True).lower().replace(" ", "") != option.lower().strip().replace(
                        " ", ""):
                    if try_count == 0:
                        break
                    self.web.click(locator=voidordermodal.OPTION_WITH_LABEL(option))
                    sleep(seconds=0.2)
                    try_count -= 1

            selected_option = self.web.get_value(locator=voidordermodal.SELECTED_COMMENT, normalize=True)
            available_options = self.web.get_texts(locator=voidordermodal.OPTION_LABELS, normalize=True)

            details = VoidOrderModalDetails(
                title=title, order_number=order_number, time=time, selected_option=selected_option,
                available_options=available_options, cust_phone=phone
            )

            action = action.upper()
            if action == 'NO_ACTION':
                pass
            elif action == 'VOID':
                self.web.click(locator=voidordermodal.VOID_BTN)
                self.web.wait_until_not_visible(locator=voidordermodal.VOID_BTN)
            elif action == 'CANCEL':
                self.web.click(locator=voidordermodal.CANCEL_BTN)
                self.web.wait_until_not_visible(locator=voidordermodal.VOID_BTN)
            else:
                raise Exception(f"The provided action {action} is not supported.")

        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
        self.logger.debug(details)
        return details


