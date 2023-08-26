 
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AdherenceAdjustmentLibrary.locators import adhadjlocators
from robot.api import logger
from robot.api import logger
from datetime import datetime
import time
import os


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
        time.sleep(2)
        self.__ctx.input_text(adhadjlocators.FLTR_USERS_SRCH, text=exp_user)
        self.__ctx.wait_until_element_is_visible(adhadjlocators.FLTR_USERS_RSLT)
        self.__ctx.click_element(adhadjlocators.FLTR_USERS_RSLT)
                              

        # Selecting the Team/s
        self.__ctx.wait_until_element_is_visible(adhadjlocators.FLTR_TEAM_DRPDWN)
        self.__ctx.click_element(adhadjlocators.FLTR_TEAM_DRPDWN)
        time.sleep(2)
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
    

    # @keyword
    # def click_export_to_xls_button(self):
    #     logger.info("Clicking the Export to xls button to download the selected dispute entries")

    #     # Perform the click action here
    #     self.__ctx.wait_until_element_is_visible(locator=adhadjlocators.FLTR_EXPRT_BTN)
    #     self.__ctx.click_button(locator=adhadjlocators.FLTR_EXPRT_BTN)

    #     # Specify the directory where downloads are expected
    #     download_directory = r"C:\Users\WONDERS\Downloads"  # Use a raw string with 'r' prefix
    #     expected_filename = "Adh_Adj_20230101-20230801.xlsx"

    #     # Wait for the file to appear in the download directory
    #     timeout = 60  # Maximum time to wait in seconds
    #     interval = 5  # Time interval between checks in seconds
    #     elapsed_time = 0

    #     while elapsed_time < timeout:
    #         file_path = os.path.join(download_directory, expected_filename)
    #         if os.path.exists(file_path):
    #             logger.info(f"File '{expected_filename}' was downloaded successfully.")
    #             break  # Exit the loop when the file is found
    #         else:
    #             time.sleep(interval)
    #             elapsed_time += interval

    #     if elapsed_time >= timeout:
    #         logger.warn(f"File '{expected_filename}' was not found in the download directory after waiting.")


    @keyword
    def click_export_to_xls_button(self, start_date: str, end_date: str):
        logger.info("Clicking the Export to xls button to download the selected dispute entries")

        self.__ctx.wait_until_element_is_visible(locator=adhadjlocators.FLTR_EXPRT_BTN)
        self.__ctx.click_button(locator=adhadjlocators.FLTR_EXPRT_BTN)

        input_sdate = datetime.strptime(start_date, "%Y-%m-%d")
        input_edate = datetime.strptime(end_date, "%Y-%m-%d")

        output_sdate = input_sdate.strftime("%Y%m%d")
        output_edate = input_edate.strftime("%Y%m%d")
        
        download_directory = r"C:\Users\WONDERS\Downloads"
        expected_filename = f"Adh_Adj_{output_sdate}-{output_edate}.xlsx"

        # Wait for the file to appear in the download directory
        timeout = 60
        interval = 5
        elapsed_time = 0
        file_path = os.path.join(download_directory, expected_filename)

        while elapsed_time < timeout:
            if os.path.exists(file_path):
                logger.info(f"File '{expected_filename}' was downloaded successfully.")
                
                # Delete the file after validation
                os.remove(file_path)
                logger.info(f"File '{expected_filename}' has been deleted after validation.")
                break  # Exit the loop when the file is found and validated
            else:
                time.sleep(interval)
                elapsed_time += interval

        if elapsed_time >= timeout:
            logger.warn(f"File '{expected_filename}' was not found in the download directory after waiting.")