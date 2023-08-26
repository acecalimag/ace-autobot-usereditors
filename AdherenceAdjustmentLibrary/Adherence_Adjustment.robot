*** Settings ***
Library    AdherenceAdjustmentLibrary
Library    AdherenceAdjustmentLibrary.DatabaseLibrary
# Library    AdherenceAdjustmentLibrary.APILibrary
Library    RequestsLibrary
Library    SeleniumLibrary
Library    Collections
Variables  resource/variables.py

# Test Setup        User Team
# Test Teardown     Logout


*** Keywords ***
Adherence Adjustment

    Open Config In Browser
    Login And Redirect                   username=${USERNAME}                password=${PASSWORD}            redirect_url=${EXP_URL} 


Logout
    Logout To System
    

*** Test Cases ***

Verify completeness of fields, labels, and buttons for Adherence Adjustment Page
    [Setup]        Adherence Adjustment
    [Teardown]     Logout
    
    # Verify Adherence Adjustment Page Headers
    ${result_hdrs}                       Get User Details Headers                    username=${USERNAME}
    ${adhadj_header}                     Check Page Header                           exp_hdr_adhadjlbl=${EXP_HDR_ADADJLBL}                  exp_hdr_user=${result_hdrs['username']} - ${result_hdrs['position']}
    Log Dictionary                       ${adhadj_header}
    Log To Console                       ${adhadj_header}
    

    # Verify Adherence Adjustment Filters and its Placeholders
    ${result}                           Get User Details                             username=${USERNAME}
    Check Filter Section                exp_fltr_sdlbl=${EXP_FLTR_SDLBL}             exp_fltr_sdplhdr=${EXP_FLTR_SDPLHDR}           exp_fltr_edlbl=${EXP_FLTR_EDLBL}    exp_fltr_edplhdr=${EXP_FLTR_EDPLHDR}        exp_fltr_usersplhdr=Select users        exp_fltr_locplhdr=${result['location']}        exp_fltr_teamspldhr=Select teams        exp_fltr_posplhdr=Select Positions        exp_fltr_statplhdr=Pending


    # Select a Dispute Entry
    ${result}                           Get User Details                             username=${DISP_AGENT_NAME}
    ${res_dis}                          Get Dispute Details Db                       udid=${UDID}
    Select Filters                      start_date=${EXP_FLTR_SDATE}                 end_date=${EXP_FLTR_EDATE}                            exp_user=${result['username']}        exp_team=${result['team']}            exp_post=${result['position']}
    Click Export To Xls Button          start_date=${EXP_FLTR_SDATE}                 end_date=${EXP_FLTR_EDATE}
    Select Dispute Entry                wfid=${result['workforceid']}                udid=${res_dis['UDID']}

    # Verify the column names in the Dispute Table
    ${dispute_table}                    Check Dispute Table                          exp_rtrlbl=${EXP_TBL_RTR_LBL}                  exp_unamelbl=${EXP_TBL_UNAME_LBL}            exp_loclbl=${EXP_TBL_LOC_LBL}            exp_teamlbl=${EXP_TBL_TEAM_LBL}            exp_statuslbl=${EXP_TBL_STAT_LBL}            exp_rvwrlbl=${EXP_TBL_RVWR_LBL}            exp_rvwdatlbl=${EXP_TBL_RVWDAT_LBL}            exp_crtdlbl=${EXP_TBL_CRTD_LBL}
    Log Dictionary                      ${dispute_table}
    Log To Console                      ${dispute_table}

    
    # Verify the Adherence/Dispute Information Header, Labels and Buttons
    ${adi_section}                      Check Adherence Dispute Info Section        exp_ads_hdr=${EXP_ADS_HDR}                    exp_ads_fname_lbl=${EXP_ADS_FNAME_LBL}        exp_ads_stat_lbl=${EXP_ADS_STAT_LBL}          exp_ads_ctr_lbl=${EXP_ADS_CTR_LBL}        exp_ads_rtr_lbl=${EXP_ADS_RTR_LBL}        exp_ads_whrs_lbl=${EXP_ADS_WHRS_LBL}        exp_ads_rsn_lbl=${EXP_ADS_RSN_LBL}        exp_ads_crt_lbl=${EXP_ADS_CRT_LBL}        exp_ads_loc_lbl=${EXP_ADS_LOC_LBL}        exp_ads_team_lbl=${EXP_ADS_TEAM_LBL}        exp_ads_cact_lbl=${EXP_ADS_CACT_LBL}        exp_ads_ract_lbl=${EXP_ADS_RACT_LBL}        exp_ads_phrs_lbl=${EXP_ADS_PHRS_LBL}        exp_ads_revsec_lbl=${EXP_ADS_REVSEC_LBL}        exp_ads_cmnt_lbl=${EXP_ADS_CMNT_LBL}        exp_ads_inotes_lbl=${EXP_ADS_INOTES_LBL}        exp_ads_revby_lbl=${EXP_ADS_REVBY_LBL}        exp_ads_revat_lbl=${EXP_ADS_REVAT_LBL}        exp_ads_cnfrmat_lbl=${EXP_ADS_CNFRMAT_LBL}        exp_ads_aupsched_lbl=${EXP_ADS_AUPSCHED_LBL}        exp_ads_auact_lbl=${EXP_ADS_AUACT_LBL}        exp_ads_manup_lbl=${EXP_ADS_MANUP_LBL}
    Log Dictionary                      ${adi_section}
    Log To Console                      ${adi_section}



