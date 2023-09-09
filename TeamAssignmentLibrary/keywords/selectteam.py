 
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from TeamAssignmentLibrary.locators import teamlocators

class SelectTeam:
    
    def __init__(self, ctx: SeleniumLibrary) -> None:
        self.__ctx = ctx
        
    @keyword 
    def select_team(self, team_name: str):
        self.__ctx.wait_until_element_is_visible(locator=teamlocators.TEAMLIST)
        # self.__ctx.scroll_element_into_view(locator=teamlocators.TEAMLIST)
        
        # Combine the suggested scroll and click function here
        def scroll_to_element_and_click(driver, element_text):
            driver = self.__ctx.driver
            element = driver.find_element(By.XPATH, f"//td[text()='{element_text}']")
            driver.execute_script("arguments[0].scrollIntoView();", element)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//td[text()='{element_text}']"))).click()

        # Call the combined function with the provided team_name
        scroll_to_element_and_click(self.__ctx.driver, team_name)