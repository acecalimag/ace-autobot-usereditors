 
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AdherenceAdjustmentLibrary.locators import adhadjlocators
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from robot.api import logger
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time




class SelectDispute:
    
    def __init__(self, ctx: SeleniumLibrary) -> None:
        self.__ctx = ctx
        
    @keyword 
    def filter_select(self):
        logger.info(f"Modify the filters to select a dispute entry")
        


    @keyword
    def select_filters(self, start_date:str, end_date: str, exp_user: str, exp_team: str, exp_post: str):
        logger.info(f"Modify the filters to select a dispute entry")
        driver = self.__ctx.driver

        
        # self.__ctx.wait_until_element_is_visible(locator=adhadjlocators.DSPT_LIST)


        # Selecting the Start Date
        self.__ctx.wait_until_element_is_visible(locator=adhadjlocators.FLTR_SD_INP)
        self.__ctx.click_element(locator=adhadjlocators.FLTR_SD_INP)

        slocator = adhadjlocators.CAL_SD_PICKER
        sd_locator = f"//div[@aria-label='{start_date}']"
        sprev_btn = adhadjlocators.CAL_SDPREV

        while True:
            
            # Check if the target tr element is present in the current page
            try:
                tr_element = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f"{slocator}{sd_locator}")
                    )
                )
                # Click on the found tr_element
                tr_element.click()
                print("Clicked on:", tr_element.text)
                break  # Exit the loop since the element was found and clicked
            except:
                # Element not found, click on the "Next" link
                try:
                    prev_link = WebDriverWait(driver, 2).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, f"{sprev_btn}")
                        )
                    )
                    prev_link.click()
                    print("Clicked on 'Prev'")
                except:
                    print("Previous button not found or clickable, exiting loop.")
                    break  # Exit the loop if Next link is not found or not clickable


        # Selecting the End Date
        self.__ctx.wait_until_element_is_visible(locator=adhadjlocators.FLTR_ED_INP)
        self.__ctx.click_element(locator=adhadjlocators.FLTR_ED_INP)

        elocator = adhadjlocators.CAL_ED_PICKER
        ed_locator = f"//div[@aria-label='{end_date}']"
        eprev_btn = adhadjlocators.CAL_EDPREV

        while True:
            
            # Check if the target tr element is present in the current page
            try:
                tr_element = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f"{elocator}{ed_locator}")
                    )
                )
                # Click on the found tr_element
                tr_element.click()
                print("Clicked on:", tr_element.text)
                break  # Exit the loop since the element was found and clicked
            except:
                # Element not found, click on the "Next" link
                try:
                    prev_link = WebDriverWait(driver, 2).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, f"{eprev_btn}")
                        )
                    )
                    prev_link.click()
                    print("Clicked on 'Prev'")
                except:
                    print("Previous button not found or clickable, exiting loop.")
                    break  # Exit the loop if Next link is not found or not clickable


        # # Selecting the User/s
        self.__ctx.wait_until_element_is_visible(adhadjlocators.FLTR_USERS_DRPDWN)
        self.__ctx.click_element(adhadjlocators.FLTR_USERS_DRPDWN)
        time.sleep(5)
        self.__ctx.input_text(adhadjlocators.FLTR_USERS_SRCH, text=exp_user)
        self.__ctx.wait_until_element_is_visible(adhadjlocators.FLTR_USERS_RSLT)
        self.__ctx.click_element(adhadjlocators.FLTR_USERS_RSLT)
                              

        # Selecting the Team/s
        self.__ctx.wait_until_element_is_visible(adhadjlocators.FLTR_TEAM_DRPDWN)
        self.__ctx.click_element(adhadjlocators.FLTR_TEAM_DRPDWN)
        time.sleep(5)
        self.__ctx.input_text(adhadjlocators.FLTR_TEAM_SRCH, text=exp_team)
        self.__ctx.wait_until_element_is_visible(adhadjlocators.FLTR_TEAM_RSLT)
        self.__ctx.click_element(adhadjlocators.FLTR_TEAM_RSLT)



        # Selecting the Position/s
        self.__ctx.wait_until_element_is_visible(locator=adhadjlocators.FLTR_POST_DRPDWN)
        self.__ctx.click_element(locator=adhadjlocators.FLTR_POST_DRPDWN)
        self.__ctx.wait_until_element_is_visible(locator=adhadjlocators.POST_LOCATOR(position=exp_post))
        self.__ctx.click_element(locator=adhadjlocators.POST_LOCATOR(position=exp_post))


        # Selecting the Status
        self.__ctx.wait_until_element_is_visible(locator=adhadjlocators.FLTR_STAT_DRPDWN)
        self.__ctx.click_element(locator=adhadjlocators.FLTR_STAT_DRPDWN)
        self.__ctx.click_element(locator=adhadjlocators.FLTR_STAT_SALL)


        # Click the GO Button
        self.__ctx.click_element(locator=adhadjlocators.FLTR_GO_BTN)



    @keyword
    def select_dispute_entry(self, wfid: str, udid: str):
        driver = self.__ctx.driver

        self.__ctx.wait_until_element_is_visible(locator=adhadjlocators.DSPT_LIST)

        dislocator = adhadjlocators.DSPT_LIST
        dispute_locator = f"//tr[@data-workforceid='{wfid}' and @data-udid='{udid}']"
        dnext_btn = adhadjlocators.DIS_NEXTBTN

        while True:
            # Scroll down the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Check if the target tr element is present in the current page
            try:
                tr_element = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f"{dislocator}{dispute_locator}")
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
                            (By.XPATH, f"{dnext_btn}")
                        )
                    )
                    next_link.click()
                    print("Clicked on 'Next'")
                except:
                    print("Next link not found or clickable, exiting loop.")
                    break  # Exit the loop if Next link is not found or not clickable

            # Scroll up the page
            driver.execute_script("window.scrollTo(0, 0);")