Verify the Dispute Details
    [Setup]        Adherence Adjustment
    [Teardown]     Logout

    # Verify the Adherence/Dispute Information

    ${res_dis}                           Get Dispute Details Db                     udid=${UDID}

    ${result}                            Get User Details                           username=${DISP_AGENT_NAME}
    Select Filters                       start_date=${EXP_FLTR_SDATE}               end_date=${EXP_FLTR_EDATE}                    exp_user=${result['username']}                exp_team=${result['team']}                              exp_post=${result['position']}
    Select Dispute Entry                 wfid=${result['workforceid']}              udid=${res_dis['UDID']}
    
    ${dis_dtls}                          Check Dispute Details                      exp_ads_fname_dtl=${res_dis['Full Name']}     exp_ads_stat_dtl=${res_dis['Status']}         exp_ads_ctr_dtl=${res_dis['Current Time Range']}        exp_ads_rtr_dtl=${res_dis['Requested Time Range']}          exp_ads_whrs_dtl=${res_dis['Work Hours']}        exp_ads_rsn_dtl=${res_dis['Reason']}        exp_ads_crt_dtl=${res_dis['Created At']}        exp_ads_loc_dtl=${res_dis['Location']}        exp_ads_team_dtl=${res_dis['Team']}        exp_ads_cact_dtl=${res_dis['Current Activity']}        exp_ads_ract_dtl=${res_dis['Requested Activity']}        exp_ads_phrs_dtl=${res_dis['Pay Hours']}        exp_ads_cmnt_dtl=${res_dis['Comment']}        exp_ads_inotes_dtl=${res_dis['Internal Notes']}        exp_ads_revby_dtl=${res_dis['Reviewed By']}        exp_ads_revat_dtl=${res_dis['Reviewed At']}        exp_ads_cnfrmat_dtl=${res_dis['Confirmed At']}
    Log Dictionary                       ${dis_dtls}
    Log To Console                       ${dis_dtls}

    # Comparison between UI and DB
    Should Be Equal As Strings           ${dis_dtls['Full Name']}                   ${res_dis['Full Name']}
    Should Be Equal As Strings           ${dis_dtls['Status']}                      ${res_dis['Status']}
    Should Be Equal As Strings           ${dis_dtls['Current Time Range']}          ${res_dis['Current Time Range']}
    Should Be Equal As Strings           ${dis_dtls['Requested Time Range']}        ${res_dis['Requested Time Range']}
    Should Be Equal As Strings           ${dis_dtls['Work Hours']}                  ${res_dis['Work Hours']}
    Should Be Equal As Strings           ${dis_dtls['Reason']}                      ${res_dis['Reason']}
    Should Be Equal As Strings           ${dis_dtls['Created At']}                  ${res_dis['Created At']}
    Should Be Equal As Strings           ${dis_dtls['Location']}                    ${res_dis['Location']}
    Should Be Equal As Strings           ${dis_dtls['Team']}                        ${res_dis['Team']}
    Should Be Equal As Strings           ${dis_dtls['Current Activity']}            ${res_dis['Current Activity']}
    Should Be Equal As Strings           ${dis_dtls['Requested Activity']}          ${res_dis['Requested Activity']}
    Should Be Equal As Strings           ${dis_dtls['Pay Hours']}                   ${res_dis['Pay Hours']}
    Should Be Equal As Strings           ${dis_dtls['Comment']}                     ${res_dis['Comment']}
    Should Be Equal As Strings           ${dis_dtls['Internal Notes']}              ${res_dis['Internal Notes']}
    Should Be Equal As Strings           ${dis_dtls['Reviewed By']}                 ${res_dis['Reviewed By']}
    Should Be Equal As Strings           ${dis_dtls['Reviewed At']}                 ${res_dis['Reviewed At']}
    Should Be Equal As Strings           ${dis_dtls['Confirmed At']}                ${res_dis['Confirmed At']}
    
    

