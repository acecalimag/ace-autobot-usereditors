from datetime import timedelta
from libraries.userconfig.UserConfigLibrary.locators import landingpage
from autocore.bases import WebLibraryComponent
from robot.api.deco import keyword


class LandingPageKeywords(WebLibraryComponent):

    @keyword(tags=("UserConfigKeywords", "LandingPageKeywords"))
    def open_status_dropdown(self,):
        self.__open_dropdown(locator=landingpage.STATUS_DROPDOWN)    

    def __open_dropdown(self, locator):
        self.web.wait_until_visible(locator=locator, timeout=timedelta(seconds=2))
        self.web.click(locator=locator)


    