
from autocore.bases import WebLibraryComponent
from UserTeamsLibrary.locators import pagelocators
from robot.api.deco import keyword

# from SeleniumLibrary import SeleniumLibrary
# from robot.api import logger


class OpenPage(WebLibraryComponent):
    
    # def __init__(self, ctx: SeleniumLibrary) -> None:
    #     self.__ctx = ctx
        
    @keyword 
    def open_user_team(self):
        self.logger.info(f"Select configuration for User Team")
        self.web.se_lib.wait_until_element_is_visible(locator=pagelocators.CONFNAV)
        self.web.se_lib.click_element(locator=pagelocators.EDITORDROPDOWN)
        
        self.web.se_lib.wait_until_element_is_visible(locator=pagelocators.USERTEAM)
        self.web.se_lib.click_element(locator=pagelocators.USERTEAM)
        
        
