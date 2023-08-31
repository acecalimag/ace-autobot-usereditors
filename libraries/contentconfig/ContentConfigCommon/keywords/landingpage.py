
from robot.api.deco import keyword
from autocore.bases import WebLibraryComponent
from libraries.contentconfig.ContentConfigCommon.dto.navbardetails import NavbarDetails
from libraries.contentconfig.ContentConfigCommon.locators import landingpage


class LandingPageKeywords(WebLibraryComponent):

    @keyword(tags=("LandingPageKeywords","ContentConfigCommonKeywords"))
    def open_printer_editor(self):
        self.__open_editor_located_by(locator=landingpage.PRINTER_EDITOR_OPTION)

    @keyword(tags=("LandingPageKeywords","ContentConfigCommonKeywords"))
    def open_propay_account_editor(self):
        self.__open_editor_located_by(locator=landingpage.PROPAY_ACCOUNT_EDITOR_OPTION)
        
    @keyword(tags=("LandingPageKeywords","ContentConfigCommonKeywords"))
    def open_credit_card_not_editor(self):
        self.__open_editor_located_by(locator=landingpage.CREDIT_CARD_NOTE_EDITOR_OPTION)
        
    @keyword(tags=("LandingPageKeywords","ContentConfigCommonKeywords"))
    def open_wonderspay_terminal_editor(self):
        self.__open_editor_located_by(locator=landingpage.WONDERSPAY_TERMINAL_EDITOR_OPTION)

    def __open_editor_located_by(self, locator: str):
        self.web.wait_until_visible(locator=landingpage.WONDERS_LOGO)
        self.web.wait_until_visible(
            locator=landingpage.NAVBAR_OPTION_EDITORS_DROPDOWN)
        self.web.click(
            locator=landingpage.NAVBAR_OPTION_EDITORS_DROPDOWN)
        self.web.scroll_into_view(locator=locator)
        self.web.click(locator=locator)

    @keyword(tags=("LandingPageKeywords","ContentConfigCommonKeywords"))
    def get_navbar_details(self, _:NavbarDetails = None) -> NavbarDetails:
        self.web.wait_until_visible(locator=landingpage.WONDERS_LOGO)
        self.web.wait_until_visible(
            locator=landingpage.NAVBAR_OPTION_EDITORS_DROPDOWN)
        menu_items = [i for i in self.web.get_texts(locator=landingpage.NAVBAR_MENU_LABLES, normalize=True)]
        self.web.click(locator=landingpage.NAVBAR_OPTION_EDITORS_DROPDOWN)
        editors = [i for i in self.web.get_texts(landingpage.NAVBAR_DROPDOWN_OPTIONS, normalize=True) if len(i) > 0]
        self.web.click(locator=landingpage.NAVBAR_OPTION_EDITORS_DROPDOWN)
        details = NavbarDetails(
            username=self.web.get_text(locator=landingpage.USERNAME),
            position=self.web.get_text(locator=landingpage.POSITION),
            menu_items=menu_items,
            editor_dropdown_options=editors
        )
        self.logger.debug(details)
        return details