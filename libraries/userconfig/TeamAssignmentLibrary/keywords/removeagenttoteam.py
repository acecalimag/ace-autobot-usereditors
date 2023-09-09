
from libraries.userconfig.TeamAssignmentLibrary.locators import teamlocators
from autocore.bases import WebLibraryComponent
from robot.api.deco import keyword

# from robot.api import logger
# from SeleniumLibrary import SeleniumLibrary
# import time


class RemoveAgenttoTeam(WebLibraryComponent):
    
    # def __init__(self, ctx: SeleniumLibrary) -> None:
    #     self.__ctx = ctx
        
    @keyword 
    def remove_agent(self, agent_name: str, agent_uid: str):
        self.web.se_lib.wait_until_element_is_visible(locator=teamlocators.TEAMROSTERLIST)
        self.web.se_lib.click_element(locator=teamlocators.TEAMROSTERFLTR)
        self.web.input_text(locator=teamlocators.TEAMROSTERFLTR, text=agent_name)
        # time.sleep(5)  

        option_locator = self.get_option_value(agent_uid)
        self.web.se_lib.wait_until_element_is_visible(locator=option_locator)
        self.web.se_lib.click_element(locator=option_locator)
        selected = self.web.se_lib.get_element_attribute(locator=option_locator, attribute="selected")
        self.logger.info(f"{selected}")
        self.web.se_lib.click_button(locator=teamlocators.REMOVESLCBTN)
        self.web.se_lib.scroll_element_into_view(locator=teamlocators.SAVEBTN)
        self.web.se_lib.click_button(locator=teamlocators.SAVEBTN)


    def get_option_value(self, agent_uid):
        option_locator = f"xpath://option[@value='{agent_uid}']"
        self.web.se_lib.find_element(option_locator)
        return option_locator

