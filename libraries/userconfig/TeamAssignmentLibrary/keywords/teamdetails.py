
from libraries.userconfig.TeamAssignmentLibrary.locators import teamlocators
from autocore.bases import WebLibraryComponent 
from autocore.AssertsLibrary import assert_equal
from robot.api.deco import keyword

# from SeleniumLibrary import SeleniumLibrary
# from asserts import assert_equal
# from robot.api import logger



class TeamDetails(WebLibraryComponent):
    
    # def __init__(self, ctx: SeleniumLibrary) -> None:
    #     self.__ctx = ctx

    @keyword 
    def check_team_details(self, exp_name: str, exp_lead: str, exp_loc: str):
        self.logger.info(f"Check the details using  {exp_name}, {exp_lead} and {exp_loc}")
        
        team_details = {}
        
        act_name = self.web.get_text(locator=teamlocators.TNAME)
        self.logger.info(f"got_act: {act_name}")
        team_details['Team Name'] = act_name
        assert_equal(act_name, exp_name, f"Expected form name '{exp_name}' does not match the actual name '{act_name}'")

        act_lead = self.web.get_text(locator=teamlocators.TLEAD)
        self.logger.info(f"got_act: {act_lead}")
        team_details['Team Lead'] = act_lead
        assert_equal(act_lead, exp_lead, f"Expected form type '{exp_lead}' does not match the actual type '{act_lead}'")

        act_loc = self.web.get_text(locator=teamlocators.TLOC)
        self.logger.info(f"got_act: {act_loc}")
        team_details['Team Location'] = act_loc
        assert_equal(act_loc, exp_loc, f"Expected form location '{exp_loc}' does not match the actual location '{act_loc}'")
        
        return team_details