Testing the Adherence Dispute Information Header, Labels and Buttons
    [Setup]        Adherence Adjustment
    [Teardown]     Logout

    ${result}                               Get User Details                        username=${DISP_AGENT_NAME}
    ${res_dis}                              Get Dispute Details Db                  udid=${UDID}
    Select Filters                          start_date=${EXP_FLTR_SDATE}            end_date=${EXP_FLTR_EDATE}                    exp_user=${result['username']}                exp_team=${result['team']}                exp_post=${result['position']}
    Select Dispute Entry                    wfid=${result['workforceid']}           udid=${res_dis['UDID']}
    
    ${adi_section}                          Check Adherence Dispute Info Section    exp_ads_hdr=${EXP_ADS_HDR}                    exp_ads_fname_lbl=${EXP_ADS_FNAME_LBL}        exp_ads_stat_lbl=${EXP_ADS_STAT_LBL}          exp_ads_ctr_lbl=${EXP_ADS_CTR_LBL}        exp_ads_rtr_lbl=${EXP_ADS_RTR_LBL}        exp_ads_whrs_lbl=${EXP_ADS_WHRS_LBL}        exp_ads_rsn_lbl=${EXP_ADS_RSN_LBL}        exp_ads_crt_lbl=${EXP_ADS_CRT_LBL}        exp_ads_loc_lbl=${EXP_ADS_LOC_LBL}        exp_ads_team_lbl=${EXP_ADS_TEAM_LBL}        exp_ads_cact_lbl=${EXP_ADS_CACT_LBL}        exp_ads_ract_lbl=${EXP_ADS_RACT_LBL}        exp_ads_phrs_lbl=${EXP_ADS_PHRS_LBL}        exp_ads_revsec_lbl=${EXP_ADS_REVSEC_LBL}        exp_ads_cmnt_lbl=${EXP_ADS_CMNT_LBL}        exp_ads_inotes_lbl=${EXP_ADS_INOTES_LBL}        exp_ads_revby_lbl=${EXP_ADS_REVBY_LBL}        exp_ads_revat_lbl=${EXP_ADS_REVAT_LBL}        exp_ads_cnfrmat_lbl=${EXP_ADS_CNFRMAT_LBL}        exp_ads_aupsched_lbl=${EXP_ADS_AUPSCHED_LBL}        exp_ads_auact_lbl=${EXP_ADS_AUACT_LBL}        exp_ads_manup_lbl=${EXP_ADS_MANUP_LBL}
    Log Dictionary                          ${adi_section}
    Log To Console                          ${adi_section}





Database Query User Details
    ${result}                            Get User Details                          username=${DISP_AGENT_NAME}
    Log Dictionary                       ${result}
    Log To Console                       ${result}


Database Dispute Details
    ${result}                            Get Dispute Details Db                     udid=${UDID}
    Log Dictionary                       ${result}
    Log To Console                       ${result}





