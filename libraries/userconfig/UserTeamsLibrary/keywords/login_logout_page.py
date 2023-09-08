
from autocore.bases import WebLibraryComponent
from libraries.userconfig.UserTeamsLibrary.locators import loginlocators
from robot.api.deco import keyword

# from SeleniumLibrary import SeleniumLibrary
# from robot.api import logger


class LoginPage(WebLibraryComponent):
    
    # def __init__(self, ctx: SeleniumLibrary) -> None:
    #     self.__ctx = ctx
    
    @keyword
    def login(self, username: str, password: str):
        self.logger.info(f"Logging in using  {username} and {password}")
        self.web.se_lib.wait_until_element_is_visible(locator=loginlocators.USERNAME_FLD)
        self.web.input_text(locator=loginlocators.USERNAME_FLD, text=username)
        self.web.input_text(locator=loginlocators.PASSWORD_FLD, text=password)
        self.web.se_lib.click_element(locator=loginlocators.LOGIN_BTN)
        
class LogoutPage(WebLibraryComponent):
    
    # def __init__(self, ctx: SeleniumLibrary) -> None:
    #     self.web = ctx

    @keyword
    def logout_to_system(self):
        self.logger.info("Logging out of the system")
        self.web.se_lib.click_element(locator=loginlocators.NAVTOLOGOUT)
        
        # Wait for the logout button to be clickable and then click it
        self.web.se_lib.wait_until_element_is_visible(locator=loginlocators.LOGOUT_BTN)
        self.web.se_lib.click_element(locator=loginlocators.LOGOUT_BTN)
        
        # Wait for the confirmation logout button to be clickable and then click it
        self.web.se_lib.wait_until_element_is_visible(locator=loginlocators.CNFRM_LOGOUT_BTN)
        self.web.se_lib.click_element(locator=loginlocators.CNFRM_LOGOUT_BTN)
        
        self.web.close_browser()