
from libraries.userconfig.TeamAssignmentLibrary.locators import pagelocators
from autocore.bases import WebLibraryComponent
from robot.api.deco import keyword

# from SeleniumLibrary import SeleniumLibrary
# from robot.api import logger

class OpenPage(WebLibraryComponent):
    
    # def __init__(self, ctx: SeleniumLibrary) -> None:
    #     self.__ctx = ctx
        
    @keyword 
    def open_team_assignment(self):
        self.logger.info(f"Select configuration for Team Assignment")
        self.web.se_lib.wait_until_element_is_visible(locator=pagelocators.CONFNAV)
        self.web.se_lib.click_element(locator=pagelocators.EDITORDROPDOWN)
        
        self.web.se_lib.wait_until_element_is_visible(locator=pagelocators.TEAMASSIGNMENT)
        self.web.se_lib.click_element(locator=pagelocators.TEAMASSIGNMENT)
        
        
