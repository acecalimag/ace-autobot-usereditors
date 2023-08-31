from libraries.dashboard.DashboardCommon.locators import landingpage
from autocore.bases import WebLibraryComponent
from robot.api.deco import keyword


class LandingKeywords(WebLibraryComponent):
    
    @keyword
    def go_to_client_tech_dashboard(self):
        self.web.wait_until_visible(locator=landingpage.CLIENT_TECH)
        self.web.click(locator=landingpage.CLIENT_TECH)