
from libraries.userconfig.TeamAssignmentLibrary.locators import teamlocators
from autocore.bases import WebLibraryComponent 
from robot.api.deco import keyword

# from robot.api import logger
# from SeleniumLibrary import SeleniumLibrary
# import time


class AssignAgenttoTeam(WebLibraryComponent):
    
    # def __init__(self, ctx: SeleniumLibrary) -> None:
    #     self.__ctx = ctx
        
    @keyword 
    def assign_agent(self, agent_uid: str):
        self.web.se_lib.wait_until_element_is_visible(locator=teamlocators.FREEAGENTSLIST)

        option_locator = self.get_option_value(agent_uid)
        self.web.se_lib.click_element(locator=option_locator)
        self.web.se_lib.click_button(locator=teamlocators.MOVESLCBTN)
        
        self.web.se_lib.scroll_element_into_view(locator=teamlocators.SAVEBTN)
        self.web.se_lib.click_button(locator=teamlocators.SAVEBTN)

    def get_option_value(self, agent_uid):
        option_locator = f"xpath://option[@value='{agent_uid}']"
        option_element = self.web.se_lib.find_element(option_locator)
        # option_value = option_element.get_attribute("value")
        return option_locator


    @keyword 
    def assign_agent_input(self, agent_name: str, agent_uid: str):
        self.web.se_lib.wait_until_element_is_visible(locator=teamlocators.FREEAGENTSLIST)
        self.web.se_lib.click_element(locator=teamlocators.FREEAGENTSFLTR)
        self.web.input_text(locator=teamlocators.FREEAGENTSFLTR, text=agent_name)  

        option_locator = self.get_option_value(agent_uid)
        self.web.se_lib.wait_until_element_is_visible(locator=option_locator)
        self.web.se_lib.click_element(locator=option_locator)
        selected = self.web.get_element_attribute(locator=option_locator, attribute="selected")
        self.logger.info(f"{selected}")
        self.web.click_button(locator=teamlocators.MOVESLCBTN)
        
        self.web.scroll_element_into_view(locator=teamlocators.SAVEBTN)
        self.web.click_button(locator=teamlocators.SAVEBTN)

    def get_option_value(self, agent_uid):
        option_locator = f"xpath://option[@value='{agent_uid}']"
        option_element = self.web.se_lib.find_element(option_locator)
        # option_value = option_element.get_attribute("value")
        return option_locator
    
