
from robot.api.deco import keyword
from autocore.bases import WebLibraryComponent
from libraries.userconfig.UserMetaCommon.dto.navbardetails import NavbarDetails
from libraries.userconfig.UserMetaCommon.locators import landingpage
from autocore.logger import Logger
from datetime import timedelta


class LandingPageKeywords(WebLibraryComponent):
    #User Configuration
    @keyword(tags=("LandingPageKeywords","UserConfigCommonKeywords"))
    def open_user_config(self):
        self.__open_editor_located_by(locator=landingpage.USER_CONFIG)
    
    @keyword(tags=("LandingPageKeywords","UserConfigCommonKeywords"))
    def open_user_teams(self):
        self.__open_editor_located_by(locator=landingpage.USER_TEAMS)
    
    @keyword(tags=("LandingPageKeywords","UserConfigCommonKeywords"))
    def open_aux_config(self):
        self.__open_editor_located_by(locator=landingpage.AUX_CONFIG)
    
    @keyword(tags=("LandingPageKeywords","UserConfigCommonKeywords"))
    def open_team_assignment(self):
        self.__open_editor_located_by(locator=landingpage.TEAM_ASSIGNMENT)

    #Aux Configuration
    @keyword(tags=("LandingPageKeywords","UserConfigCommonKeywords"))
    def open_agent_ranking(self):
        self.__open_editor_located_by(locator=landingpage.AGENT_RANKING)
    
    @keyword(tags=("LandingPageKeywords","UserConfigCommonKeywords"))
    def open_auto_assign(self):
        self.__open_editor_located_by(locator=landingpage.AUTO_ASSIGN)
    
    @keyword(tags=("LandingPageKeywords","UserConfigCommonKeywords"))
    def open_call_restriction(self):
        self.__open_editor_located_by(locator=landingpage.CALL_RESTRICTION)

    #Client Configuration
    @keyword(tags=("LandingPageKeywords","UserConfigCommonKeywords"))
    def open_restaurant_config(self):
        self.__open_editor_located_by(locator=landingpage.RESTAURANT_CONFIG)
    
    @keyword(tags=("LandingPageKeywords","UserConfigCommonKeywords"))
    def open_restaurant_grp(self):
        self.__open_editor_located_by(locator=landingpage.RESTAURANT_GROUP)
    
    @keyword(tags=("LandingPageKeywords","UserConfigCommonKeywords"))
    def open_training_grp(self):
        self.__open_editor_located_by(locator=landingpage.TRAINING_GRP)
       
    def __open_editor_located_by(self, locator: str):
        self.web.wait_until_visible(
            locator=landingpage.WONDERS_LOGO)
        self.web.wait_until_visible(
            locator=landingpage.NAVBAR_OPTION_EDITORS_DROPDOWN)
        self.web.click(
            locator=landingpage.NAVBAR_OPTION_EDITORS_DROPDOWN)
        self.web.scroll_into_view(locator=locator)
        self.web.click(locator=locator)
    
    @keyword
    def elements_in_dictionary_are_visible(self, dict: dict, timeout: timedelta = None):
        """Where dictionary has KEY as labels and VALUE as locator (css, xpath, and etc.)"""

        for key, value in dict.items():
           self.web.wait_until_visible(locator=value, timeout=timeout)
           dictionary = list(dict.keys())
        Logger.info(self, also_console=True, msg=f"'{dictionary}' elements are visible")

    @keyword
    def logout_from_usermeta(self):
        self.web.click(locator=landingpage.NAVBAR_MENU)
        self.web.wait_until_visible(locator=landingpage.NAVBAR_MENU_LOGOUT)
        self.web.click(locator=landingpage.NAVBAR_MENU_LOGOUT)
        self.web.wait_until_visible(locator=landingpage.NAVBAR_MENU_YES)
        self.web.click(locator=landingpage.NAVBAR_MENU_YES)

    # @keyword(tags=("LandingPageKeywords","UserConfigCommonKeywords"))
    # def get_navbar_details(self, _:NavbarDetails = None) -> NavbarDetails:
    #     self.web.wait_until_visible(locator=landingpage.WONDERS_LOGO)
    #     self.web.wait_until_visible(
    #         locator=landingpage.NAVBAR_OPTION_EDITORS_DROPDOWN)
    #     menu_items = [i for i in self.web.get_texts(locator=landingpage.NAVBAR_MENU_LABLES, normalize=True)]
    #     self.web.click(locator=landingpage.NAVBAR_OPTION_EDITORS_DROPDOWN)
    #     editors = [i for i in self.web.get_texts(landingpage.NAVBAR_DROPDOWN_OPTIONS, normalize=True) if len(i) > 0]
    #     self.web.click(locator=landingpage.NAVBAR_OPTION_EDITORS_DROPDOWN)
    #     details = NavbarDetails(
    #         username=self.web.get_text(locator=landingpage.USERNAME),
    #         position=self.web.get_text(locator=landingpage.POSITION),
    #         menu_items=menu_items,
    #         editor_dropdown_options=editors
    #     )
    #     self.logger.debug(details)
    #     return details