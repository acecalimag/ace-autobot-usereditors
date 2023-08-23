
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from robot.api import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time


from AdherenceAdjustmentLibrary.locators import adhadjlocators


class AdherenceAdjustmentPage:
    
    def __init__(self, ctx: SeleniumLibrary) -> None:
        self.__ctx = ctx


    @keyword 
    def check_page_header(self, exp_hdr_adhadjlbl: str, exp_hdr_user: str):
        logger.info(f"Check the Adherence Adjustment Headers Details")

        adhadj_header = {}

        # Verify the Adherence Adjustment Label in Header
        self.__ctx.wait_until_element_is_visible(locator=adhadjlocators.ADADJLBL)
        elements = self.__ctx.driver.find_elements("xpath", adhadjlocators.ADADJLBL)
        if elements:
            element = elements[0]
            act_hdr_adhadjlbl = element.text
            
            # Compare actual_text with expected_text
            if act_hdr_adhadjlbl == exp_hdr_adhadjlbl:
                logger.info(f"Adherence Adjustment Label is showing and text matches: {act_hdr_adhadjlbl}")
                adhadj_header['Adherence Adjustment Label'] = 'Showing'
            else:
                logger.info(f"Adherence Adjustment Label is showing but text does not match. Actual: {act_hdr_adhadjlbl}, Expected: {exp_hdr_adhadjlbl}")
                adhadj_header['Adherence Adjustment Label'] = 'Not Showing'
        else:
            logger.info("Adherence Adjustment Label is not showing")
            adhadj_header['Adherence Adjustment Label'] = 'Not Showing'


        # Verify the User Label in Header
        self.__ctx.wait_until_element_is_visible(locator=adhadjlocators.HDR_USER)
        self.__ctx.capture_page_screenshot
        elements = self.__ctx.driver.find_elements("xpath", adhadjlocators.HDR_USER)
        if elements:
            element = elements[0]
            act_hdr_user = element.text
            
            # Compare actual_text with expected_text
            if act_hdr_user == exp_hdr_user:
                logger.info(f"User Header Label is showing and text matches: {act_hdr_user}")
                adhadj_header['User Header Label'] = 'Showing'
            else:
                logger.info(f"User Header Label is showing but text does not match. Actual: {act_hdr_user}, Expected: {exp_hdr_user}")
                adhadj_header['User Header Label'] = 'Not Showing'
        else:
            logger.info("User Header Label is not showing")
            adhadj_header['User Header Label'] = 'Not Showing'


        return adhadj_header



    @keyword 
    def check_dispute_table(self, exp_rtrlbl: str, exp_unamelbl: str, exp_loclbl: str, exp_teamlbl: str, exp_statuslbl: str, exp_rvwrlbl: str, exp_rvwdatlbl: str, exp_crtdlbl: str):
        logger.info(f"Check the Dispute Table if fields, labels, and buttons are present")

        dispute_table = {}

        # Verify the Dispute Table Column Labels (Requested Time Range)
        element_locator = (By.XPATH, adhadjlocators.TBL_RTR_LBL)
        driver = self.__ctx.driver

        # Scroll the element into view using WebDriverWait and JavaScript
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(element_locator)
        )
        driver.execute_script("arguments[0].scrollIntoView();", element)

        # Find the element again after scrolling
        elements = driver.find_elements(*element_locator)

        # Your existing code for verification and comparison
        if elements:
            element = elements[0]
            act_rtrlbl = element.text

            # Compare actual_text with expected_text
            if act_rtrlbl == exp_rtrlbl:
                logger.info(f"Requested Time Range Label in Dispute Table is showing and text matches: {act_rtrlbl}")
                dispute_table['Requested Time Range Label in Dispute Table'] = 'Showing'
            else:
                logger.info(f"Requested Time Range Label is showing but text does not match. Actual: {act_rtrlbl}, Expected: {exp_rtrlbl}")
                dispute_table['Requested Time Range Label in Dispute Table'] = 'Not Showing'
        else:
            logger.info("Requested Time Range Label in Dispute Table is not showing")
            dispute_table['Requested Time Range Label in Dispute Table'] = 'Not Showing'



        # Verify the Dispute Table Column Labels (Username)
        elements = self.__ctx.driver.find_elements("xpath", adhadjlocators.TBL_UNAME_LBL)
        if elements:
            element = elements[0]
            act_unamelbl = element.text
            
            # Compare actual_text with expected_text
            if act_unamelbl == exp_unamelbl:
                logger.info(f"Username Label in Dispute Table is showing and text matches: {act_unamelbl}")
                dispute_table['UsernameLabel in Dispute Table'] = 'Showing'
            else:
                logger.info(f"Username Label is showing but text does not match. Actual: {act_unamelbl}, Expected: {exp_unamelbl}")
                dispute_table['Username Label in Dispute Table'] = 'Not Showing'
        else:
            logger.info("Username in Dispute Table is not showing")
            dispute_table['Username in Dispute Table'] = 'Not Showing'


        # Verify the Dispute Table Column Labels (Location)
        elements = self.__ctx.driver.find_elements("xpath", adhadjlocators.TBL_LOC_LBL)
        if elements:
            element = elements[0]
            act_loclbl = element.text
            
            # Compare actual_text with expected_text
            if act_loclbl == exp_loclbl:
                logger.info(f"Location Label in Dispute Table is showing and text matches: {act_loclbl}")
                dispute_table['Location Label in Dispute Table'] = 'Showing'
            else:
                logger.info(f"Location Label is showing but text does not match. Actual: {act_loclbl}, Expected: {exp_loclbl}")
                dispute_table['Location Label in Dispute Table'] = 'Not Showing'
        else:
            logger.info("Location LABEL in Dispute Table is not showing")
            dispute_table['Location Label in Dispute Table'] = 'Not Showing'


        # Verify the Dispute Table Column Labels (Team)
        elements = self.__ctx.driver.find_elements("xpath", adhadjlocators.TBL_TEAM_LBL)
        if elements:
            element = elements[0]
            act_teamlbl = element.text
            
            # Compare actual_text with expected_text
            if act_teamlbl == exp_teamlbl:
                logger.info(f"Team Label in Dispute Table is showing and text matches: {act_teamlbl}")
                dispute_table['Team Label in Dispute Table'] = 'Showing'
            else:
                logger.info(f"Team Label is showing but text does not match. Actual: {act_teamlbl}, Expected: {exp_teamlbl}")
                dispute_table['Team Label in Dispute Table'] = 'Not Showing'
        else:
            logger.info("Team Label in Dispute Table is not showing")
            dispute_table['Team Label in Dispute Table'] = 'Not Showing'


        # Verify the Dispute Table Column Labels (Status)
        elements = self.__ctx.driver.find_elements("xpath", adhadjlocators.TBL_STAT_LBL)
        if elements:
            element = elements[0]
            act_statuslbl = element.text
            
            # Compare actual_text with expected_text
            if act_statuslbl == exp_statuslbl:
                logger.info(f"Status Label in Dispute Table is showing and text matches: {act_statuslbl}")
                dispute_table['Status Label in Dispute Table'] = 'Showing'
            else:
                logger.info(f"Status Label is showing but text does not match. Actual: {act_statuslbl}, Expected: {exp_statuslbl}")
                dispute_table['Status Label in Dispute Table'] = 'Not Showing'
        else:
            logger.info("Status Label in Dispute Table is not showing")
            dispute_table['Status Label in Dispute Table'] = 'Not Showing'



        # Verify the Dispute Table Column Labels (Reviewer)
        elements = self.__ctx.driver.find_elements("xpath", adhadjlocators.TBL_RVWR_LBL)
        if elements:
            element = elements[0]
            act_rvwrlbl = element.text
            
            # Compare actual_text with expected_text
            if act_rvwrlbl == exp_rvwrlbl:
                logger.info(f"Reviewer Label in Dispute Table is showing and text matches: {act_rvwrlbl}")
                dispute_table['Reviewer Label in Dispute Table'] = 'Showing'
            else:
                logger.info(f"Reviewer Label is showing but text does not match. Actual: {act_rvwrlbl}, Expected: {exp_rvwrlbl}")
                dispute_table['Reviewer Label in Dispute Table'] = 'Not Showing'
        else:
            logger.info("Reviewer Label in Dispute Table is not showing")
            dispute_table['Reviewer Label in Dispute Table'] = 'Not Showing'



        # Verify the Dispute Table Column Labels (Reviewed At)
        elements = self.__ctx.driver.find_elements("xpath", adhadjlocators.TBL_RVWDAT_LBL)
        if elements:
            element = elements[0]
            act_rvwdatlbl = element.text
            
            # Compare actual_text with expected_text
            if act_rvwdatlbl == exp_rvwdatlbl:
                logger.info(f"Reviewed At Label in Dispute Table is showing and text matches: {act_rvwdatlbl}")
                dispute_table['Reviewed At Label in Dispute Table'] = 'Showing'
            else:
                logger.info(f"Reviewed At Label is showing but text does not match. Actual: {act_rvwdatlbl}, Expected: {exp_rvwdatlbl}")
                dispute_table['Reviewed At Label in Dispute Table'] = 'Not Showing'
        else:
            logger.info("Reviewed At Label in Dispute Table is not showing")
            dispute_table['Reviewed At Label in Dispute Table'] = 'Not Showing'


        # Verify the Dispute Table Column Labels (Created)
        elements = self.__ctx.driver.find_elements("xpath", adhadjlocators.TBL_CRTD_LBL)
        if elements:
            element = elements[0]
            act_crtdlbl = element.text
            
            # Compare actual_text with expected_text
            if act_crtdlbl == exp_crtdlbl:
                logger.info(f"Created Label in Dispute Table is showing and text matches: {act_crtdlbl}")
                dispute_table['Created Label in Dispute Table'] = 'Showing'
            else:
                logger.info(f"Created Label is showing but text does not match. Actual: {act_crtdlbl}, Expected: {exp_crtdlbl}")
                dispute_table['Created Label in Dispute Table'] = 'Not Showing'
        else:
            logger.info("Created Label in Dispute Table is not showing")
            dispute_table['Created Label in Dispute Table'] = 'Not Showing'



        return dispute_table



