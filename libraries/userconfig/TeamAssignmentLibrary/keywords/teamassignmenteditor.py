
from libraries.userconfig.TeamAssignmentLibrary.locators import teamlocators
from autocore.bases import WebLibraryComponent 
from robot.api.deco import keyword

# from SeleniumLibrary import SeleniumLibrary
# from robot.api import logger
# import  time


class TeamAssignmentEditor(WebLibraryComponent):
    
    # def __init__(self, ctx: SeleniumLibrary) -> None:
    #     self.__ctx = ctx

    @keyword 
    def select_agent(self, agent_name: str, agent_uid: str):
        self.web.se_lib.wait_until_element_is_visible(locator=teamlocators.FREEAGENTSLIST)
        self.web.se_lib.click_element(locator=teamlocators.FREEAGENTSFLTR)
        self.web.input_text(locator=teamlocators.FREEAGENTSFLTR, text=agent_name)  
        
        option_locator = self.get_option_value(agent_uid)
        self.web.se_lib.wait_until_element_is_visible(locator=option_locator)
        self.web.se_lib.click_element(locator=option_locator)
        selected = self.web.se_lib.get_element_attribute(locator=option_locator, attribute="selected")
        self.logger.info(f"{selected}")
        self.web.se_lib.click_button(locator=teamlocators.MOVESLCBTN)

    def get_option_value(self, agent_uid):
        option_locator = f"xpath://option[@value='{agent_uid}']"
        self.web.find_element(option_locator)
        return option_locator
    

    @keyword 
    def unselect_agent(self, agent_uid: str):
        self.web.se_lib.wait_until_element_is_visible(locator=teamlocators.TEAMROSTERLIST)

        option_locator = self.get_option_value(agent_uid)
        self.web.se_lib.click_element(locator=option_locator)
        self.web.se_lib.click_button(locator=teamlocators.REMOVEALLBTN)

    def get_option_value(self, agent_uid):
        option_locator = f"xpath://option[@value='{agent_uid}']"
        self.web.se_lib.find_element(option_locator)
        return option_locator


    @keyword 
    def check_team_editor(self, exp_tnamelbl: str, exp_tleadlbl: str, exp_tloclbl: str, exp_falbl: str, exp_trosterlbl: str, exp_fafltr: str, exp_rosfltr: str):
        self.logger.info(f"Check the Team Assignment Editor page if fields, labels, and buttons are present")

        team_assignment_content = {}
        
        
        elements = self.web.se_lib.driver.find_elements("xpath", teamlocators.TNAMELBL)
        if elements:
            element = elements[0]
            act_tnamelbl = element.text
            
            # Compare actual_text with expected_text
            if act_tnamelbl == exp_tnamelbl:
                self.logger.info(f"Team Name Label is showing and text matches: {act_tnamelbl}")
                team_assignment_content['Team Name Label'] = 'Showing'
            else:
                self.logger.info(f"Team Name Label is showing but text does not match. Actual: {act_tnamelbl}, Expected: {exp_tnamelbl}")
                team_assignment_content['Team Name Label'] = 'Not Showing'
        else:
            self.logger.info("Team Name Label is not showing")
            team_assignment_content['Team Name Label'] = 'Not Showing'
        

        elements = self.web.se_lib.driver.find_elements("xpath", teamlocators.TLEADLBL)
        if elements:
            element = elements[0]
            act_tleadlbl = element.text
            
            # Compare actual_text with expected_text
            if act_tleadlbl == exp_tleadlbl:
                self.logger.info(f"Team Lead Label is showing and text matches: {act_tleadlbl}")
                team_assignment_content['Team Lead Label'] = 'Showing'
            else:
                self.logger.info(f"Team Lead Label is showing but text does not match. Actual: {act_tleadlbl}, Expected: {exp_tleadlbl}")
                team_assignment_content['Team Lead Label'] = 'Not Showing'
        else:
            self.logger.info("Team Lead Label is not showing")
            team_assignment_content['Team Lead Label'] = 'Not Showing'       


        elements = self.web.se_lib.driver.find_elements("xpath", teamlocators.TLOCLBL)
        if elements:
            element = elements[0]
            act_tloclbl = element.text
            
            # Compare actual_text with expected_text
            if act_tloclbl == exp_tloclbl:
                self.logger.info(f"Team Location Label is showing and text matches: {act_tloclbl}")
                team_assignment_content['Team Location Label'] = 'Showing'
            else:
                self.logger.info(f"Team Location Label is showing but text does not match. Actual: {act_tloclbl}, Expected: {exp_tloclbl}")
                team_assignment_content['Team Location Label'] = 'Not Showing'
        else:
            self.logger.info("Team Location Label is not showing")
            team_assignment_content['Team Location Label'] = 'Not Showing' 
        
        
        
        elements = self.web.se_lib.driver.find_elements("xpath", teamlocators.FREEAGENTSLBL)
        if elements:
            element = elements[0]
            act_falbl = element.text
            
            # Compare actual_text with expected_text
            if act_falbl == exp_falbl:
                self.logger.info(f"FREE AGENTS Label is showing and text matches: {act_falbl}")
                team_assignment_content['Free Agents Label'] = 'Showing'
            else:
                self.logger.info(f"FREE AGENTS Label is showing but text does not match. Actual: {act_falbl}, Expected: {exp_falbl}")
                team_assignment_content['Free Agents Label'] = 'Not Showing'
        else:
            self.logger.info("FREE AGENTS Label is not showing")
            team_assignment_content['Free Agents Label'] = 'Not Showing'
        


        elements = self.web.se_lib.driver.find_elements("xpath", teamlocators.TEAMROSTERLBL)
        if elements:
            element = elements[0]
            act_trosterlbl = element.text
            
            # Compare actual_text with expected_text
            if act_trosterlbl == exp_trosterlbl:
                self.logger.info(f"TEAM ROSTER Label is showing and text matches: {act_trosterlbl}")
                team_assignment_content['TEAM ROSTER Label'] = 'Showing'
            else:
                self.logger.info(f"TEAM ROSTER Label is showing but text does not match. Actual: {act_trosterlbl}, Expected: {exp_trosterlbl}")
                team_assignment_content['TEAM ROSTER Label'] = 'Not Showing'
        else:
            self.logger.info("TEAM ROSTER Label is not showing")
            team_assignment_content['TEAM ROSTER Label'] = 'Not Showing'
            
        

        elements = self.web.se_lib.driver.find_elements("xpath", teamlocators.FREEAGENTSFLTR)
        if elements:
            element = elements[0]
            
            # Retrieve the "placeholder" attribute value
            act_fafltr_placeholder = element.get_attribute("placeholder")
            
            # Compare the placeholder attribute value with the expected value
            if act_fafltr_placeholder == exp_fafltr:
                self.logger.info(f"FREE AGENTS Filter is showing and placeholder matches: {act_fafltr_placeholder}")
                team_assignment_content['FREE AGENTS Filter'] = 'Showing'
            else:
                self.logger.info(f"FREE AGENTS Filter is showing but placeholder does not match. Actual: {act_fafltr_placeholder}, Expected: {exp_fafltr}")
                team_assignment_content['FREE AGENTS Filter'] = 'Not Showing'
        else:
            self.logger.info("FREE AGENTS Filter is not showing")
            team_assignment_content['FREE AGENTS Filter'] = 'Not Showing'



        elements = self.web.se_lib.driver.find_elements("xpath", teamlocators.TEAMROSTERFLTR)
        if elements:
            element = elements[0]
            
            # Retrieve the "placeholder" attribute value
            act_rosfltr_placeholder = element.get_attribute("placeholder")
            
            # Compare the placeholder attribute value with the expected value
            if act_rosfltr_placeholder == exp_rosfltr:
                self.logger.info(f"TEAM ROSTER Filter is showing and placeholder matches: {act_rosfltr_placeholder}")
                team_assignment_content['TEAM ROSTER Filter'] = 'Showing'
            else:
                self.logger.info(f"TEAM ROSTER Filter is showing but placeholder does not match. Actual: {act_rosfltr_placeholder}, Expected: {exp_rosfltr}")
                team_assignment_content['TEAM ROSTER Filter'] = 'Not Showing'
        else:
            self.logger.info("TEAM ROSTER Filter is not showing")
            team_assignment_content['TEAM ROSTER Filter'] = 'Not Showing'



        if self.web.se_lib.driver.find_elements("xpath", teamlocators.MOVESLCBTN):
            self.logger.info("MOVE SELECTED Button is showing")
            team_assignment_content['MOVE SELECTED Button'] = 'Showing'
        else:
            self.logger.info("MOVE SELECTED Button is not showing")
            team_assignment_content['MOVE SELECTED Button'] = 'Not Showing'



        if self.web.se_lib.driver.find_elements("xpath", teamlocators.MOVEALLBTN):
            self.logger.info("MOVE ALL Button is showing")
            team_assignment_content['MOVE ALL Button'] = 'Showing'
        else:
            self.logger.info("MOVE ALL Button is not showing")
            team_assignment_content['MOVE ALL Button'] = 'Not Showing'



        if self.web.se_lib.driver.find_elements("xpath", teamlocators.REMOVESLCBTN):
            self.logger.info("REMOVE SELECTED Button is showing")
            team_assignment_content['REMOVE SELECTED Button'] = 'Showing'
        else:
            self.logger.info("REMOVE SELECTED Button is not showing")
            team_assignment_content['REMOVE SELECTED Button'] = 'Not Showing'



        if self.web.se_lib.driver.find_elements("xpath", teamlocators.REMOVEALLBTN):
            self.logger.info("REMOVE ALL Button is showing")
            team_assignment_content['REMOVE ALL Button'] = 'Showing'
        else:
            self.logger.info("REMOVE ALL Button is not showing")
            team_assignment_content['REMOVE ALL Button'] = 'Not Showing'



        if self.web.se_lib.driver.find_elements("xpath", teamlocators.FREEAGENTSLIST):
            self.logger.info("FREE AGENT LIST is showing")
            team_assignment_content['FREE AGENT LIST'] = 'Showing'
        else:
            self.logger.info("FREE AGENT LIST is not showing")
            team_assignment_content['FREE AGENT LIST'] = 'Not Showing'

        

        if self.web.se_lib.driver.find_elements("xpath", teamlocators.TEAMROSTERLIST):
            self.logger.info("TEAM AGENT LIST is showing")
            team_assignment_content['TEAM AGENT LIST'] = 'Showing'
        else:
            self.logger.info("TEAM AGENT LIST is not showing")
            team_assignment_content['TEAM AGENT LIST'] = 'Not Showing'


        try:
            self.web.se_lib.scroll_element_into_view(teamlocators.SAVEBTN)
            if self.web.se_lib.find_element(teamlocators.SAVEBTN):
                self.logger.info("SAVE BUTTON is showing")
                team_assignment_content['SAVE BUTTON LIST'] = 'Showing'
            else:
                self.logger.info("SAVE BUTTON is not showing")
                team_assignment_content['SAVE BUTTON LIST'] = 'Not Showing'
        except Exception as e:
            self.logger.error("An error occurred:", str(e))
            team_assignment_content['SAVE BUTTON LIST'] = 'Error'
        
        
        try:
            self.web.se_lib.scroll_element_into_view(teamlocators.CANCELBTN)
            if self.web.find_elements(teamlocators.CANCELBTN):
                self.logger.info("CANCEL BUTTON is showing")
                team_assignment_content['CANCEL BUTTON LIST'] = 'Showing'
            else:
                self.logger.info("CANCEL BUTTON is not showing")
                team_assignment_content['CANCEL BUTTON LIST'] = 'Not Showing'
        except Exception as e:
            self.logger.error("An error occurred:", str(e))
            team_assignment_content['CANCEL BUTTON LIST'] = 'Error'
        

        return team_assignment_content
    


    @keyword 
    def check_reminder_section(self, exp_rmndrlbl: str, exp_alerttext: str):
        self.logger.info(f"Check the Reminder Section if fields, labels, and buttons are present")

        reminder_section = {}
  

        if self.web.se_lib.driver.find_elements("xpath", teamlocators.ALERT):
                self.logger.info("ALERT / REMINDER is showing")
                reminder_section['ALERT / REMINDER'] = 'Showing'
        else:
            self.logger.info("ALERT / REMINDER is not showing")
            reminder_section['ALERT / REMINDER'] = 'Not Showing'



        if self.web.se_lib.driver.find_elements("xpath", teamlocators.INFO_CIRCLE):
            self.logger.info("INFO ICON is showing")
            reminder_section['INFO ICON'] = 'Showing'
        else:
            self.logger.info("ALERT / REMINDER is not showing")
            reminder_section['INFO ICON'] = 'Not Showing'



        if self.web.se_lib.driver.find_elements("xpath", teamlocators.DISMISS_ALERT_BTN):
            self.logger.info("CLOSE BUTTON is showing")
            reminder_section['CLOSE BUTTON'] = 'Showing'
        else:
            self.logger.info("CLOSE BUTTON is not showing")
            reminder_section['CLOSE BUTTON'] = 'Not Showing'



        elements = self.web.se_lib.driver.find_elements("xpath", teamlocators.RMNDR)
        if elements:
            element = elements[0]
            
            div_text = element.text.strip()
          
            if div_text == exp_rmndrlbl:
                self.logger.info("REMINDER LABEL is showing and content matches")
                reminder_section['REMINDER LABEL'] = 'Showing'
            else:
                self.logger.info("REMINDER LABEL is showing but content does not match")
                reminder_section['REMINDER LABEL'] = 'Not Showing'
        else:
            self.logger.info("REMINDER LABEL is not showing")
            reminder_section['REMINDER LABEL'] = 'Not Showing'



        elements = self.web.se_lib.driver.find_elements("xpath", teamlocators.ALERTTEXT)
        if elements:
            element = elements[0]
            
            div_text = element.text.strip()
          
            if div_text == exp_alerttext:
                self.logger.info("REMINDER NOTICE is showing and content matches")
                reminder_section['REMINDER NOTICE'] = 'Showing'
            else:
                self.logger.info("REMINDER NOTICE is showing but content does not match")
                reminder_section['REMINDER NOTICE'] = 'Not Showing'
        else:
            self.logger.info("REMINDER NOTICE is not showing")
            reminder_section['REMINDER NOTICE'] = 'Not Showing'


        return reminder_section  

