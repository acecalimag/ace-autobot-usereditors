
from libraries.userconfig.UserTeamsLibrary.locators import userteamslocators
from autocore.bases import WebLibraryComponent
from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from SeleniumLibrary import SeleniumLibrary
# from robot.api import logger
import time


class CreateTeam(WebLibraryComponent):
    
    # def __init__(self, ctx: SeleniumLibrary) -> None:
    #     self.__ctx = ctx
        
    @keyword 
    def click_create_team(self):
        self.web.se_lib.wait_until_element_is_visible(locator=userteamslocators.CR_TEAM_BTN)
        self.web.se_lib.click_button(locator=userteamslocators.CR_TEAM_BTN)


    @keyword 
    def fillout_form(self, exp_cntlbl: str, in_name: str, in_desc: str, in_lead: str, in_loc: str, in_type: str, in_status: str):
        self.logger.info(f"Fillout the form using to create new team")

        driver = self.web.se_lib.driver

        create_new_team = {}

        # Verify the Create New Team Label
        elements = self.web.se_lib.driver.find_elements("xpath", userteamslocators.VIEW_UPDATE_LBL)
        if elements:
            element = elements[0]
            act_cntlbl = element.text
            
            # Compare actual_text with expected_text
            if act_cntlbl == exp_cntlbl:
                self.logger.info(f"Create New Team Label is showing and text matches: {act_cntlbl}")
                create_new_team['Create New Team Label'] = 'Showing'
            else:
                self.logger.info(f"Create New Team Label is showing but text does not match. Actual: {act_cntlbl}, Expected: {exp_cntlbl}")
                create_new_team['Create New Team Label'] = 'Not Showing'
        else:
            self.logger.info("Create New Team Label is not showing")
            create_new_team['Create New Team Label'] = 'Not Showing'


    
        # Fillout the form to create new team
        
        # Enter the Name
        self.web.input_text(locator=userteamslocators.TNAME, text=in_name)
        
        act_in_name = self.web.get_value(locator=userteamslocators.TNAME)
        self.logger.info(f"got_act: {act_in_name}")
        create_new_team['Team Name'] = act_in_name


        # Enter the Description
        self.web.input_text(locator=userteamslocators.TDESC, text=in_desc)
        
        act_in_desc = self.web.get_value(locator=userteamslocators.TDESC)
        self.logger.info(f"got_act: {act_in_desc}")
        create_new_team['Team Description'] = act_in_desc


        # Select Team Lead
        tlead_loc = userteamslocators.TLEAD_LOC(lead=in_lead)
        self.web.se_lib.click_element(locator=userteamslocators.TLEAD)
        # time.sleep(5)
        self.web.se_lib.wait_until_element_is_visible(tlead_loc)
        self.web.se_lib.click_element(tlead_loc)
        
        act_in_lead = self.web.get_text(tlead_loc)
        self.logger.info(f"got_act: {act_in_lead}")
        create_new_team['Team Lead'] = act_in_lead


        # Select Location
        tloc_loc = userteamslocators.TLOC_LOC(loc=in_loc)
        self.web.se_lib.click_element(locator=userteamslocators.TLOC)
        # time.sleep(5)
        self.web.se_lib.wait_until_element_is_visible(tloc_loc)
        self.web.se_lib.click_element(tloc_loc)

        act_in_loc = self.web.get_text(tloc_loc)
        self.logger.info(f"got_act: {act_in_loc}")
        create_new_team['Team Location'] = act_in_loc


        # Select Type
        in_type_modified = in_type.lower().replace("-", "")
        ttype_loc = userteamslocators.TTYPE_LOC(type=in_type_modified)
        self.web.se_lib.click_element(locator=userteamslocators.TTYPE)
        self.web.se_lib.wait_until_element_is_visible(ttype_loc)
        self.web.se_lib.click_element(locator=ttype_loc)

        act_in_type = self.web.get_text(ttype_loc)
        self.logger.info(f"got_act: {act_in_type}")
        create_new_team['Team Type'] = act_in_type


        # Select Status
        tstatus_loc = userteamslocators.TSTATUS_LOC(status=in_status.lower())
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
            create_new_team['Team Status'] = 'Enabled'
            act_in_stat = 'Enabled'
        else:
            self.logger.info("ENABLE BUTTON IS NOT SELECTED - TEAM STATUS is Disabled")
            create_new_team['Team Status'] = 'Disabled'
            act_in_stat = 'Disabled'

        if is_disabled_selected and is_disabled_enabled:
            self.logger.info("DISABLE BUTTON IS SELECTED - TEAM STATUS is Disabled")
            create_new_team['Team Status'] = 'Disabled'
            act_in_stat = 'Disabled'
        else:
            self.logger.info("DISABLE BUTTON IS NOT SELECTED - TEAM STATUS is Enabled")
            create_new_team['Team Status'] = 'Enabled'
            act_in_stat = 'Enabled'
        
        self.logger.info(f"got_act: {act_in_stat}")
        create_new_team['Team Status'] = act_in_stat

        return create_new_team



    @keyword 
    def click_save_button(self):
        self.web.se_lib.scroll_element_into_view(locator=userteamslocators.SAVEBTN)
        self.web.se_lib.click_button(locator=userteamslocators.SAVEBTN)
        # time.sleep(5)


    @keyword 
    def click_create_button(self):
        self.web.se_lib.scroll_element_into_view(locator=userteamslocators.CRTBTN)
        self.web.se_lib.click_button(locator=userteamslocators.CRTBTN)
        # time.sleep(5)
        # self.web.se_lib.reload_page
        # time.sleep(5)