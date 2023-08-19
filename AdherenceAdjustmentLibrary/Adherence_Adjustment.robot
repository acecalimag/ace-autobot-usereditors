*** Settings ***
Library    AdherenceAdjustmentLibrary
Library    AdherenceAdjustmentLibrary.DatabaseLibrary
Library    AdherenceAdjustmentLibrary.APILibrary
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
    ${result}                            Get User Details                     username=${USERNAME}
    ${adhadj_header}                     Check Page Header                    exp_hdr_adhadjlbl=${EXP_HDR_ADADJLBL}        exp_hdr_user=${result['username']} - ${result['position']}
    Log Dictionary                       ${adhadj_header}
    Log To Console                       ${adhadj_header}
    

    # Verify Adherence Adjustment Filters and its Placeholders Details



    # Select a Dispute Entry
    ${result}                           Get User Details                     username=tqa3
    Select Dispute Entry                start_date=2023-01-01                end_date=2023-08-01        exp_user=tqa3            exp_post=Engineering
    Search And Click Next               wfid=${result['workforceid']}        udid=10623919-cb46-412f-bba5-69ce21a8db6e
    

    # Verify the column names in the Dispute Table
    ${dispute_table}                     Check Dispute Table                  exp_rtrlbl=${EXP_TBL_RTR_LBL}                exp_unamelbl=${EXP_TBL_UNAME_LBL}            exp_loclbl=${EXP_TBL_LOC_LBL}            exp_teamlbl=${EXP_TBL_TEAM_LBL}            exp_statuslbl=${EXP_TBL_STAT_LBL}            exp_rvwrlbl=${EXP_TBL_RVWR_LBL}            exp_rvwdatlbl=${EXP_TBL_RVWDAT_LBL}            exp_crtdlbl=${EXP_TBL_CRTD_LBL}
    Log Dictionary                       ${dispute_table}
    Log To Console                       ${dispute_table}

    
    # Verify the Adherence/Dispute Information Labels



View Dispute Details
    [Setup]        Adherence Adjustment
    [Teardown]     Logout

    # Verify the Adherence/Dispute Information

    ${result}                           Get User Details                     username=tqa3
    Select Dispute Entry                start_date=2023-01-01                end_date=2023-08-01        exp_user=tqa3            exp_post=Engineering
    Search And Click Next               wfid=${result['workforceid']}        udid=10623919-cb46-412f-bba5-69ce21a8db6e
    Sleep    20s







Database Query
    ${result}                            Get User Details                            username=${USERNAME}
    Log To Console                       ${result}







