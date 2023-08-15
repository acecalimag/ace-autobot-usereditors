 
from robot.api import logger
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword

from UserTeamLibrary.locators import userteamlocators
import time


class AssignAgenttoTeam:
    
    def __init__(self, ctx: SeleniumLibrary) -> None:
        self.__ctx = ctx
        
    @keyword 
    def assign_agent(self, agent_uid: str):
        self.__ctx.wait_until_element_is_visible(locator=userteamlocators.FREEAGENTSLIST)

        option_locator = self.get_option_value(agent_uid)
        self.__ctx.click_element(locator=option_locator)
        self.__ctx.click_button(locator=userteamlocators.MOVESLCBTN)
        
        self.__ctx.scroll_element_into_view(locator=userteamlocators.SAVEBTN)
        self.__ctx.click_button(locator=userteamlocators.SAVEBTN)

    def get_option_value(self, agent_uid):
        option_locator = f"xpath://option[@value='{agent_uid}']"
        option_element = self.__ctx.find_element(option_locator)
        # option_value = option_element.get_attribute("value")
        return option_locator


    @keyword 
    def assign_agent_input(self, agent_name: str, agent_uid: str):
        self.__ctx.wait_until_element_is_visible(locator=userteamlocators.FREEAGENTSLIST)
        self.__ctx.click_element(locator=userteamlocators.FREEAGENTSFLTR)
        self.__ctx.input_text(locator=userteamlocators.FREEAGENTSFLTR, text=agent_name)  

        option_locator = self.get_option_value(agent_uid)
        self.__ctx.wait_until_element_is_visible(locator=option_locator)
        self.__ctx.click_element(locator=option_locator)
        selected = self.__ctx.get_element_attribute(locator=option_locator, attribute="selected")
        logger.info(f"{selected}")
        self.__ctx.click_button(locator=userteamlocators.MOVESLCBTN)
        
        self.__ctx.scroll_element_into_view(locator=userteamlocators.SAVEBTN)
        self.__ctx.click_button(locator=userteamlocators.SAVEBTN)

    def get_option_value(self, agent_uid):
        option_locator = f"xpath://option[@value='{agent_uid}']"
        option_element = self.__ctx.find_element(option_locator)
        # option_value = option_element.get_attribute("value")
        return option_locator
    
