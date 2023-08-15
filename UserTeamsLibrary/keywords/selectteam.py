 
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UserTeamsLibrary.locators import userteamslocators
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SelectTeam:
    
    def __init__(self, ctx: SeleniumLibrary) -> None:
        self.__ctx = ctx
        

    @keyword
    def search_and_click_next(self, team_name):
        driver = self.__ctx.driver  # Assuming self.__ctx.driver is the WebDriver instance

        self.__ctx.wait_until_element_is_visible(locator=userteamslocators.TEAMLIST)

        locator = userteamslocators.TEAMLIST
        team_locator = f"//tr[@data-name='{team_name}']"
        next_btn = userteamslocators.NEXTBTN

        while True:
            # Scroll down the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Check if the target tr element is present in the current page
            try:
                tr_element = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f"{locator}{team_locator}")
                    )
                )
                # Click on the found tr_element
                tr_element.click()
                print("Clicked on:", tr_element.text)
                break  # Exit the loop since the element was found and clicked
            except:
                # Element not found, click on the "Next" link
                try:
                    next_link = WebDriverWait(driver, 2).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, f"{next_btn}")
                        )
                    )
                    next_link.click()
                    print("Clicked on 'Next'")
                except:
                    print("Next link not found or clickable, exiting loop.")
                    break  # Exit the loop if Next link is not found or not clickable