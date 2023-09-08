 
from libraries.userconfig.UserTeamsLibrary.locators import userteamslocators
from autocore.bases import WebLibraryComponent
from selenium.webdriver.support.ui import WebDriverWait
from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# from SeleniumLibrary import SeleniumLibrary
# from robot.api import logger
# import time


class EditTeam(WebLibraryComponent):
    
    # def __init__(self, ctx: SeleniumLibrary) -> None:
    #     self.__ctx = ctx
        

    @keyword 
    def edit_team(self, exp_vulbl: str, ed_name: str, ed_desc: str, ed_lead: str, ed_loc: str, ed_type: str, ed_status: str):
        self.logger.info(f"Fillout the form using to create new team")

        driver = self.web.se_lib.driver
        edit_team = {}

        # Verify the View/Update Label
        elements = self.web.se_lib.driver.find_elements("xpath", userteamslocators.VIEW_UPDATE_LBL)
        if elements:
            element = elements[0]
            act_vulbl = element.text
            
            # Compare actual_text with expected_text
            if act_vulbl == exp_vulbl:
                self.logger.info(f"View/Update Label is showing and text matches: {act_vulbl}")
                edit_team['View/Update Label'] = 'Showing'
            else:
                self.logger.info(f"View/Update Label is showing but text does not match. Actual: {act_vulbl}, Expected: {exp_vulbl}")
                edit_team['View/Update Label'] = 'Not Showing'
        else:
            self.logger.info("View/Update Label is not showing")
            edit_team['View/Update Label'] = 'Not Showing'


    
        # Fillout the form to create new team
        
        # Enter the Name
        self.web.se_lib.clear_element_text(locator=userteamslocators.TNAME)
        self.web.input_text(locator=userteamslocators.TNAME, text=ed_name)
        
        act_ed_name = self.web.get_value(locator=userteamslocators.TNAME)
        self.logger.info(f"got_act: {act_ed_name}")
        edit_team['Team Name'] = act_ed_name


        # Enter the Description
        self.web.se_lib.clear_element_text(locator=userteamslocators.TDESC)
        self.web.input_text(locator=userteamslocators.TDESC, text=ed_desc)
        
        act_ed_desc = self.web.get_value(locator=userteamslocators.TDESC)
        self.logger.info(f"got_act: {act_ed_desc}")
        edit_team['Team Description'] = act_ed_desc


        # Select Team Lead
        tlead_loc = userteamslocators.TLEAD_LOC(lead=ed_lead)
        self.web.click_element(locator=userteamslocators.TLEAD)
        # time.sleep(5)
        self.web.se_lib.wait_until_element_is_visible(tlead_loc)
        self.web.se_lib.click_element(tlead_loc)
        
        act_ed_lead = self.web.get_text(tlead_loc)
        self.logger.info(f"got_act: {act_ed_lead}")
        edit_team['Team Lead'] = act_ed_lead


        # Select Location
        tloc_loc = userteamslocators.TLOC_LOC(loc=ed_loc)
        self.web.se_lib.click_element(locator=userteamslocators.TLOC)
        # time.sleep(5)
        self.web.se_lib.wait_until_element_is_visible(tloc_loc)
        self.web.se_lib.click_element(tloc_loc)

        act_ed_loc = self.web.get_text(tloc_loc)
        self.logger.info(f"got_act: {act_ed_loc}")
        edit_team['Team Location'] = act_ed_loc


        # Select Type
        ed_type_modified = ed_type.lower().replace("-", "")
        ttype_loc = userteamslocators.TTYPE_LOC(type=ed_type_modified)
        self.web.se_lib.click_element(locator=userteamslocators.TTYPE)
        self.web.se_lib.wait_until_element_is_visible(ttype_loc)
        self.web.se_lib.click_element(locator=ttype_loc)

        act_ed_type = self.web.get_text(ttype_loc)
        self.logger.info(f"got_act: {act_ed_type}")
        edit_team['Team Type'] = act_ed_type


        # Select Status
        tstatus_loc = userteamslocators.TSTATUS_LOC(status=ed_status.lower())
        self.web.se_lib.click_element(tstatus_loc)

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
            edit_team['Team Status'] = 'Enabled'
            act_ed_stat = 'Enabled'
        else:
            self.logger.info("ENABLE BUTTON IS NOT SELECTED - TEAM STATUS is Disabled")
            edit_team['Team Status'] = 'Disabled'
            act_ed_stat = 'Disabled'

        if is_disabled_selected and is_disabled_enabled:
            self.logger.info("DISABLE BUTTON IS SELECTED - TEAM STATUS is Disabled")
            edit_team['Team Status'] = 'Disabled'
            act_ed_stat = 'Disabled'
        else:
            self.logger.info("DISABLE BUTTON IS NOT SELECTED - TEAM STATUS is Enabled")
            edit_team['Team Status'] = 'Enabled'
            act_ed_stat = 'Enabled'
        
        self.logger.info(f"got_act: {act_ed_stat}")
        edit_team['Team Status'] = act_ed_stat


        return edit_team

