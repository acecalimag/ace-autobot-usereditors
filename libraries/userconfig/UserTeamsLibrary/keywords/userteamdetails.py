
from libraries.userconfig.UserTeamsLibrary.locators import userteamslocators
from autocore.bases import WebLibraryComponent
from autocore.AssertsLibrary import assert_equal
from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from SeleniumLibrary import SeleniumLibrary
# from robot.api import logger
# from asserts import assert_equal


class UserTeamDetails(WebLibraryComponent):
    
    # def __init__(self, ctx: SeleniumLibrary) -> None:
    #     self.__ctx = ctx

    @keyword 
    def check_team_details(self, exp_name: str, exp_desc: str, exp_lead: str, exp_loc: str, exp_type: str, exp_stat: str, exp_last_upd: str):
        self.logger.info(f"Check the details using  {exp_name}, {exp_desc}, {exp_lead}, {exp_loc}, {exp_type}, {exp_stat} and {exp_last_upd}")
        
        team_details = {}
        
        # Verify the Team Name
        self.web.se_lib.wait_until_element_is_visible(locator=userteamslocators.TNAME)
        act_name = self.web.get_value(locator=userteamslocators.TNAME)
        self.logger.info(f"got_act: {act_name}")
        team_details['Team Name'] = act_name
        assert_equal(act_name, exp_name, f"Expected form Team Name '{exp_name}' does not match the actual Team Name '{act_name}'")


        # Verify the Team Description
        act_desc = self.web.get_value(locator=userteamslocators.TDESC)
        self.logger.info(f"got_act: {act_desc}")
        team_details['Team Description'] = act_desc
        assert_equal(act_desc, exp_desc, f"Expected form Team Description '{exp_desc}' does not match the actual Team Description '{act_desc}'")


        # Verify the Team Lead Name
        tlead_loc = userteamslocators.TLEAD_LOC(lead=exp_lead)
        act_lead = self.web.get_text(tlead_loc)
        self.logger.info(f"got_act: {act_lead}")
        team_details['Team Lead'] = act_lead
        assert_equal(act_lead, exp_lead, f"Expected form Team Lead '{exp_lead}' does not match the actual Team Lead '{act_lead}'")        


        # Verify the Team Location
        tloc_loc = userteamslocators.TLOC_LOC(loc=exp_loc)
        act_loc = self.web.get_text(tloc_loc)
        self.logger.info(f"got_act: {act_loc}")
        team_details['Team Location'] = act_loc
        assert_equal(act_lead, exp_lead, f"Expected form Team Loc '{exp_loc}' does not match the actual Team Loc '{act_loc}'")


        # Verify the Team Type
        exp_type_modified = exp_type.lower().replace("-", "")
        ttype_loc = userteamslocators.TTYPE_LOC(type=exp_type_modified)

        act_type = self.web.get_text(ttype_loc)
        self.logger.info(f"got_act: {act_type}")
        team_details['Team Type'] = act_type
        assert_equal(act_type, exp_type, f"Expected form Team Type '{exp_type}' does not match the actual Team Type '{act_type}'")



        # Verify the Team Status
        driver = self.web.se_lib.driver
        enabled_radio_locator = (By.XPATH, userteamslocators.TSTAT_ENB)
        disabled_radio_locator = (By.XPATH, userteamslocators.TSTAT_DISB)

        enabled_radio_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(enabled_radio_locator)
        )
        is_enabled_selected = enabled_radio_button.is_selected()
        is_enabled_enabled = enabled_radio_button.is_enabled()

        disabled_radio_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(disabled_radio_locator)
        )
        is_disabled_selected = disabled_radio_button.is_selected()
        is_disabled_enabled = disabled_radio_button.is_enabled()

        if is_enabled_selected and is_enabled_enabled:
            self.logger.info("ENABLE BUTTON IS SELECTED - TEAM STATUS is Enabled")
            team_details['Team Status'] = 'Enabled'
            act_stat = 'Enabled'
        else:
            self.logger.info("ENABLE BUTTON IS NOT SELECTED - TEAM STATUS is Disabled")
            team_details['Team Status'] = 'Disabled'
            act_stat = 'Disabled'

        if is_disabled_selected and is_disabled_enabled:
            self.logger.info("DISABLE BUTTON IS SELECTED - TEAM STATUS is Disabled")
            team_details['Team Status'] = 'Disabled'
            act_stat = 'Disabled'
        else:
            self.logger.info("DISABLE BUTTON IS NOT SELECTED - TEAM STATUS is Enabled")
            team_details['Team Status'] = 'Enabled'
            act_stat = 'Enabled'
        
        self.logger.info(f"got_act: {act_stat}")
        team_details['Team Status'] = act_stat
        assert_equal(act_stat, exp_stat, f"Expected form Team Status '{exp_stat}' does not match the actual Team Status '{act_stat}'")


        # Verify the Last Updated Details
        act_last_upd = self.web.get_text(locator=userteamslocators.UPDTIME)
        self.logger.info(f"got_act: {act_last_upd}")
        team_details['Last Updated'] = act_last_upd
        assert_equal(act_last_upd, exp_last_upd, f"Expected form Last Updated '{exp_last_upd}' does not match the actual Last Updated '{act_last_upd}'")


        return team_details


