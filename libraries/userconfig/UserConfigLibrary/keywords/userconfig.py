
from autocore.AssertsLibrary import assert_equal
from libraries.userconfig.UserConfigLibrary.locators import userconfig
from libraries.userconfig.UserMetaCommon.keywords.landingpage import LandingPageKeywords

from autocore.bases import WebLibraryComponent
from robot.api.deco import keyword
from autocore.logger import Logger


class UserConfigKeywords(WebLibraryComponent):

    @keyword(tags=("UserConfigKeywords",))
    def verify_elements_are_complete(self,):
        LandingPageKeywords.elements_in_dictionary_are_visible(self, dict=userconfig.USERCONFIG_ELEMENTS)  

    @keyword(tags=("UserConfigKeywords",))
    def search_for_an_agent(self, agent: str):
        self.web.click(locator=userconfig.USERCONFIG_ELEMENTS['Agent Dropdown'])
        self.web.wait_until_visible(locator=userconfig.AGENT_DESELECT_ALL)
        self.web.scroll_into_view(locator=userconfig.AGENT_DESELECT_ALL)
        self.web.click(locator=userconfig.AGENT_DESELECT_ALL)
        self.web.click(locator=userconfig.AGENT_SEARCH)
        self.web.input_text(locator=userconfig.AGENT_SEARCH, text=agent.upper(), clear=True)
        self.web.click(locator=userconfig.AGENT_SEARCH_RESULT(agent=agent.upper()))
        self.web.click(locator=userconfig.USERCONFIG_ELEMENTS["Go"])
    
    @keyword(tags=("UserConfigKeywords",))
    def update_agent_location(self, agent, location):
        self.search_for_an_agent(agent=agent)
        self.web.click(locator=userconfig.AGENT_LOCATION_ARROW, use_js_if_failed=True)
        self.web.click(locator=userconfig.NEW_LOCATION(location=location))
        self.web.click(locator=userconfig.USERCONFIG_ELEMENTS["Save"])
        self.web.click(locator=userconfig.AGENT_LOCATION_ARROW, use_js_if_failed=True)

    @keyword(tags=("UserConfigKeywords",))
    def sort_column(self):
        self.web.click(locator=userconfig.USERNAME_HEADER)
        HEADER_NAME = self.web.get_text(locator=userconfig.USERNAME_HEADER)
        ascending = list()
        one = self.web.get_text(locator=userconfig.USERNAME_ONE)
        ascending.append(one)
        two = self.web.get_text(locator=userconfig.USERNAME_TWO)
        ascending.append(two)
        three = self.web.get_text(locator=userconfig.USERNAME_THREE)
        ascending.append(three)
        expected_list = ascending
        expected_list.sort()
        Logger.info(self, also_console=True, msg=f"{expected_list} vs {ascending}")
        assert_equal(exp=expected_list, actual=ascending)
        self.web.scroll_into_view(locator=userconfig.USERNAME_HEADER)
        Logger.info(self, also_console=True, msg=f"{HEADER_NAME}'s first three values are: {ascending}")

        
        

        


