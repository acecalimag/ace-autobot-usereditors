
from AdherenceAdjustmentLibrary.locators import pagelocators
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from robot.api import logger

class OpenPage:
    
    def __init__(self, ctx: SeleniumLibrary) -> None:
        self.__ctx = ctx
        
    @keyword 
    def open_adherence_adjustment(self):
        logger.info(f"Select configuration for User Team")
        self.__ctx.wait_until_element_is_visible(locator=pagelocators.CONFNAV)
        self.__ctx.click_element(locator=pagelocators.EDITORDROPDOWN)
        
        self.__ctx.wait_until_element_is_visible(locator=pagelocators.USERTEAM)
        self.__ctx.click_element(locator=pagelocators.USERTEAM)
        
        
