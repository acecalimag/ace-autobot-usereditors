
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from robot.api import logger
from asserts import assert_equal
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from AdherenceAdjustmentLibrary.locators import adhadjlocators


class DisputeDetails:
    
    def __init__(self, ctx: SeleniumLibrary) -> None:
        self.__ctx = ctx

    @keyword 
    def check_dispute_details(self, exp_ads_fname_dtl: str, exp_ads_stat_dtl: str, exp_ads_ctr_dtl: str, exp_ads_rtr_dtl: str, exp_ads_whrs_dtl: str):
        logger.info(f"Check the filed dispute details of an Agent")
        
        dispute_details = {}
        

        # Verify the Full Name
        act_ads_fname_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_FNAME_DTL)
        logger.info(f"got_act: {act_ads_fname_dtl}")
        dispute_details['Full Name'] = act_ads_fname_dtl
        assert_equal(act_ads_fname_dtl, exp_ads_fname_dtl, f"Expected form Team Name '{exp_ads_fname_dtl}' does not match the actual Full Name '{act_ads_fname_dtl}'")


        # Verify the Status
        act_ads_stat_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_STAT_DTL)
        logger.info(f"got_act: {act_ads_stat_dtl}")
        dispute_details['Status'] = act_ads_stat_dtl
        assert_equal(act_ads_stat_dtl, exp_ads_stat_dtl, f"Expected form Status '{exp_ads_stat_dtl}' does not match the actual Status '{act_ads_stat_dtl}'")


        # Verify the Current Time Range
        act_ads_ctr_st_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_CTR_ST_DTL)
        act_ads_ctr_et_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_CTR_ET_DTL)
        act_ads_ctr_dtl = f"{act_ads_ctr_st_dtl} - {act_ads_ctr_et_dtl}"
        logger.info(f"got_act: {act_ads_ctr_dtl}")
        dispute_details['Current Time Range'] = act_ads_ctr_dtl
        assert_equal(act_ads_ctr_dtl, exp_ads_ctr_dtl, f"Expected form Current Time Range '{exp_ads_ctr_dtl}' does not match the actual Current Time Range '{act_ads_ctr_dtl}'")       


        # Verify the Requested Time Range
        act_ads_rtr_st_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_RTR_ST_DTL)
        act_ads_rtr_et_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_RTR_ET_DTL)
        act_ads_rtr_dtl = f"{act_ads_rtr_st_dtl} - {act_ads_rtr_et_dtl}"
        logger.info(f"got_act: {act_ads_rtr_dtl}")
        dispute_details['Requested Time Range'] = act_ads_rtr_dtl
        assert_equal(act_ads_rtr_dtl, exp_ads_rtr_dtl, f"Expected form Requested Time Range '{exp_ads_rtr_dtl}' does not match the actual Requested Time Range '{act_ads_rtr_dtl}'")


        # Verify the Work Hours
        act_ads_whrs_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_WHRS_DTL)
        logger.info(f"got_act: {act_ads_whrs_dtl}")
        dispute_details['Status'] = act_ads_whrs_dtl
        assert_equal(act_ads_whrs_dtl, exp_ads_whrs_dtl, f"Expected form Status '{exp_ads_whrs_dtl}' does not match the actual Status '{act_ads_whrs_dtl}'")



        # # Verify the Team Status
        # driver = self.__ctx.driver
        # enabled_radio_locator = (By.XPATH, adhadjlocators.TSTAT_ENB)
        # disabled_radio_locator = (By.XPATH, adhadjlocators.TSTAT_DISB)

        # enabled_radio_button = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located(enabled_radio_locator)
        # )
        # is_enabled_selected = enabled_radio_button.is_selected()
        # is_enabled_enabled = enabled_radio_button.is_enabled()

        # disabled_radio_button = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located(disabled_radio_locator)
        # )
        # is_disabled_selected = disabled_radio_button.is_selected()
        # is_disabled_enabled = disabled_radio_button.is_enabled()

        # if is_enabled_selected and is_enabled_enabled:
        #     logger.info("ENABLE BUTTON IS SELECTED - TEAM STATUS is Enabled")
        #     dispute_details['Team Status'] = 'Enabled'
        # else:
        #     logger.info("ENABLE BUTTON IS NOT SELECTED - TEAM STATUS is Disabled")
        #     dispute_details['Team Status'] = 'Disabled'

        # if is_disabled_selected and is_disabled_enabled:
        #     logger.info("DISABLE BUTTON IS SELECTED - TEAM STATUS is Disabled")
        #     dispute_details['Team Status'] = 'Disabled'
        # else:
        #     logger.info("DISABLE BUTTON IS NOT SELECTED - TEAM STATUS is Enabled")
        #     dispute_details['Team Status'] = 'Enabled'


        # # Verify the Last Updated Details
        # act_last_upd = self.__ctx.get_text(locator=adhadjlocators.UPDTIME)
        # logger.info(f"got_act: {act_last_upd}")
        # dispute_details['Last Updated'] = act_last_upd
        # # assert_equal(act_last_upd, exp_last_upd, f"Expected form Last Updated '{exp_last_upd}' does not match the actual Last Updated '{act_last_upd}'")


        
        return dispute_details


