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
    ${result}                            Get User Details                     username=${USERNAME}
    ${adhadj_header}                     Check Page Header                    exp_hdr_adhadjlbl=${EXP_HDR_ADADJLBL}        exp_hdr_user=${result['username']} - ${result['position']}
    Log Dictionary                       ${adhadj_header}
    Log To Console                       ${adhadj_header}
    

    # Verify Adherence Adjustment Filters and its Placeholders
    ${result}                           Get User Details                    username=${USERNAME}
    Check Filter Section                exp_fltr_sdlbl=${EXP_FLTR_SDLBL}    exp_fltr_sdplhdr=${EXP_FLTR_SDPLHDR}        exp_fltr_edlbl=${EXP_FLTR_EDLBL}    exp_fltr_edplhdr=${EXP_FLTR_EDPLHDR}        exp_fltr_usersplhdr=Select users        exp_fltr_locplhdr=${result['location']}        exp_fltr_teamspldhr=Select teams        exp_fltr_posplhdr=Select Positions



    # Select a Dispute Entry
    ${result}                           Get User Details                     username=tqa3
    Select Filters                      start_date=2023-01-01                end_date=2023-08-01        exp_user=tqa4        exp_team=Cleveland            exp_post=Engineering
    Select Dispute Entry                wfid=${result['workforceid']}        udid=10623919-cb46-412f-bba5-69ce21a8db6e
    

    # Verify the column names in the Dispute Table
    ${dispute_table}                     Check Dispute Table                  exp_rtrlbl=${EXP_TBL_RTR_LBL}                exp_unamelbl=${EXP_TBL_UNAME_LBL}            exp_loclbl=${EXP_TBL_LOC_LBL}            exp_teamlbl=${EXP_TBL_TEAM_LBL}            exp_statuslbl=${EXP_TBL_STAT_LBL}            exp_rvwrlbl=${EXP_TBL_RVWR_LBL}            exp_rvwdatlbl=${EXP_TBL_RVWDAT_LBL}            exp_crtdlbl=${EXP_TBL_CRTD_LBL}
    Log Dictionary                       ${dispute_table}
    Log To Console                       ${dispute_table}

    
    # Verify the Adherence/Dispute Information Labels



View Dispute Details
    [Setup]        Adherence Adjustment
    [Teardown]     Logout

    # Verify the Adherence/Dispute Information

    # ${result}                           Get User Details                     username=tqa3
    Select Filters                      start_date=2023-01-01                end_date=2023-08-01        exp_user=tqa3        exp_team=Xrp            exp_post=Engineering
    Select Dispute Entry                wfid=99007                           udid=10623919-cb46-412f-bba5-69ce21a8db6e
    # ${result['workforceid']}
    Sleep    20s
    
    

Testing the Filters
    [Setup]        Adherence Adjustment
    [Teardown]     Logout

    ${result}                           Get User Details                    username=${USERNAME}
    Check Filter Section                exp_fltr_sdlbl=${EXP_FLTR_SDLBL}    exp_fltr_sdplhdr=${EXP_FLTR_SDPLHDR}        exp_fltr_edlbl=${EXP_FLTR_EDLBL}    exp_fltr_edplhdr=${EXP_FLTR_EDPLHDR}        exp_fltr_usersplhdr=Select users        exp_fltr_locplhdr=${result['location']}        exp_fltr_teamspldhr=Select teams        exp_fltr_posplhdr=Select Positions





Database Query User Details
    ${result}                            Get User Details                            username=${USERNAME}
    Log To Console                       ${result['location']}


Database Dispute Details
    ${result}                            Get Dispute Details                         udid=271cf76b-cab5-4964-8e19-7ef10aa84f11
    Log Dictionary                       ${result}
    Log To Console                       ${result}





