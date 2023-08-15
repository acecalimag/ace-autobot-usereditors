
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from robot.api import logger
from asserts import assert_equal
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from UserTeamLibrary.locators import userteamlocators


class TeamDetails:
    
    def __init__(self, ctx: SeleniumLibrary) -> None:
        self.__ctx = ctx

    @keyword 
    def check_team_details(self, exp_name: str, exp_desc: str, exp_lead: str, exp_lead_uid: str, exp_loc: str, exp_loc_code: str, exp_type: str, exp_last_upd: str):
        logger.info(f"Check the details using  {exp_name}, {exp_desc}, {exp_lead}, {exp_loc}, {exp_type} and {exp_last_upd}")
        
        team_details = {}
        

        # Verify the Team Name
        act_name = self.__ctx.get_value(locator=userteamlocators.TNAME)
        logger.info(f"got_act: {act_name}")
        team_details['Team Name'] = act_name
        assert_equal(act_name, exp_name, f"Expected form Team Name '{exp_name}' does not match the actual Team Name '{act_name}'")


        # Verify the Team Lead Details
        tlead_locator = f"//option[text()='{exp_lead}']"
        act_lead = self.__ctx.get_text(tlead_locator)
        logger.info(f"got_act: {act_lead}")
        team_details['Team Lead Name'] = act_lead
        assert_equal(act_lead, exp_lead, f"Expected form Team Lead '{exp_lead}' does not match the actual Team Lead '{act_lead}'")

        act_lead_uid = self.__ctx.get_value(locator=userteamlocators.TLEAD)
        logger.info(f"got_act: {act_lead_uid}")
        team_details['Team Lead UID'] = act_lead_uid
        assert_equal(act_lead_uid, exp_lead_uid, f"Expected form Team Lead UID '{exp_lead_uid}' does not match the actual Team Lead UID '{act_lead_uid}'")


        # Verify the Team Location
        loc_locator = f"//option[text()='{exp_loc}']"
        act_loc = self.__ctx.get_text(loc_locator)
        logger.info(f"got_act: {act_loc}")
        team_details['Team Location'] = act_loc
        assert_equal(act_lead, exp_lead, f"Expected form Team Loc '{exp_loc}' does not match the actual Team Loc '{act_loc}'")

        act_loc_code = self.__ctx.get_value(locator=userteamlocators.TLOC)
        logger.info(f"got_act: {act_loc_code}")
        team_details['Team Location Code'] = act_loc_code
        assert_equal(act_loc_code, exp_loc_code, f"Expected form Team Location Code '{exp_loc_code}' does not match the actual Team Location Code '{act_loc_code}'")


        # Verify the Team Type
        act_type = self.__ctx.get_value(locator=userteamlocators.TTYPE)
        logger.info(f"got_act: {act_type}")
        team_details['Team Type'] = act_type
        assert_equal(act_type, exp_type, f"Expected form Team Type '{exp_type}' does not match the actual Team Type '{act_type}'")


        # Verify the Team Status
        driver = self.__ctx.driver
        enabled_radio_locator = (By.XPATH, "//input[@id='enabled']")
        disabled_radio_locator = (By.XPATH, "//input[@id='disabled']")

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
            logger.info("ENABLE BUTTON IS SELECTED - TEAM STATUS is Enabled")
        else:
            logger.info("ENABLE BUTTON IS NOT SELECTED - TEAM STATUS is Disabled")

        if is_disabled_selected and is_disabled_enabled:
            logger.info("DISABLE BUTTON IS SELECTED - TEAM STATUS is Disabled")
        else:
            logger.info("DISABLE BUTTON IS NOT SELECTED - TEAM STATUS is Enabled")


        # Verify the Last Updated Details
        act_last_upd = self.__ctx.get_text(locator=userteamlocators.UPDTIME)
        logger.info(f"got_act: {act_last_upd}")
        team_details['Team Name'] = act_last_upd
        assert_equal(act_last_upd, exp_last_upd, f"Expected form Last Updated '{exp_last_upd}' does not match the actual Last Updated '{act_last_upd}'")


        
        return team_details


