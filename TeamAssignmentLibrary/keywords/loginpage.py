
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from TeamAssignmentLibrary.locators import loginlocators
from robot.api import logger

class LoginPage:
    
    def __init__(self, ctx: SeleniumLibrary) -> None:
        self.__ctx = ctx
    
    @keyword
    def login(self, username: str, password: str):
        logger.info(f"Loggin in using  {username} and {password}")
        self.__ctx.wait_until_element_is_visible(locator=loginlocators.USERNAME_FLD)
        self.__ctx.input_text(locator=loginlocators.USERNAME_FLD, text=username)
        self.__ctx.input_text(locator=loginlocators.PASSWORD_FLD, text=password)
        self.__ctx.click_element(locator=loginlocators.LOGIN_BTN)
        
        