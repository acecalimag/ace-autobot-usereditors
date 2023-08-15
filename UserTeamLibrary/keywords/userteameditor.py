
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from robot.api import logger
import  time

from UserTeamLibrary.locators import userteamlocators


class UserTeamEditor:
    
    def __init__(self, ctx: SeleniumLibrary) -> None:
        self.__ctx = ctx

    @keyword 
    def select_agent(self, agent_name: str, agent_uid: str):
        self.__ctx.wait_until_element_is_visible(locator=userteamlocators.FREEAGENTSLIST)
        self.__ctx.click_element(locator=userteamlocators.FREEAGENTSFLTR)
        self.__ctx.input_text(locator=userteamlocators.FREEAGENTSFLTR, text=agent_name)  
        
        option_locator = self.get_option_value(agent_uid)
        self.__ctx.wait_until_element_is_visible(locator=option_locator)
        self.__ctx.click_element(locator=option_locator)
        selected = self.__ctx.get_element_attribute(locator=option_locator, attribute="selected")
        logger.info(f"{selected}")
        self.__ctx.click_button(locator=userteamlocators.MOVESLCBTN)

    def get_option_value(self, agent_uid):
        option_locator = f"xpath://option[@value='{agent_uid}']"
        self.__ctx.find_element(option_locator)
        return option_locator
    

    @keyword 
    def unselect_agent(self, agent_uid: str):
        self.__ctx.wait_until_element_is_visible(locator=userteamlocators.TEAMROSTERLIST)

        option_locator = self.get_option_value(agent_uid)
        self.__ctx.click_element(locator=option_locator)
        self.__ctx.click_button(locator=userteamlocators.REMOVEALLBTN)

    def get_option_value(self, agent_uid):
        option_locator = f"xpath://option[@value='{agent_uid}']"
        self.__ctx.find_element(option_locator)
        return option_locator


    @keyword 
    def check_team_editor(self, exp_falbl: str, exp_trosterlbl: str, exp_fafltr: str, exp_rosfltr: str, exp_rmndrlbl: str, exp_alerttext: str):
        logger.info(f"Check the Team Assignment Editor page if fields, labels, and buttons are present")

        team_assignment_content = {}
        
        elements = self.__ctx.driver.find_elements("xpath", userteamlocators.FREEAGENTSLBL)
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
        


        elements = self.__ctx.driver.find_elements("xpath", userteamlocators.TEAMROSTERLBL)
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
            
        

        elements = self.__ctx.driver.find_elements("xpath", userteamlocators.FREEAGENTSFLTR)
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



        elements = self.__ctx.driver.find_elements("xpath", userteamlocators.TEAMROSTERFLTR)
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



        if self.__ctx.driver.find_elements("xpath", userteamlocators.MOVESLCBTN):
            logger.info("MOVE SELECTED Button is showing")
            team_assignment_content['MOVE SELECTED Button'] = 'Showing'
        else:
            logger.info("MOVE SELECTED Button is not showing")
            team_assignment_content['MOVE SELECTED Button'] = 'Not Showing'



        if self.__ctx.driver.find_elements("xpath", userteamlocators.MOVEALLBTN):
            logger.info("MOVE ALL Button is showing")
            team_assignment_content['MOVE ALL Button'] = 'Showing'
        else:
            logger.info("MOVE ALL Button is not showing")
            team_assignment_content['MOVE ALL Button'] = 'Not Showing'



        if self.__ctx.driver.find_elements("xpath", userteamlocators.REMOVESLCBTN):
            logger.info("REMOVE SELECTED Button is showing")
            team_assignment_content['REMOVE SELECTED Button'] = 'Showing'
        else:
            logger.info("REMOVE SELECTED Button is not showing")
            team_assignment_content['REMOVE SELECTED Button'] = 'Not Showing'



        if self.__ctx.driver.find_elements("xpath", userteamlocators.REMOVEALLBTN):
            logger.info("REMOVE ALL Button is showing")
            team_assignment_content['REMOVE ALL Button'] = 'Showing'
        else:
            logger.info("REMOVE ALL Button is not showing")
            team_assignment_content['REMOVE ALL Button'] = 'Not Showing'



        if self.__ctx.driver.find_elements("xpath", userteamlocators.FREEAGENTSLIST):
            logger.info("FREE AGENT LIST is showing")
            team_assignment_content['FREE AGENT LIST'] = 'Showing'
        else:
            logger.info("FREE AGENT LIST is not showing")
            team_assignment_content['FREE AGENT LIST'] = 'Not Showing'

        

        if self.__ctx.driver.find_elements("xpath", userteamlocators.TEAMROSTERLIST):
            logger.info("TEAM AGENT LIST is showing")
            team_assignment_content['TEAM AGENT LIST'] = 'Showing'
        else:
            logger.info("TEAM AGENT LIST is not showing")
            team_assignment_content['TEAM AGENT LIST'] = 'Not Showing'


        try:
            self.__ctx.scroll_element_into_view(userteamlocators.SAVEBTN)
            if self.__ctx.find_element(userteamlocators.SAVEBTN):
                logger.info("SAVE BUTTON is showing")
                team_assignment_content['SAVE BUTTON LIST'] = 'Showing'
            else:
                logger.info("SAVE BUTTON is not showing")
                team_assignment_content['SAVE BUTTON LIST'] = 'Not Showing'
        except Exception as e:
            logger.error("An error occurred:", str(e))
            team_assignment_content['SAVE BUTTON LIST'] = 'Error'
        
        
        try:
            self.__ctx.scroll_element_into_view(userteamlocators.CANCELBTN)
            if self.__ctx.find_elements(userteamlocators.CANCELBTN):
                logger.info("CANCEL BUTTON is showing")
                team_assignment_content['CANCEL BUTTON LIST'] = 'Showing'
            else:
                logger.info("CANCEL BUTTON is not showing")
                team_assignment_content['CANCEL BUTTON LIST'] = 'Not Showing'
        except Exception as e:
            logger.error("An error occurred:", str(e))
            team_assignment_content['CANCEL BUTTON LIST'] = 'Error'
        


        if self.__ctx.driver.find_elements("xpath", userteamlocators.ALERT):
            logger.info("ALERT / REMINDER is showing")
            team_assignment_content['ALERT / REMINDER'] = 'Showing'
        else:
            logger.info("ALERT / REMINDER is not showing")
            team_assignment_content['ALERT / REMINDER'] = 'Not Showing'



        if self.__ctx.driver.find_elements("xpath", userteamlocators.INFO_CIRCLE):
            logger.info("INFO ICON is showing")
            team_assignment_content['INFO ICON'] = 'Showing'
        else:
            logger.info("ALERT / REMINDER is not showing")
            team_assignment_content['INFO ICON'] = 'Not Showing'



        if self.__ctx.driver.find_elements("xpath", userteamlocators.DISMISS_ALERT_BTN):
            logger.info("CLOSE BUTTON is showing")
            team_assignment_content['CLOSE BUTTON'] = 'Showing'
        else:
            logger.info("CLOSE BUTTON is not showing")
            team_assignment_content['CLOSE BUTTON'] = 'Not Showing'



        elements = self.__ctx.driver.find_elements("xpath", userteamlocators.RMNDR)
        if elements:
            element = elements[0]
            
            div_text = element.text.strip()
          
            if div_text == exp_rmndrlbl:
                logger.info("REMINDER LABEL is showing and content matches")
                team_assignment_content['REMINDER LABEL'] = 'Showing'
            else:
                logger.info("REMINDER LABEL is showing but content does not match")
                team_assignment_content['REMINDER LABEL'] = 'Not Showing'
        else:
            logger.info("REMINDER LABEL is not showing")
            team_assignment_content['REMINDER LABEL'] = 'Not Showing'



        elements = self.__ctx.driver.find_elements("xpath", userteamlocators.ALERTTEXT)
        if elements:
            element = elements[0]
            
            div_text = element.text.strip()
          
            if div_text == exp_alerttext:
                logger.info("REMINDER NOTICE is showing and content matches")
                team_assignment_content['REMINDER NOTICE'] = 'Showing'
            else:
                logger.info("REMINDER NOTICE is showing but content does not match")
                team_assignment_content['REMINDER NOTICE'] = 'Not Showing'
        else:
            logger.info("REMINDER NOTICE is not showing")
            team_assignment_content['REMINDER NOTICE'] = 'Not Showing'



        return team_assignment_content