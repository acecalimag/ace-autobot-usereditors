 
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword

from TeamAssignmentLibrary.locators import teamlocators
import time


class RemoveAgenttoTeam:
    
    def __init__(self, ctx: SeleniumLibrary) -> None:
        self.__ctx = ctx
        
    @keyword 
    def remove_agent(self, agent_name: str, agent_uid: str):
        self.__ctx.wait_until_element_is_visible(locator=teamlocators.TEAMROSTERLIST)
        self.__ctx.click_element(locator=teamlocators.TEAMROSTERFLTR)
        # self.__ctx.input_text(locator=teamlocators.TEAMROSTERFLTR, text=agent_name)
        # time.sleep(5)  

        option_locator = self.get_option_value(agent_uid)
        self.__ctx.wait_until_element_is_enabled(locator=option_locator)        
        self.__ctx.click_element(locator=option_locator)
        self.__ctx.click_button(locator=teamlocators.REMOVESLCBTN)
        self.__ctx.scroll_element_into_view(locator=teamlocators.SAVEBTN)
        self.__ctx.click_button(locator=teamlocators.SAVEBTN)

    def get_option_value(self, agent_uid):
        option_locator = f"xpath://option[@value='{agent_uid}']"
        self.__ctx.find_element(option_locator)
        return option_locator
