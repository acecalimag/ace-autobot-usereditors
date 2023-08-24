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
    Login And Redirect                    username=${USERNAME}                password=${PASSWORD}            redirect_url=${EXP_URL} 


Logout
    Logout To System
    

*** Test Cases ***

Verify completeness of fields, labels, and buttons for Adherence Adjustment Page
    [Setup]        Adherence Adjustment
    [Teardown]     Logout
    
    # Verify Adherence Adjustment Page Headers
    ${result_hdrs}                       Get User Details Headers             username=${USERNAME}
    ${adhadj_header}                     Check Page Header                    exp_hdr_adhadjlbl=${EXP_HDR_ADADJLBL}        exp_hdr_user=${result_hdrs['username']} - ${result_hdrs['position']}
    Log Dictionary                       ${adhadj_header}
    Log To Console                       ${adhadj_header}
    

    # Verify Adherence Adjustment Filters and its Placeholders
    ${result}                           Get User Details                      username=${USERNAME}
    Check Filter Section                exp_fltr_sdlbl=${EXP_FLTR_SDLBL}      exp_fltr_sdplhdr=${EXP_FLTR_SDPLHDR}        exp_fltr_edlbl=${EXP_FLTR_EDLBL}    exp_fltr_edplhdr=${EXP_FLTR_EDPLHDR}        exp_fltr_usersplhdr=Select users        exp_fltr_locplhdr=${result['location']}        exp_fltr_teamspldhr=Select teams        exp_fltr_posplhdr=Select Positions        exp_fltr_statplhdr=Pending



    # Select a Dispute Entry
    ${result}                           Get User Details                      username=${DISP_AGENT_NAME}
    Select Filters                      start_date=2023-01-01                 end_date=2023-08-01                         exp_user=${result['username']}        exp_team=${result['team']}            exp_post=${result['position']}
    Select Dispute Entry                wfid=${result['workforceid']}         udid=${UDID}
    

    # Verify the column names in the Dispute Table
    ${dispute_table}                     Check Dispute Table                  exp_rtrlbl=${EXP_TBL_RTR_LBL}                exp_unamelbl=${EXP_TBL_UNAME_LBL}            exp_loclbl=${EXP_TBL_LOC_LBL}            exp_teamlbl=${EXP_TBL_TEAM_LBL}            exp_statuslbl=${EXP_TBL_STAT_LBL}            exp_rvwrlbl=${EXP_TBL_RVWR_LBL}            exp_rvwdatlbl=${EXP_TBL_RVWDAT_LBL}            exp_crtdlbl=${EXP_TBL_CRTD_LBL}
    Log Dictionary                       ${dispute_table}
    Log To Console                       ${dispute_table}

    
    # Verify the Adherence/Dispute Information Header, Labels and Buttons
    # ${result}                               Get User Details                           username=${DISP_AGENT_NAME}
    # Select Filters                          start_date=2023-01-01                      end_date=2023-08-01                           exp_user=${result['username']}                exp_team=${result['team']}                exp_post=${result['position']}
    # Select Dispute Entry                    wfid=${result['workforceid']}              udid=${UDID}
    
    ${adi_section}                          Check Adherence Dispute Info Section       exp_ads_hdr=${EXP_ADS_HDR}                    exp_ads_fname_lbl=${EXP_ADS_FNAME_LBL}        exp_ads_stat_lbl=${EXP_ADS_STAT_LBL}          exp_ads_ctr_lbl=${EXP_ADS_CTR_LBL}        exp_ads_rtr_lbl=${EXP_ADS_RTR_LBL}        exp_ads_whrs_lbl=${EXP_ADS_WHRS_LBL}        exp_ads_rsn_lbl=${EXP_ADS_RSN_LBL}        exp_ads_crt_lbl=${EXP_ADS_CRT_LBL}        exp_ads_loc_lbl=${EXP_ADS_LOC_LBL}        exp_ads_team_lbl=${EXP_ADS_TEAM_LBL}        exp_ads_cact_lbl=${EXP_ADS_CACT_LBL}        exp_ads_ract_lbl=${EXP_ADS_RACT_LBL}        exp_ads_phrs_lbl=${EXP_ADS_PHRS_LBL}        exp_ads_revsec_lbl=${EXP_ADS_REVSEC_LBL}        exp_ads_cmnt_lbl=${EXP_ADS_CMNT_LBL}        exp_ads_inotes_lbl=${EXP_ADS_INOTES_LBL}        exp_ads_revby_lbl=${EXP_ADS_REVBY_LBL}        exp_ads_revat_lbl=${EXP_ADS_REVAT_LBL}        exp_ads_cnfrmat_lbl=${EXP_ADS_CNFRMAT_LBL}        exp_ads_aupsched_lbl=${EXP_ADS_AUPSCHED_LBL}        exp_ads_auact_lbl=${EXP_ADS_AUACT_LBL}        exp_ads_manup_lbl=${EXP_ADS_MANUP_LBL}
    Log Dictionary                          ${adi_section}
    Log To Console                          ${adi_section}



