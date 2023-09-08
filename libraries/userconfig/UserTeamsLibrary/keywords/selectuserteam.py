
from autocore.bases import WebLibraryComponent 
from libraries.userconfig.UserTeamsLibrary.locators import userteamslocators
from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

# from SeleniumLibrary import SeleniumLibrary


class SelectUserTeam(WebLibraryComponent):
    
    # def __init__(self, ctx: SeleniumLibrary) -> None:
    #     self.__ctx = ctx

    @keyword
    def search_and_click_next(self, team_name):
        driver = self.web.se_lib.driver

        self.web.se_lib.wait_until_element_is_visible(locator=userteamslocators.TEAMLIST)
        # self.web.se_lib.scroll_element_into_view(locator=userteamslocators.PAGE1BTN)
        # self.web.se_lib.click_element(locator=userteamslocators.PAGE1BTN)

        locator = userteamslocators.TEAMLIST
        team_locator = f"//tr[@data-name='{team_name}']"
        next_btn = userteamslocators.NEXTBTN

        while True:
            try:
                tr_element = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f"{locator}{team_locator}")
                    )
                )

                # Use ActionChains to move to the element and click it
                actions = ActionChains(driver)
                actions.move_to_element(tr_element).click().perform()

                print("Clicked on:", tr_element.text)
                break  # Exit the loop since the element was found and clicked
            except TimeoutException:
                # Scroll down the page
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                print("Element not found, scrolling down.")

                # Click on the "Next" button to load more content
                try:
                    next_link = WebDriverWait(driver, 2).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, f"{next_btn}")
                        )
                    )
                    next_link.click()
                    print("Clicked on 'Next' to load more content.")
                except TimeoutException:
                    print("Next link not found or clickable, exiting loop.")
                    break  # Exit the loop if Next link is not found or not clickable



    # @keyword
    # def search_and_click_next(self, team_name):
    #     driver = self.web.se_lib.driver

    #     self.web.se_lib.wait_until_element_is_visible(locator=userteamslocators.TEAMLIST)

    #     locator = userteamslocators.TEAMLIST
    #     team_locator = f"//tr[@data-name='{team_name}']"
    #     next_btn = userteamslocators.NEXTBTN
    #     prev_btn = userteamslocators.PREVBTN

    #     # 

    #     while True:
    #         try:
    #             tr_element = WebDriverWait(driver, 2).until(
    #                 EC.presence_of_element_located(
    #                     (By.XPATH, f"{locator}{team_locator}")
    #                 )
    #             )

    #             # Use ActionChains to move to the element and click it
    #             actions = ActionChains(driver)
    #             actions.move_to_element(tr_element).click().perform()

    #             print("Clicked on:", tr_element.text)
    #             break  # Exit the loop since the element was found and clicked
    #         except TimeoutException:
    #             # Scroll down the page
    #             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #             print("Element not found, scrolling down.")

    #             # Wait for the "Next" button to become clickable
    #             try:
    #                 next_link = WebDriverWait(driver, 5).until(
    #                     EC.element_to_be_clickable(
    #                         (By.XPATH, f"{next_btn}")
    #                     )
    #                 )

    #                 # Check if the "Next" button is disabled
    #                 if 'disabled' not in next_link.get_attribute('class'):
    #                     next_link.click()
    #                     print("Clicked on 'Next' to load more content.")
    #                 else:
    #                     print("Next link is disabled, trying 'Previous' button.")
    #                     try:
    #                         prev_link = WebDriverWait(driver, 5).until(
    #                             EC.element_to_be_clickable(
    #                                 (By.XPATH, f"{prev_btn}")
    #                             )
    #                         )
    #                         prev_link.click()
    #                         print("Clicked on 'Previous' to go back.")
    #                     except TimeoutException:
    #                         print("Previous link not found or clickable, exiting loop.")
    #                         break  # Exit the loop if neither Next nor Previous link is found or clickable
    #             except TimeoutException:
    #                 print("Next link not found or clickable, exiting loop.")
    #                 break  # Exit the loop if Next link is not found or not clickable