# , exp_fltr_statplhdr: str, exp_fltr_gobtnlbl: str, exp_fltr_extoxlsbtnlbl: str):

    @keyword 
    def check_filter_section(self, exp_fltr_sdlbl: str, exp_fltr_sdplhdr: str, exp_fltr_edlbl: str, exp_fltr_edplhdr: str, exp_fltr_usersplhdr: str, exp_fltr_locplhdr: str, exp_fltr_teamspldhr: str, exp_fltr_posplhdr: str):
        logger.info(f"Check the Filter Section if fields, labels, and buttons are present")

        filter_section = {}

        # Verify the Start Date Label and Placeholder
        # Label

        elements = self.__ctx.driver.find_elements("xpath", adhadjlocators.FLTR_SD_LBL)
        if elements:
            element = elements[0]
            act_fltr_sdlbl = element.text
            
            if act_fltr_sdlbl == exp_fltr_sdlbl:
                logger.info(f"Start Date Label is showing and text matches: {act_fltr_sdlbl}")
                filter_section['Start Date Label'] = 'Showing'
            else:
                logger.info(f"Start Date Label is showing but text does not match. Actual: {act_fltr_sdlbl}, Expected: {exp_fltr_sdlbl}")
                filter_section['Start Date Label'] = 'Not Showing'
        else:
            logger.info("Start Date Label is not showing")
            filter_section['Start Date Label'] = 'Not Showing'


        # Placeholder

        input_element = self.__ctx.driver.find_element("xpath", adhadjlocators.FLTR_SD_INP)
        self.__ctx.driver.execute_script("arguments[0].click();", input_element)
        self.__ctx.wait_until_element_is_visible(locator=adhadjlocators.FLTR_SD_PLHDR)
        elements = self.__ctx.driver.find_elements("xpath", f"{adhadjlocators.FLTR_SD_PLHDR}")

        if elements:
            element = elements[0]

            act_fltr_sdplhdr = element.get_attribute("aria-label")
            # logger.info(f"Highlighted Date Aria-Label: {act_fltr_sdplhdr}") # For checking

            if act_fltr_sdplhdr == exp_fltr_sdplhdr:
                logger.info(f"Start Date Placeholder is showing and text matches: {act_fltr_sdplhdr}")
                filter_section['Start Date Placeholder'] = 'Showing'
            else:
                logger.info(f"Start Date Placeholder is showing but text does not match. Actual: {act_fltr_sdplhdr}, Expected: {exp_fltr_sdplhdr}")
                filter_section['Start Date Placeholder'] = 'Not Showing'
        else:
            logger.info("Start Date Placeholder is not showing")
            filter_section['Start Date Placeholder'] = 'Not Showing'


        # Verify the End Date Label and Placeholder
        # Label

        elements = self.__ctx.driver.find_elements("xpath", adhadjlocators.FLTR_ED_LBL)
        if elements:
            element = elements[0]
            act_fltr_edlbl = element.text
            
            if act_fltr_edlbl == exp_fltr_edlbl:
                logger.info(f"End Date Label is showing and text matches: {act_fltr_edlbl}")
                filter_section['End Date Label'] = 'Showing'
            else:
                logger.info(f"End Date Label is showing but text does not match. Actual: {act_fltr_edlbl}, Expected: {exp_fltr_edlbl}")
                filter_section['End Date Label'] = 'Not Showing'
        else:
            logger.info("End Date Label is not showing")
            filter_section['End Date Label'] = 'Not Showing'


        # Placeholder

        input_element = self.__ctx.driver.find_element("xpath", adhadjlocators.FLTR_ED_INP)
        self.__ctx.driver.execute_script("arguments[0].click();", input_element)
        self.__ctx.wait_until_element_is_visible(locator=adhadjlocators.FLTR_ED_PLHDR)
        elements = self.__ctx.driver.find_elements("xpath", f"{adhadjlocators.FLTR_ED_PLHDR}")

        if elements:
            element = elements[0]

            act_fltr_edplhdr = element.get_attribute("aria-label")
            # logger.info(f"Highlighted Date Aria-Label: {act_fltr_edplhdr}") # For checking

            if act_fltr_edplhdr == exp_fltr_edplhdr:
                logger.info(f"End Date Placeholder is showing and text matches: {act_fltr_edplhdr}")
                filter_section['End Date Placeholder'] = 'Showing'
            else:
                logger.info(f"End Date Placeholder is showing but text does not match. Actual: {act_fltr_edplhdr}, Expected: {exp_fltr_edplhdr}")
                filter_section['End Date Placeholder'] = 'Not Showing'
        else:
            logger.info("End Date Placeholder is not showing")
            filter_section['End Date Placeholder'] = 'Not Showing'



        # Verify the Users Placeholder

        elements = self.__ctx.driver.find_elements("xpath", adhadjlocators.FLTR_USERS_PLHDR(user=exp_fltr_usersplhdr))
        if elements:
            element = elements[0]

            act_fltr_usersplhdr = element.get_attribute("title")
            # logger.info(f"Title: {act_fltr_usersplhdr}")  # For checking

            if act_fltr_usersplhdr == exp_fltr_usersplhdr:
                logger.info(f"User/s Placeholder is showing and text matches: {act_fltr_usersplhdr}")
                filter_section['User/s Placeholder'] = 'Showing'
            else:
                logger.info(f"User/s Placeholder is showing but text does not match. Actual: {act_fltr_usersplhdr}, Expected: {exp_fltr_usersplhdr}")
                filter_section['User/s Placeholder'] = 'Not Showing'
        else:
            logger.info("User/s Placeholder is not showing")
            filter_section['User/s Placeholder'] = 'Not Showing'



        # Verify the Locations Placeholder

        elements = self.__ctx.driver.find_elements("xpath", adhadjlocators.FLTR_LOC_PLHDR(loc=exp_fltr_locplhdr))
        if elements:
            element = elements[0]

            act_fltr_locplhdr = element.get_attribute("title")
            # logger.info(f"Location: {act_fltr_locplhdr}")  # For checking

            if act_fltr_locplhdr == exp_fltr_locplhdr:
                logger.info(f"Location Placeholder is showing and text matches: {act_fltr_locplhdr}")
                filter_section['Location Placeholder'] = 'Showing'
            else:
                logger.info(f"Location Placeholder is showing but text does not match. Actual: {act_fltr_locplhdr}, Expected: {exp_fltr_locplhdr}")
                filter_section['Location Placeholder'] = 'Not Showing'
        else:
            logger.info("Location Placeholder is not showing")
            filter_section['Location Placeholder'] = 'Not Showing'



        # Verify the Teams Placeholder

        elements = self.__ctx.driver.find_elements("xpath", adhadjlocators.FLTR_TEAM_PLHDR(team=exp_fltr_teamspldhr))
        if elements:
            element = elements[0]

            act_fltr_teamspldhr = element.get_attribute("title")
            logger.info(f"Team: {act_fltr_teamspldhr}")  # For checking

            if act_fltr_teamspldhr == exp_fltr_teamspldhr:
                logger.info(f"Team Placeholder is showing and text matches: {act_fltr_teamspldhr}")
                filter_section['Team Placeholder'] = 'Showing'
            else:
                logger.info(f"Team Placeholder is showing but text does not match. Actual: {act_fltr_teamspldhr}, Expected: {exp_fltr_teamspldhr}")
                filter_section['Team Placeholder'] = 'Not Showing'
        else:
            logger.info("Team Placeholder is not showing")
            filter_section['Team Placeholder'] = 'Not Showing'



        # Verify the Positions Placeholder

        elements = self.__ctx.driver.find_elements("xpath", adhadjlocators.FLTR_POST_PLHDR(position=exp_fltr_posplhdr))
        if elements:
            element = elements[0]

            act_fltr_posplhdr = element.get_attribute("title")
            logger.info(f"Position: {act_fltr_posplhdr}")  # For checking

            if act_fltr_posplhdr == exp_fltr_posplhdr:
                logger.info(f"Position Placeholder is showing and text matches: {act_fltr_posplhdr}")
                filter_section['Position Placeholder'] = 'Showing'
            else:
                logger.info(f"Position Placeholder is showing but text does not match. Actual: {act_fltr_posplhdr}, Expected: {exp_fltr_posplhdr}")
                filter_section['Position Placeholder'] = 'Not Showing'
        else:
            logger.info("Position Placeholder is not showing")
            filter_section['Position Placeholder'] = 'Not Showing'



        try:
            self.__ctx.scroll_element_into_view(adhadjlocators.FLTR_GO_BTN)
            if self.__ctx.find_element(adhadjlocators.FLTR_GO_BTN):
                logger.info("GO BUTTON is showing")
                filter_section['GO BUTTON LIST'] = 'Showing'
            else:
                logger.info("GO BUTTON is not showing")
                filter_section['GO BUTTON LIST'] = 'Not Showing'
        except Exception as e:
            logger.error("An error occurred:", str(e))
            filter_section['GO BUTTON LIST'] = 'Error'
        
        
        try:
            self.__ctx.scroll_element_into_view(adhadjlocators.FLTR_EXPRT_BTN)
            if self.__ctx.find_elements(adhadjlocators.FLTR_EXPRT_BTN):
                logger.info("Export to xls BUTTON is showing")
                filter_section['Export to xls BUTTON LIST'] = 'Showing'
            else:
                logger.info("Export to xls BUTTON is not showing")
                filter_section['Export to xls BUTTON LIST'] = 'Not Showing'
        except Exception as e:
            logger.error("An error occurred:", str(e))
            filter_section['Export to xls BUTTON LIST'] = 'Error'
        

        return filter_section




