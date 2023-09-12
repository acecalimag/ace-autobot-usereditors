
from autocore.bases import WebLibraryComponent
from libraries.userconfig.UserTeamsLibrary.locators import userteams
from libraries.userconfig.UserMetaCommon.keywords.landingpage import LandingPageKeywords
from libraries.db.KjtDbLibrary.keywords.userteams import UserTeams
from autocore.AssertsLibrary import assert_equal
from autocore.bases import WebLibraryComponent
from robot.api.deco import keyword
# from autocore.logger import Logger


class UserTeamsKeywords(WebLibraryComponent):

    @keyword(tags=("UserTeamsKeywords",))
    def verify_elements_are_complete(self,):
        self.web.click(locator=userteams.USERTEAMS_ELEMENTS["Create Team"])
        self.web.click(locator=userteams.FIRST_TEAM)
        LandingPageKeywords.elements_in_dictionary_are_visible(self, dict=userteams.USERTEAMS_ELEMENTS)  

    @keyword(tags=("UserTeamsKeywords",))
    def choose_existing_team(self, team: str):
        
        while True:
            try:
                self.web.is_visible(locator=userteams.TEAM(team=team),timeout=5)
                self.web.scroll_into_view(userteams.TEAM(team=team))
                self.web.click(userteams.TEAM(team=team))
                self.logger.info(also_console=True, msg=f"Successfully chose: {team}")
                break
                
            except:
                try:
                    self.web.scroll_into_view(userteams.USERTEAMS_ELEMENTS["Next"])
                    self.web.click(userteams.USERTEAMS_ELEMENTS["Next"])
                    self.logger.info(also_console=True, msg=f"Clicked next")
                except:
                    self.logger.info(also_console=True, msg=f"Failed to click next")
                    break
            
        ACT_TEAM_NAME = self.web.get_value(locator=userteams.TEAM_NAME)
        assert_equal(actual=ACT_TEAM_NAME, exp=team)

    @keyword(tags=("UserTeamsKeyword",))
    def update_team_type(self, type: str):
        try:
            self.web.click(userteams.USERTEAMS_ELEMENTS["Type Select"])
            self.web.click(userteams.TEAM_TYPE(type=type))
            ACTUAL_TYPE_VALUE = self.web.get_value(userteams.USERTEAMS_ELEMENTS["Type Select"])
            self.logger.info(also_console=True, msg=f"Chose type: {ACTUAL_TYPE_VALUE}",)
            assert_equal(actual=ACTUAL_TYPE_VALUE, exp=type)
        except:
            self.logger.info(also_console=True, msg=f"Failed to choose team type: {type}")
            raise Exception
        self.web.click(userteams.USERTEAMS_ELEMENTS["Save"])
        self.logger.info(also_console=True, msg=f"Saved successfully")

       
             


