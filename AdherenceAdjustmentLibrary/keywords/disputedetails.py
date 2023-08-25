
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
    def check_dispute_details(self, exp_ads_fname_dtl: str, exp_ads_stat_dtl: str, exp_ads_ctr_dtl: str, exp_ads_rtr_dtl: str, exp_ads_whrs_dtl: str, exp_ads_rsn_dtl:str, exp_ads_crt_dtl:str, exp_ads_loc_dtl:str, exp_ads_team_dtl: str, exp_ads_cact_dtl: str, exp_ads_ract_dtl:str, exp_ads_phrs_dtl: str, exp_ads_cmnt_dtl: str, exp_ads_inotes_dtl: str, exp_ads_revby_dtl: str, exp_ads_revat_dtl: str, exp_ads_cnfrmat_dtl: str):
        logger.info(f"Check the filed dispute details of an Agent")
        
        dispute_details = {}
        

        # Verify the Full Name
        act_ads_fname_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_FNAME_DTL)
        logger.info(f"got_act: {act_ads_fname_dtl}")
        dispute_details['Full Name'] = act_ads_fname_dtl
        assert_equal(act_ads_fname_dtl, exp_ads_fname_dtl, f"Expected form Full Name '{exp_ads_fname_dtl}' does not match the actual Full Name '{act_ads_fname_dtl}'")


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
        dispute_details['Work Hours'] = act_ads_whrs_dtl
        assert_equal(act_ads_whrs_dtl, exp_ads_whrs_dtl, f"Expected form Work Hours '{exp_ads_whrs_dtl}' does not match the actual Work Hours '{act_ads_whrs_dtl}'")


        # Verify the Reason
        act_ads_rsn_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_RSN_DTL)
        logger.info(f"got_act: {act_ads_rsn_dtl}")
        dispute_details['Reason'] = act_ads_rsn_dtl
        assert_equal(act_ads_rsn_dtl, exp_ads_rsn_dtl, f"Expected form Reason '{exp_ads_rsn_dtl}' does not match the actual Reason '{act_ads_rsn_dtl}'")


        # Verify the Created At
        act_ads_crt_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_CRT_DTL)
        logger.info(f"got_act: {act_ads_crt_dtl}")
        dispute_details['Created At'] = act_ads_crt_dtl
        assert_equal(act_ads_crt_dtl, exp_ads_crt_dtl, f"Expected form Created At '{exp_ads_crt_dtl}' does not match the actual Created At '{act_ads_crt_dtl}'")


        # Verify the Location
        act_ads_loc_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_LOC_DTL)
        logger.info(f"got_act: {act_ads_loc_dtl}")
        dispute_details['Location'] = act_ads_loc_dtl
        assert_equal(act_ads_loc_dtl, exp_ads_loc_dtl, f"Expected form Location '{exp_ads_loc_dtl}' does not match the actual Location '{act_ads_loc_dtl}'")


        # Verify the Team
        act_ads_team_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_TEAM_DTL)
        logger.info(f"got_act: {act_ads_team_dtl}")
        dispute_details['Team'] = act_ads_team_dtl
        assert_equal(act_ads_team_dtl, exp_ads_team_dtl, f"Expected form Team '{exp_ads_team_dtl}' does not match the actual Team '{act_ads_team_dtl}'")


        # Verify the Current Activity
        act_ads_cact_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_CACT_DTL)
        logger.info(f"got_act: {act_ads_cact_dtl}")
        dispute_details['Current Activity'] = act_ads_cact_dtl
        assert_equal(act_ads_cact_dtl, exp_ads_cact_dtl, f"Expected form Current Activity '{exp_ads_cact_dtl}' does not match the actual Current Activity '{act_ads_cact_dtl}'")


        # Verify the Requested Activity
        act_ads_ract_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_RACT_DTL)
        logger.info(f"got_act: {act_ads_ract_dtl}")
        dispute_details['Requested Activity'] = act_ads_ract_dtl
        assert_equal(act_ads_ract_dtl, exp_ads_ract_dtl, f"Expected form Requested Activity '{exp_ads_ract_dtl}' does not match the actual Requested Activity '{act_ads_ract_dtl}'")


        # Verify the Pay Hours
        act_ads_phrs_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_PHRS_DTL)
        logger.info(f"got_act: {act_ads_phrs_dtl}")
        dispute_details['Pay Hours'] = act_ads_phrs_dtl
        assert_equal(act_ads_phrs_dtl, exp_ads_phrs_dtl, f"Expected form Pay Hours '{exp_ads_phrs_dtl}' does not match the actual Pay Hours '{act_ads_phrs_dtl}'")


        # Verify the Comment
        act_ads_cmnt_dtl = self.__ctx.get_value(locator=adhadjlocators.ADS_CMNT_DTL)
        logger.info(f"got_act: {act_ads_cmnt_dtl}")
        dispute_details['Comment'] = act_ads_cmnt_dtl
        assert_equal(act_ads_cmnt_dtl, exp_ads_cmnt_dtl, f"Expected form Comment '{exp_ads_cmnt_dtl}' does not match the actual Comment '{act_ads_cmnt_dtl}'")


        # Verify the Internal Notes
        act_ads_inotes_dtl = self.__ctx.get_value(locator=adhadjlocators.ADS_INOTES_DTL)
        logger.info(f"got_act: {act_ads_inotes_dtl}")
        dispute_details['Internal Notes'] = act_ads_inotes_dtl
        assert_equal(act_ads_inotes_dtl, exp_ads_inotes_dtl, f"Expected form Internal Notes '{exp_ads_inotes_dtl}' does not match the actual Internal Notes '{act_ads_inotes_dtl}'")


        # Verify the Reviewed By
        act_ads_revby_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_REVBY_DTL)
        logger.info(f"got_act: {act_ads_revby_dtl}")
        dispute_details['Reviewed By'] = act_ads_revby_dtl
        assert_equal(act_ads_revby_dtl, exp_ads_revby_dtl, f"Expected form Reviewed By '{exp_ads_revby_dtl}' does not match the actual Reviewed By '{act_ads_revby_dtl}'")


        # Verify the Reviewed At
        act_ads_revat_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_REVAT_DTL)
        logger.info(f"got_act: {act_ads_revat_dtl}")
        dispute_details['Reviewed At'] = act_ads_revat_dtl
        assert_equal(act_ads_revat_dtl, exp_ads_revat_dtl, f"Expected form Reviewed At '{exp_ads_revat_dtl}' does not match the actual Reviewed At '{act_ads_revat_dtl}'")


        # Verify the Confirmed At
        act_ads_cnfrmat_dtl = self.__ctx.get_text(locator=adhadjlocators.ADS_CNFRMAT_DTL)
        logger.info(f"got_act: {act_ads_cnfrmat_dtl}")
        dispute_details['Confirmed At'] = act_ads_cnfrmat_dtl
        assert_equal(act_ads_cnfrmat_dtl, exp_ads_cnfrmat_dtl, f"Expected form Confirmed At '{exp_ads_cnfrmat_dtl}' does not match the actual Confirmed At '{act_ads_cnfrmat_dtl}'")


        return dispute_details


