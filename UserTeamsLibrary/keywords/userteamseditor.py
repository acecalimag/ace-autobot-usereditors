
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from robot.api import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from UserTeamsLibrary.locators import userteamslocators


class UserTeamsEditor:
    
    def __init__(self, ctx: SeleniumLibrary) -> None:
        self.__ctx = ctx

    @keyword 
    def check_team_list_table(self, exp_tllbl: str, exp_namelbl: str, exp_leadlbl: str, exp_loclbl: str, exp_typelbl: str, exp_statuslbl: str, exp_lupdlbl: str):
        logger.info(f"Check the Team List Table if fields, labels, and buttons are present")

        team_list_table = {}

       
        # Verify the TEAM LIST Label
        elements = self.__ctx.driver.find_elements("xpath", userteamslocators.TEAM_LIST_LBL)
        if elements:
            element = elements[0]
            act_tllbl = element.text
            
            # Compare actual_text with expected_text
            if act_tllbl == exp_tllbl:
                logger.info(f"TEAM LIST Label is showing and text matches: {act_tllbl}")
                team_list_table['TEAM LIST Label'] = 'Showing'
            else:
                logger.info(f"TEAM LIST Label is showing but text does not match. Actual: {act_tllbl}, Expected: {exp_tllbl}")
                team_list_table['TEAM LIST Label'] = 'Not Showing'
        else:
            logger.info("TEAM LIST Label is not showing")
            team_list_table['TEAM LIST Label'] = 'Not Showing'


        # # Verify the TEAM LIST Table Column Labels (Name)
        # self.__ctx.scroll_element_into_view("xpath", userteamslocators.TBL_NAME_LBL)
        # elements = self.__ctx.driver.find_elements("xpath", userteamslocators.TBL_NAME_LBL)
        # if elements:
        #     element = elements[0]
        #     act_namelbl = element.text
            
        #     # Compare actual_text with expected_text
        #     if act_namelbl == exp_namelbl:
        #         logger.info(f"Name Label in Team List Table is showing and text matches: {act_namelbl}")
        #         team_list_table['Name Label in Team List Table'] = 'Showing'
        #     else:
        #         logger.info(f"Name Label is showing but text does not match. Actual: {act_namelbl}, Expected: {exp_namelbl}")
        #         team_list_table['Name Label in Team List Table'] = 'Not Showing'
        # else:
        #     logger.info("Name Label in Team List Table is not showing")
        #     team_list_table['Name Label in Team List Table'] = 'Not Showing'


        # Verify the TEAM LIST Table Column Labels (Name)
        element_locator = (By.XPATH, userteamslocators.TBL_NAME_LBL)
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
            act_namelbl = element.text

            # Compare actual_text with expected_text
            if act_namelbl == exp_namelbl:
                logger.info(f"Name Label in Team List Table is showing and text matches: {act_namelbl}")
                team_list_table['Name Label in Team List Table'] = 'Showing'
            else:
                logger.info(f"Name Label is showing but text does not match. Actual: {act_namelbl}, Expected: {exp_namelbl}")
                team_list_table['Name Label in Team List Table'] = 'Not Showing'
        else:
            logger.info("Name Label in Team List Table is not showing")
            team_list_table['Name Label in Team List Table'] = 'Not Showing'







        # Verify the TEAM LIST Table Column Labels (Team Lead)
        elements = self.__ctx.driver.find_elements("xpath", userteamslocators.TBL_TLEAD_LBL)
        if elements:
            element = elements[0]
            act_leadlbl = element.text
            
            # Compare actual_text with expected_text
            if act_leadlbl == exp_leadlbl:
                logger.info(f"Team Lead Label in Team List Table is showing and text matches: {act_leadlbl}")
                team_list_table['Team Lead Label in Team List Table'] = 'Showing'
            else:
                logger.info(f"Team Lead Label is showing but text does not match. Actual: {act_leadlbl}, Expected: {exp_leadlbl}")
                team_list_table['Team Lead Label in Team List Table'] = 'Not Showing'
        else:
            logger.info("Team Lead in Team List Table is not showing")
            team_list_table['Team Lead in Team List Table'] = 'Not Showing'


        # Verify the TEAM LIST Table Column Labels (Location)
        elements = self.__ctx.driver.find_elements("xpath", userteamslocators.TBL_TLOC_LBL)
        if elements:
            element = elements[0]
            act_loclbl = element.text
            
            # Compare actual_text with expected_text
            if act_loclbl == exp_loclbl:
                logger.info(f"Location Label in Team List Table is showing and text matches: {act_loclbl}")
                team_list_table['Location Label in Team List Table'] = 'Showing'
            else:
                logger.info(f"Location Label is showing but text does not match. Actual: {act_loclbl}, Expected: {exp_loclbl}")
                team_list_table['Location Label in Team List Table'] = 'Not Showing'
        else:
            logger.info("Location LABEL in Team List Table is not showing")
            team_list_table['Location Label in Team List Table'] = 'Not Showing'


        # Verify the TEAM LIST Table Column Labels (Type)
        elements = self.__ctx.driver.find_elements("xpath", userteamslocators.TBL_TTYPE_LBL)
        if elements:
            element = elements[0]
            act_typelbl = element.text
            
            # Compare actual_text with expected_text
            if act_typelbl == exp_typelbl:
                logger.info(f"Type Label in Team List Table is showing and text matches: {act_typelbl}")
                team_list_table['Type Label in Team List Table'] = 'Showing'
            else:
                logger.info(f"Type Label is showing but text does not match. Actual: {act_typelbl}, Expected: {exp_typelbl}")
                team_list_table['Type Label in Team List Table'] = 'Not Showing'
        else:
            logger.info("Type Label in Team List Table is not showing")
            team_list_table['Type Label in Team List Table'] = 'Not Showing'


        # Verify the TEAM LIST Table Column Labels (Status)
        elements = self.__ctx.driver.find_elements("xpath", userteamslocators.TBL_TSTAT_LBL)
        if elements:
            element = elements[0]
            act_statuslbl = element.text
            
            # Compare actual_text with expected_text
            if act_statuslbl == exp_statuslbl:
                logger.info(f"Status Label in Team List Table is showing and text matches: {act_statuslbl}")
                team_list_table['Status Label in Team List Table'] = 'Showing'
            else:
                logger.info(f"Status Label is showing but text does not match. Actual: {act_statuslbl}, Expected: {exp_statuslbl}")
                team_list_table['Status Label in Team List Table'] = 'Not Showing'
        else:
            logger.info("Status Label in Team List Table is not showing")
            team_list_table['Status Label in Team List Table'] = 'Not Showing'



        # Verify the TEAM LIST Table Column Labels (Last Updated)
        elements = self.__ctx.driver.find_elements("xpath", userteamslocators.TBL_TLUPD_LBL)
        if elements:
            element = elements[0]
            act_lupdlbl = element.text
            
            # Compare actual_text with expected_text
            if act_lupdlbl == exp_lupdlbl:
                logger.info(f"Last Updated Label in Team List Table is showing and text matches: {act_lupdlbl}")
                team_list_table['Last Updated Label in Team List Table'] = 'Showing'
            else:
                logger.info(f"Last Updated Label is showing but text does not match. Actual: {act_lupdlbl}, Expected: {exp_lupdlbl}")
                team_list_table['Last Updated Label in Team List Table'] = 'Not Showing'
        else:
            logger.info("Last Updated Label in Team List Table is not showing")
            team_list_table['Last Updated Label in Team List Table'] = 'Not Showing'



        return team_list_table





    @keyword 
    def check_view_update_section(self, exp_vulbl: str, exp_vu_namelbl: str, exp_vu_tdlbl: str, exp_vu_tllbl: str, exp_vu_loclbl: str, exp_vu_typelbl: str, exp_vu_statuslbl: str, exp_vu_lstupdlbl: str):
        logger.info(f"Check the View/Update Section if fields, labels, and buttons are present")

        view_update_section = {}

        # Verify the View/Update Label
        elements = self.__ctx.driver.find_elements("xpath", userteamslocators.VIEW_UPDATE_LBL)
        if elements:
            element = elements[0]
            act_vulbl = element.text
            
            # Compare actual_text with expected_text
            if act_vulbl == exp_vulbl:
                logger.info(f"View/Update Label is showing and text matches: {act_vulbl}")
                view_update_section['View/Update Label'] = 'Showing'
            else:
                logger.info(f"View/Update Label is showing but text does not match. Actual: {act_vulbl}, Expected: {exp_vulbl}")
                view_update_section['View/Update Label'] = 'Not Showing'
        else:
            logger.info("View/Update Label is not showing")
            view_update_section['View/Update Label'] = 'Not Showing'
        


        # Verify the View/Update Section Labels (Name)
        elements = self.__ctx.driver.find_elements("xpath", userteamslocators.VU_NAMELBL)
        if elements:
            element = elements[0]
            act_vu_namelbl = element.text
            
            # Compare actual_text with expected_text
            if act_vu_namelbl == exp_vu_namelbl:
                logger.info(f"Name Label in View/Update Section is showing and text matches: {act_vu_namelbl}")
                view_update_section['Name Label in View/Update Section'] = 'Showing'
            else:
                logger.info(f"Name Label in View/Update Section is showing but text does not match. Actual: {act_vu_namelbl}, Expected: {exp_vu_namelbl}")
                view_update_section['Name Label in View/Update Section'] = 'Not Showing'
        else:
            logger.info("Name Label in View/Update Section is not showing")
            view_update_section['Name Label in View/Update Section'] = 'Not Showing'



        # Verify the View/Update Section Labels (Description)
        elements = self.__ctx.driver.find_elements("xpath", userteamslocators.VU_TDLBL)
        if elements:
            element = elements[0]
            act_vu_tdlbl = element.text
            
            # Compare actual_text with expected_text
            if act_vu_tdlbl == exp_vu_tdlbl:
                logger.info(f"Description Label in View/Update Section is showing and text matches: {act_vu_tdlbl}")
                view_update_section['Description Label in View/Update Section'] = 'Showing'
            else:
                logger.info(f"Description Label in View/Update Section is showing but text does not match. Actual: {act_vu_tdlbl}, Expected: {exp_vu_tdlbl}")
                view_update_section['Description Label in View/Update Section'] = 'Not Showing'
        else:
            logger.info("Description Label in View/Update Section is not showing")
            view_update_section['Description Label in View/Update Section'] = 'Not Showing'


        # Verify the View/Update Section Labels (Team Lead)
        elements = self.__ctx.driver.find_elements("xpath", userteamslocators.VU_TDLBL)
        if elements:
            element = elements[0]
            act_vu_tllbl = element.text
            
            # Compare actual_text with expected_text
            if act_vu_tllbl == exp_vu_tllbl:
                logger.info(f"Team Lead Label in View/Update Section is showing and text matches: {act_vu_tllbl}")
                view_update_section['Team Lead Label in View/Update Section'] = 'Showing'
            else:
                logger.info(f"Team Lead Label in View/Update Section is showing but text does not match. Actual: {act_vu_tllbl}, Expected: {exp_vu_tllbl}")
                view_update_section['Team Lead Label in View/Update Section'] = 'Not Showing'
        else:
            logger.info("Team Lead Label in View/Update Section is not showing")
            view_update_section['Team Lead Label in View/Update Section'] = 'Not Showing'


        # Verify the View/Update Section Labels (Location)
        elements = self.__ctx.driver.find_elements("xpath", userteamslocators.VU_LOCLBL)
        if elements:
            element = elements[0]
            act_vu_loclbl = element.text
            
            # Compare actual_text with expected_text
            if act_vu_loclbl == exp_vu_loclbl:
                logger.info(f"Location Label in View/Update Section is showing and text matches: {act_vu_loclbl}")
                view_update_section['Location Label in View/Update Section'] = 'Showing'
            else:
                logger.info(f"Location Label in View/Update Section is showing but text does not match. Actual: {act_vu_loclbl}, Expected: {exp_vu_loclbl}")
                view_update_section['Location Label in View/Update Section'] = 'Not Showing'
        else:
            logger.info("Location Label in View/Update Section is not showing")
            view_update_section['Location Label in View/Update Section'] = 'Not Showing'


        # Verify the View/Update Section Labels (Type)
        elements = self.__ctx.driver.find_elements("xpath", userteamslocators.VU_TYPELBL)
        if elements:
            element = elements[0]
            act_vu_typelbl = element.text
            
            # Compare actual_text with expected_text
            if act_vu_typelbl == exp_vu_typelbl:
                logger.info(f"Type Label in View/Update Section is showing and text matches: {act_vu_typelbl}")
                view_update_section['Type Label in View/Update Section'] = 'Showing'
            else:
                logger.info(f"Type Label in View/Update Section is showing but text does not match. Actual: {act_vu_typelbl}, Expected: {exp_vu_typelbl}")
                view_update_section['Type Label in View/Update Section'] = 'Not Showing'
        else:
            logger.info("Type Label in View/Update Section is not showing")
            view_update_section['Type Label in View/Update Section'] = 'Not Showing'


        # Verify the View/Update Section Labels (Status)
        elements = self.__ctx.driver.find_elements("xpath", userteamslocators.VU_STATUSLBL)
        if elements:
            element = elements[0]
            act_vu_statuslbl = element.text
            
            # Compare actual_text with expected_text
            if act_vu_statuslbl == exp_vu_statuslbl:
                logger.info(f"Status Label in View/Update Section is showing and text matches: {act_vu_statuslbl}")
                view_update_section['Status Label in View/Update Section'] = 'Showing'
            else:
                logger.info(f"Status Label in View/Update Section is showing but text does not match. Actual: {act_vu_statuslbl}, Expected: {exp_vu_statuslbl}")
                view_update_section['Status Label in View/Update Section'] = 'Not Showing'
        else:
            logger.info("Status Label in View/Update Section is not showing")
            view_update_section['Status Label in View/Update Section'] = 'Not Showing'        


        # Verify the View/Update Section Labels (Last Updated)
        elements = self.__ctx.driver.find_elements("xpath", userteamslocators.VU_LSTUPDLBL)
        if elements:
            element = elements[0]
            act_vu_lstupdlbl = element.text
            
            # Compare actual_text with expected_text
            if act_vu_lstupdlbl == exp_vu_lstupdlbl:
                logger.info(f"Last Updated Label in View/Update Section is showing and text matches: {act_vu_lstupdlbl}")
                view_update_section['Last Updated Label in View/Update Section'] = 'Showing'
            else:
                logger.info(f"Last Updated Label in View/Update Section is showing but text does not match. Actual: {act_vu_lstupdlbl}, Expected: {exp_vu_lstupdlbl}")
                view_update_section['Last Updated Label in View/Update Section'] = 'Not Showing'
        else:
            logger.info("Last Updated Label in View/Update Section is not showing")
            view_update_section['Last Updated Label in View/Update Section'] = 'Not Showing' 


        # Verify Save Button is showing
        try:
            self.__ctx.scroll_element_into_view(userteamslocators.SAVEBTN)
            if self.__ctx.find_element(userteamslocators.SAVEBTN):
                logger.info("SAVE BUTTON is showing")
                view_update_section['SAVE BUTTON LIST'] = 'Showing'
            else:
                logger.info("SAVE BUTTON is not showing")
                view_update_section['SAVE BUTTON LIST'] = 'Not Showing'
        except Exception as e:
            logger.error("An error occurred:", str(e))
            view_update_section['SAVE BUTTON LIST'] = 'Error'
        

        # Verify Cancel Button is showing        
        try:
            self.__ctx.scroll_element_into_view(userteamslocators.CANCELBTN)
            if self.__ctx.find_elements(userteamslocators.CANCELBTN):
                logger.info("CANCEL BUTTON is showing")
                view_update_section['CANCEL BUTTON LIST'] = 'Showing'
            else:
                logger.info("CANCEL BUTTON is not showing")
                view_update_section['CANCEL BUTTON LIST'] = 'Not Showing'
        except Exception as e:
            logger.error("An error occurred:", str(e))
            view_update_section['CANCEL BUTTON LIST'] = 'Error' 


        return view_update_section

  