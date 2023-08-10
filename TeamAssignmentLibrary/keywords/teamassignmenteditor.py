
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from robot.api import logger
from robot.api import TestSuite
import  time

from TeamAssignmentLibrary.locators import teamlocators


class TeamAssignmentEditor:
    
    def __init__(self, ctx: SeleniumLibrary) -> None:
        self.__ctx = ctx

    @keyword 
    def select_agent(self, agent_name: str, agent_uid: str):
        self.__ctx.wait_until_element_is_visible(locator=teamlocators.FREEAGENTSLIST)
        self.__ctx.click_element(locator=teamlocators.FREEAGENTSFLTR)
        self.__ctx.input_text(locator=teamlocators.FREEAGENTSFLTR, text=agent_name)  
        
        option_locator = self.get_option_value(agent_uid)
        self.__ctx.wait_until_element_is_visible(locator=option_locator)
        self.__ctx.click_element(locator=option_locator)
        selected = self.__ctx.get_element_attribute(locator=option_locator, attribute="selected")
        logger.info(f"{selected}")
        self.__ctx.click_button(locator=teamlocators.MOVESLCBTN)

    def get_option_value(self, agent_uid):
        option_locator = f"xpath://option[@value='{agent_uid}']"
        self.__ctx.find_element(option_locator)
        return option_locator
    

    @keyword 
    def unselect_agent(self, agent_uid: str):
        self.__ctx.wait_until_element_is_visible(locator=teamlocators.TEAMROSTERLIST)

        option_locator = self.get_option_value(agent_uid)
        self.__ctx.click_element(locator=option_locator)
        self.__ctx.click_button(locator=teamlocators.REMOVEALLBTN)

    def get_option_value(self, agent_uid):
        option_locator = f"xpath://option[@value='{agent_uid}']"
        self.__ctx.find_element(option_locator)
        return option_locator


    @keyword 
    def check_team_editor(self, exp_falbl: str, exp_trosterlbl: str, exp_fafltr: str, exp_rosfltr: str):
        logger.info(f"Check the Team Assignment Editor page if fields, labels, and buttons are present")

        team_assignment_content = {}
        
        elements = self.__ctx.driver.find_elements("xpath", teamlocators.FREEAGENTSLBL)
        if elements:
            element = elements[0]
            act_falbl = element.text
            
            # Compare actual_text with expected_text
            if act_falbl == exp_falbl:
                logger.info(f"FREE AGENTS Label is showing and text matches: {act_falbl}")
                team_assignment_content['Free Agents Label'] = 'Showing'
            else:
                logger.info(f"FREE AGENTS Label is showing but text does not match. Actual: {act_falbl}, Expected: {exp_falbl}")
                team_assignment_content['Free Agents Label'] = 'Not Showing'
        else:
            logger.info("FREE AGENTS Label is not showing")
            team_assignment_content['Free Agents Label'] = 'Not Showing'
        


        elements = self.__ctx.driver.find_elements("xpath", teamlocators.TEAMROSTERLBL)
        if elements:
            element = elements[0]
            act_trosterlbl = element.text
            
            # Compare actual_text with expected_text
            if act_trosterlbl == exp_trosterlbl:
                logger.info(f"TEAM ROSTER Label is showing and text matches: {act_trosterlbl}")
                team_assignment_content['TEAM ROSTER Label'] = 'Showing'
            else:
                logger.info(f"TEAM ROSTER Label is showing but text does not match. Actual: {act_trosterlbl}, Expected: {exp_trosterlbl}")
                team_assignment_content['TEAM ROSTER Label'] = 'Not Showing'
        else:
            logger.info("TEAM ROSTER Label is not showing")
            team_assignment_content['TEAM ROSTER Label'] = 'Not Showing'
            
        

        elements = self.__ctx.driver.find_elements("xpath", teamlocators.FREEAGENTSFLTR)
        if elements:
            element = elements[0]
            
            # Retrieve the "placeholder" attribute value
            act_fafltr_placeholder = element.get_attribute("placeholder")
            
            # Compare the placeholder attribute value with the expected value
            if act_fafltr_placeholder == exp_fafltr:
                logger.info(f"FREE AGENTS Filter is showing and placeholder matches: {act_fafltr_placeholder}")
                team_assignment_content['FREE AGENTS Filter'] = 'Showing'
            else:
                logger.info(f"FREE AGENTS Filter is showing but placeholder does not match. Actual: {act_fafltr_placeholder}, Expected: {exp_fafltr}")
                team_assignment_content['FREE AGENTS Filter'] = 'Not Showing'
        else:
            logger.info("FREE AGENTS Filter is not showing")
            team_assignment_content['FREE AGENTS Filter'] = 'Not Showing'



        elements = self.__ctx.driver.find_elements("xpath", teamlocators.TEAMROSTERFLTR)
        if elements:
            element = elements[0]
            
            # Retrieve the "placeholder" attribute value
            act_rosfltr_placeholder = element.get_attribute("placeholder")
            
            # Compare the placeholder attribute value with the expected value
            if act_rosfltr_placeholder == exp_rosfltr:
                logger.info(f"TEAM ROSTER Filter is showing and placeholder matches: {act_rosfltr_placeholder}")
                team_assignment_content['TEAM ROSTER Filter'] = 'Showing'
            else:
                logger.info(f"TEAM ROSTER Filter is showing but placeholder does not match. Actual: {act_rosfltr_placeholder}, Expected: {exp_rosfltr}")
                team_assignment_content['TEAM ROSTER Filter'] = 'Not Showing'
        else:
            logger.info("TEAM ROSTER Filter is not showing")
            team_assignment_content['TEAM ROSTER Filter'] = 'Not Showing'



        if self.__ctx.driver.find_elements("xpath", teamlocators.MOVESLCBTN):
            logger.info("MOVE SELECTED Button is showing")
            team_assignment_content['MOVE SELECTED Button'] = 'Showing'
        else:
            logger.info("MOVE SELECTED Button is not showing")
            team_assignment_content['MOVE SELECTED Button'] = 'Not Showing'



        if self.__ctx.driver.find_elements("xpath", teamlocators.MOVEALLBTN):
            logger.info("MOVE ALL Button is showing")
            team_assignment_content['MOVE ALL Button'] = 'Showing'
        else:
            logger.info("MOVE ALL Button is not showing")
            team_assignment_content['MOVE ALL Button'] = 'Not Showing'



        if self.__ctx.driver.find_elements("xpath", teamlocators.REMOVESLCBTN):
            logger.info("REMOVE SELECTED Button is showing")
            team_assignment_content['REMOVE SELECTED Button'] = 'Showing'
        else:
            logger.info("REMOVE SELECTED Button is not showing")
            team_assignment_content['REMOVE SELECTED Button'] = 'Not Showing'



        if self.__ctx.driver.find_elements("xpath", teamlocators.REMOVEALLBTN):
            logger.info("REMOVE ALL Button is showing")
            team_assignment_content['REMOVE ALL Button'] = 'Showing'
        else:
            logger.info("REMOVE ALL Button is not showing")
            team_assignment_content['REMOVE ALL Button'] = 'Not Showing'



        if self.__ctx.driver.find_elements("xpath", teamlocators.FREEAGENTSLIST):
            logger.info("FREE AGENT LIST is showing")
            team_assignment_content['FREE AGENT LIST'] = 'Showing'
        else:
            logger.info("FREE AGENT LIST is not showing")
            team_assignment_content['FREE AGENT LIST'] = 'Not Showing'

        
        if self.__ctx.driver.find_elements("xpath", teamlocators.TEAMROSTERLIST):
            logger.info("TEAM AGENT LIST is showing")
            team_assignment_content['TEAM AGENT LIST'] = 'Showing'
        else:
            logger.info("TEAM AGENT LIST is not showing")
            team_assignment_content['TEAM AGENT LIST'] = 'Not Showing'


        # if self.__ctx.driver.find_elements("xpath", teamlocators.SAVEBTN):
        #     logger.info("SAVE BUTTON is showing")
        #     team_assignment_content['SAVE BUTTON LIST'] = 'Showing'
        # else:
        #     logger.info("SAVE BUTTON LIST is not showing")
        #     team_assignment_content['SAVE BUTTON LIST'] = 'Not Showing'


        try:
            self.__ctx.scroll_element_into_view(teamlocators.SAVEBTN)
            if self.__ctx.find_element(teamlocators.SAVEBTN):
                logger.info("SAVE BUTTON is showing")
                team_assignment_content['SAVE BUTTON LIST'] = 'Showing'
            else:
                logger.info("SAVE BUTTON is not showing")
                team_assignment_content['SAVE BUTTON LIST'] = 'Not Showing'
        except Exception as e:
            logger.error("An error occurred:", str(e))
            team_assignment_content['SAVE BUTTON LIST'] = 'Error'
        
        time.sleep(5)


        try:
            self.__ctx.scroll_element_into_view(teamlocators.CANCELBTN)
            if self.__ctx.find_elements(teamlocators.CANCELBTN):
                logger.info("CANCEL BUTTON is showing")
                team_assignment_content['CANCEL BUTTON LIST'] = 'Showing'
            else:
                logger.info("CANCEL BUTTON is not showing")
                team_assignment_content['CANCEL BUTTON LIST'] = 'Not Showing'
        except Exception as e:
            logger.error("An error occurred:", str(e))
            team_assignment_content['CANCEL BUTTON LIST'] = 'Error'
        


        return team_assignment_content
















        # if self.__ctx.driver.find_elements("xpath", teamlocators.FREEAGENTSFLTR):
        #     logger.info("FREE AGENTS Filter is showing")
        #     team_assignment_content['Free Agents Filter'] = 'Showing'
        # else:
        #     logger.info("FREE AGENTS Filter is not showing")
        #     team_assignment_content['Free Agents Filter'] = 'Not Showing'












        
        # Return the dictionary containing the results of element checks













        
        
        # You can perform similar checks for other elements
        
        # Return the dictionary containing the results of element checks
        return team_assignment_content





