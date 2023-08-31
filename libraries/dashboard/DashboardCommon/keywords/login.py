from robot.api.deco import keyword
from libraries.dashboard.DashboardCommon.locators import loginpage
from libraries.dashboard.config import DASHBOARD_GLOBAL_TIMEOUT
from autocore.bases import WebLibraryComponent

class LoginKeywords(WebLibraryComponent):

    @keyword(tags=("LoginKeywords",))
    def login_to_dashboard(self, username: str = None, password: str = None):
        """Login to DASHBOARD using the provided ``username`` and ``password``."""
        self.web.wait_until_visible(locator=loginpage.LOGIN_BTN)
        if username is not None:
            self.web.input_text(locator=loginpage.USERNAME_FLD, text=username)

        if password is not None:
            self.web.input_password(locator=loginpage.PASSWORD_FLD, password=password)

        self.web.click(locator=loginpage.LOGIN_BTN)
        
