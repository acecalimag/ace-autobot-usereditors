from robot.api.deco import keyword
from autocore.bases import WebLibraryComponent
from libraries.pos.POSCommon.locators import loginpage


class LoginKeywords(WebLibraryComponent):

    @keyword(tags=("LoginKeywords",))
    def login_to_pos(self, username: str = None, password: str = None):
        """Login to POS using the provided ``username`` and ``password``.

        Pre-requisite: To use this keyword, POS login page should be open. See `Open POS in Browser`.
        """
        self.web.wait_until_visible(locator=loginpage.LOGIN_BTN)
        if username is not None:
            self.web.input_text(locator=loginpage.USERNAME_FLD, text=username)

        if password is not None:
            self.web.input_password(locator=loginpage.PASSWORD_FLD, password=password)

        self.web.click(locator=loginpage.LOGIN_BTN)
