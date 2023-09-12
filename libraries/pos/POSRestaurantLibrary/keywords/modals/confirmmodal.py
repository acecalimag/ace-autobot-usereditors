from datetime import timedelta
from robot.api.deco import keyword

from libraries.pos.POSRestaurantLibrary.dto.confirmmodaldetails import ConfirmModalDetails
from libraries.pos.POSRestaurantLibrary.locators.frame import POS_RESTAURANT_FRAME
from libraries.pos.POSRestaurantLibrary.locators.modals import confirmmodal
from autocore.bases import WebLibraryComponent
from autocore.web.webactions import sleep


def _get_button_locator(button_name: str):
    button_name = button_name.upper().strip()
    if button_name == 'HANGUP':
        return confirmmodal.HANGUP_BTN
    elif button_name == 'MODIFY':
        return confirmmodal.MODIFY_BTN
    elif button_name == 'CONTINUE':
        return confirmmodal.CONTINUE_BTN
    elif button_name == 'CANCEL':
        return confirmmodal.CANCEL_BTN
    else:
        raise Exception(f"No locator found for button {button_name}")


class ConfirmModalKeywords(WebLibraryComponent):


    @keyword(tags=("ConfirmModal", "ModalKeywords"))
    def take_action_on_confirm_modal(self, input_text: str = None, button: str = 'NO_ACTION',
                                     check_visibility: bool = False,
                                     _: ConfirmModalDetails = None) -> ConfirmModalDetails | None:
        """Take action on the confirm modal. Returns the details of the Confirm Modal as `ConfirmModalDetails` object.

        - ``button``: name of the button to click, default is ``NO_ACTION``, no button will be clicked.
        Below are the accepted values:
        -- ``HANGUP``: will click the ``HANGUP`` button.
        -- ``MODIFY``: will click the ``MODIFY`` button.
        -- ``CONTINUE``: will click the ``CONTINUE`` button.
        -- ``CANCEL``: will click the ``CANCEL`` button.

        - ``input_text``: the to be typed on the text field of the modal if visible.
        Possible usage is on the Confirm Modal when going back to homepage.
        - ``check_visibility``: If ``True``, will check if the modal is visible before taking an action. If not visible, no action will be performed and keyword won't fail.
        If ``False`` (Default), will wait until modal is visible, if not visible, keyword will fail.
        """

        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            if check_visibility and not self.web.is_visible(locator=confirmmodal.TITLE,
                                                             timeout=timedelta(seconds=1)):
                return
            else:
                self.web.wait_until_visible(locator=confirmmodal.TITLE)

            if input_text is not None:
                self.web.wait_until_visible(locator=confirmmodal.BODY_INPUT_FLD,
                                             timeout=timedelta(seconds=0.2))
                self.web.delete_text_via_keys(locator=confirmmodal.BODY_INPUT_FLD)
                sleep(seconds=0.2)
                self.web.input_text(locator=confirmmodal.BODY_INPUT_FLD, text=input_text, clear=False)
                try_count = 5
                while not self.web.is_enabled(locator=confirmmodal.CONTINUE_BTN,
                                               timeout=timedelta(seconds=2)):
                    if try_count == 0:
                        break
                    self.web.delete_text_via_keys(locator=confirmmodal.BODY_INPUT_FLD)
                    sleep(seconds=2)
                    self.web.input_text(locator=confirmmodal.BODY_INPUT_FLD, text=input_text, clear=False)
                    try_count -= 1

            details = self.__get_confirm_modal_details()

            if button == 'NO_ACTION':
                pass
            else:
                button = _get_button_locator(button_name=button)
                self.web.wait_until_visible(locator=button)
                self.web.click(locator=button)

        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
        self.logger.debug(details)
        return details

    def __get_confirm_modal_details(self) -> ConfirmModalDetails:
        self.web.wait_until_visible(locator=confirmmodal.TITLE)
        title = self.web.get_text(locator=confirmmodal.TITLE, normalize=True)
        message = self.web.get_text(locator=confirmmodal.BODY, normalize=True)
        order_number = None

        if 'Order Complete:' in message and 'version' in message:
            s_text = message.split(':')[1].strip()
            order_number = s_text.split('version')[0].strip()
        elif message.strip().startswith('Separate Orders Completed:'):
            order_number = message.split(':')[1].strip()
            order_number = order_number.split('[')[0].strip()
        elif message.strip().startswith('Order Completed:'):
            order_number = message.split(':')[1].strip()
        return ConfirmModalDetails(
            title=title,
            message=message,
            order_number=order_number
        )
