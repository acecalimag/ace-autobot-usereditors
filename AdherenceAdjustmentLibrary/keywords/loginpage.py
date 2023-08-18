
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from AdherenceAdjustmentLibrary.locators import loginlocators
from robot.api import logger
import time


class LoginPage:
    
    def __init__(self, ctx: SeleniumLibrary) -> None:
        self.__ctx = ctx
    
    @keyword
    def login_and_redirect(self, username: str, password: str, redirect_url: str):
        logger.info(f"Logging in using  {username} and {password}")
        self.__ctx.wait_until_element_is_visible(locator=loginlocators.USERNAME_FLD)
        self.__ctx.input_text(locator=loginlocators.USERNAME_FLD, text=username)
        self.__ctx.input_text(locator=loginlocators.PASSWORD_FLD, text=password)
        self.__ctx.click_element(locator=loginlocators.LOGIN_BTN)
        time.sleep(5)
        self.__ctx.go_to(redirect_url)
        # self.__ctx.wait_until_element_is_visible(locator=loginlocators.USERNAME_FLD)
        # self.__ctx.input_text(locator=loginlocators.USERNAME_FLD, text=username)
        # self.__ctx.input_text(locator=loginlocators.PASSWORD_FLD, text=password)
        # self.__ctx.click_element(locator=loginlocators.LOGIN_BTN)


    @keyword
    def logout_to_system(self):
        logger.info("Logging out of the system")
        # self.__ctx.click_element(locator=loginlocators.NAVTOLOGOUT)
        
        # # Wait for the logout button to be clickable and then click it
        # self.__ctx.wait_until_element_is_visible(locator=loginlocators.LOGOUT_BTN)
        # self.__ctx.click_element(locator=loginlocators.LOGOUT_BTN)
        
        # # Wait for the confirmation logout button to be clickable and then click it
        # self.__ctx.wait_until_element_is_visible(locator=loginlocators.CNFRM_LOGOUT_BTN)
        # self.__ctx.click_element(locator=loginlocators.CNFRM_LOGOUT_BTN)
        
        self.__ctx.close_browser()