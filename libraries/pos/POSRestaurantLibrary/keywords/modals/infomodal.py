from robot.api.deco import keyword

from libraries.pos.POSRestaurantLibrary.dto.infomodaldetails import InfoModalDetails
from libraries.pos.POSRestaurantLibrary.locators.frame import POS_RESTAURANT_FRAME
from libraries.pos.POSRestaurantLibrary.locators.modals import infomodal
from autocore.bases import WebLibraryComponent


def _get_button_locator(button_name: str):
    if button_name.upper() == 'OK':
        return infomodal.OK_BTN
    elif button_name.upper() == 'MODIFY':
        return infomodal.MODIFY_BTN
    else:
        raise Exception(f"No locator found for button {button_name}")


class InfoModalKeywords(WebLibraryComponent):

    @keyword(tags=("InfoModalKeywords", "ModalKeywords"))
    def take_action_on_info_modal(self, button: str = 'NO_ACTION', _: InfoModalDetails = None) -> InfoModalDetails:
        """Take action on the info modal. Returns the details of the Info Modal as `InfoModalDetails` object.

        - ``button``: name of the button to click, default is ``NO_ACTION``, no button will be clicked.
        Below are the accepted values:
        -- ``OK``: will click the ``OK`` button.
        -- ``MODIFY``: will click the ``MODIFY`` button.
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(locator=infomodal.HEADER)
            details = InfoModalDetails(
                title=self.web.get_text(locator=infomodal.HEADER, normalize=True),
                message=self.web.get_text(locator=infomodal.TEXT_BODY, normalize=True)
            )

            if button.upper() == 'NO_ACTION':
                pass
            else:
                button_locator = _get_button_locator(button_name=button)
                self.web.wait_until_visible(locator=button_locator)
                self.web.click(locator=button_locator)
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
        self.logger.debug(details)
        return details