View Dispute Details
    [Setup]        Adherence Adjustment
    [Teardown]     Logout

    # Verify the Adherence/Dispute Information

    ${result}                           Get User Details                     username=${DISP_AGENT_NAME}
    Select Filters                      start_date=2023-01-01                end_date=2023-08-01                           exp_user=${result['username']}        exp_team=${result['team']}           exp_post=${result['position']}
    Select Dispute Entry                wfid=${result['workforceid']}        udid=${UDID}
    Sleep    5s
    
    

Testing the Adherence Dispute Information Header, Labels and Buttons
    [Setup]        Adherence Adjustment
    [Teardown]     Logout

    ${result}                               Get User Details                           username=${DISP_AGENT_NAME}
    Select Filters                          start_date=2023-01-01                      end_date=2023-08-01                           exp_user=${result['username']}                exp_team=${result['team']}                exp_post=${result['position']}
    Select Dispute Entry                    wfid=${result['workforceid']}              udid=${UDID}
    
    ${adi_section}                          Check Adherence Dispute Info Section       exp_ads_hdr=${EXP_ADS_HDR}                    exp_ads_fname_lbl=${EXP_ADS_FNAME_LBL}        exp_ads_stat_lbl=${EXP_ADS_STAT_LBL}          exp_ads_ctr_lbl=${EXP_ADS_CTR_LBL}        exp_ads_rtr_lbl=${EXP_ADS_RTR_LBL}        exp_ads_whrs_lbl=${EXP_ADS_WHRS_LBL}        exp_ads_rsn_lbl=${EXP_ADS_RSN_LBL}        exp_ads_crt_lbl=${EXP_ADS_CRT_LBL}        exp_ads_loc_lbl=${EXP_ADS_LOC_LBL}        exp_ads_team_lbl=${EXP_ADS_TEAM_LBL}        exp_ads_cact_lbl=${EXP_ADS_CACT_LBL}        exp_ads_ract_lbl=${EXP_ADS_RACT_LBL}        exp_ads_phrs_lbl=${EXP_ADS_PHRS_LBL}        exp_ads_revsec_lbl=${EXP_ADS_REVSEC_LBL}        exp_ads_cmnt_lbl=${EXP_ADS_CMNT_LBL}        exp_ads_inotes_lbl=${EXP_ADS_INOTES_LBL}        exp_ads_revby_lbl=${EXP_ADS_REVBY_LBL}        exp_ads_revat_lbl=${EXP_ADS_REVAT_LBL}        exp_ads_cnfrmat_lbl=${EXP_ADS_CNFRMAT_LBL}        exp_ads_aupsched_lbl=${EXP_ADS_AUPSCHED_LBL}        exp_ads_auact_lbl=${EXP_ADS_AUACT_LBL}        exp_ads_manup_lbl=${EXP_ADS_MANUP_LBL}
    Log Dictionary                          ${adi_section}
    Log To Console                          ${adi_section}



Database Query User Details
    ${result}                            Get User Details                              username=${DISP_AGENT_NAME}
    Log Dictionary                       ${result}
    Log To Console                       ${result}


Database Dispute Details
    ${result}                            Get Dispute Details                         udid=${UDID}
    Log Dictionary                       ${result}
    Log To Console                       ${result}





