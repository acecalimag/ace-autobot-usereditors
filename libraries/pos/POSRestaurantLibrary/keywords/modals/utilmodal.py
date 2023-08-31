from datetime import timedelta
from robot.api.deco import keyword

from libraries.pos.POSRestaurantLibrary.dto.utilmodaldetails import UtilModalDetails
from libraries.pos.POSRestaurantLibrary.locators.frame import POS_RESTAURANT_FRAME
from libraries.pos.POSRestaurantLibrary.locators.modals import utilmodal
from autocore.bases import WebLibraryComponent


class UtilModalKeywords(WebLibraryComponent):

    @keyword(tags=("ModalKeywords", "UtilModalKeywords"))
    def take_action_on_util_modal(self, action: str = 'NO_ACTION', check_visibility: bool = False,
                                  _: UtilModalDetails = None) -> UtilModalDetails | None:
        """Takes action on the displayed util modal and return the details as an object of `UtilModalDetails`.
        - ``ACTION``: The action to be performed. Following are the accepted values:
        -- ``NO_ACTION``: Default. No action will be performed.
        -- ``YES``: Will click the ``Yes`` button.
        -- ``NO``: Will click the ``No`` button.
        -- ``CONTINUE``: Will click the ``Continue`` button.
        -- ``CANCEL``: Will click the ``Cancel`` button.

        - ``check_visibility``: If ``True``, will check if the modal is visible before taking an action. If not visible, no action will be performed and keyword won't fail.
        If ``False`` (Default), will wait until modal is visible, if not visible, keyword will fail.
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            if check_visibility and not self.web.is_visible(locator=utilmodal.HEADER,
                                                             timeout=timedelta(seconds=1)):
                return
            else:
                self.web.wait_until_visible(locator=utilmodal.HEADER)

            title = self.web.get_text(locator=utilmodal.HEADER, normalize=True)
            body = self.web.get_text(locator=utilmodal.BODY, normalize=True)

            details = UtilModalDetails(body=body, title=title)
            self.__perform_action(action=action)
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
        self.logger.debug(details)
        return details

    def __perform_action(self, action: str):
        if action is not None:
            action = action.upper()
            if action == 'NO_ACTION':
                return
            elif action == 'YES':
                return self.web.click(locator=utilmodal.YES_BTN)
            elif action == 'NO':
                return self.web.click(locator=utilmodal.NO_BTN)
            elif action == 'CONTINUE':
                return self.web.click(locator=utilmodal.CONTINUE_BTN)
            elif action == 'CANCEL':
                return self.web.click(locator=utilmodal.CANCEL_BTN)

        raise Exception(f"Invalid action provided: {action}")
