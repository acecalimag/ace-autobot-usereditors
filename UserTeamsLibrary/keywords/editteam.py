 
from robot.api import logger
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import html

from UserTeamsLibrary.locators import userteamslocators
import time


class EditTeam:
    
    def __init__(self, ctx: SeleniumLibrary) -> None:
        self.__ctx = ctx
        

    @keyword 
    def edit_team(self, exp_vulbl: str, ed_name: str, ed_desc: str, ed_lead: str, ed_loc: str, ed_type: str, ed_status: str):
        logger.info(f"Fillout the form using to create new team")

        driver = self.__ctx.driver
        edit_team = {}

        # Verify the View/Update Label
        elements = self.__ctx.driver.find_elements("xpath", userteamslocators.VIEW_UPDATE_LBL)
        if elements:
            element = elements[0]
            act_vulbl = element.text
            
            # Compare actual_text with expected_text
            if act_vulbl == exp_vulbl:
                logger.info(f"View/Update Label is showing and text matches: {act_vulbl}")
                edit_team['View/Update Label'] = 'Showing'
            else:
                logger.info(f"View/Update Label is showing but text does not match. Actual: {act_vulbl}, Expected: {exp_vulbl}")
                edit_team['View/Update Label'] = 'Not Showing'
        else:
            logger.info("View/Update Label is not showing")
            edit_team['View/Update Label'] = 'Not Showing'


    
        # Fillout the form to create new team
        
        # Enter the Name
        self.__ctx.clear_element_text(locator=userteamslocators.TNAME)
        self.__ctx.input_text(locator=userteamslocators.TNAME, text=ed_name)
        
        act_ed_name = self.__ctx.get_value(locator=userteamslocators.TNAME)
        logger.info(f"got_act: {act_ed_name}")
        edit_team['Team Name'] = act_ed_name


        # Enter the Description
        self.__ctx.clear_element_text(locator=userteamslocators.TDESC)
        self.__ctx.input_text(locator=userteamslocators.TDESC, text=ed_desc)
        
        act_ed_desc = self.__ctx.get_value(locator=userteamslocators.TDESC)
        logger.info(f"got_act: {act_ed_desc}")
        edit_team['Team Description'] = act_ed_desc


        # Select Team Lead
        tlead_loc = userteamslocators.TLEAD_LOC(lead=ed_lead)
        self.__ctx.click_element(locator=userteamslocators.TLEAD)
        # time.sleep(5)
        self.__ctx.wait_until_element_is_visible(tlead_loc)
        self.__ctx.click_element(tlead_loc)
        
        act_ed_lead = self.__ctx.get_text(tlead_loc)
        logger.info(f"got_act: {act_ed_lead}")
        edit_team['Team Lead'] = act_ed_lead


        # Select Location
        tloc_loc = userteamslocators.TLOC_LOC(loc=ed_loc)
        self.__ctx.click_element(locator=userteamslocators.TLOC)
        # time.sleep(5)
        self.__ctx.wait_until_element_is_visible(tloc_loc)
        self.__ctx.click_element(tloc_loc)

        act_ed_loc = self.__ctx.get_text(tloc_loc)
        logger.info(f"got_act: {act_ed_loc}")
        edit_team['Team Location'] = act_ed_loc


        # Select Type
        ed_type_modified = ed_type.lower().replace("-", "")
        ttype_loc = userteamslocators.TTYPE_LOC(type=ed_type_modified)
        self.__ctx.click_element(locator=userteamslocators.TTYPE)
        self.__ctx.wait_until_element_is_visible(ttype_loc)
        self.__ctx.click_element(locator=ttype_loc)

        act_ed_type = self.__ctx.get_text(ttype_loc)
        logger.info(f"got_act: {act_ed_type}")
        edit_team['Team Type'] = act_ed_type


        # Select Status
        tstatus_loc = userteamslocators.TSTATUS_LOC(status=ed_status.lower())
        self.__ctx.click_element(tstatus_loc)

        driver = self.__ctx.driver
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
            logger.info("ENABLE BUTTON IS SELECTED - TEAM STATUS is Enabled")
            edit_team['Team Status'] = 'Enabled'
        else:
            logger.info("ENABLE BUTTON IS NOT SELECTED - TEAM STATUS is Disabled")
            edit_team['Team Status'] = 'Disabled'

        if is_disabled_selected and is_disabled_enabled:
            logger.info("DISABLE BUTTON IS SELECTED - TEAM STATUS is Disabled")
            edit_team['Team Status'] = 'Disabled'
        else:
            logger.info("DISABLE BUTTON IS NOT SELECTED - TEAM STATUS is Enabled")
            edit_team['Team Status'] = 'Enabled'


        return edit_team

