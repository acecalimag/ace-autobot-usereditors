*** Settings ***
Library    UserTeamsLibrary
Library    UserTeamsLibrary.DatabaseLibrary
Library    UserTeamsLibrary.APILibrary
Library    RequestsLibrary
Library    SeleniumLibrary
Library    Collections
Variables  resource/variables.py

# Test Setup        User Team
# Test Teardown     Logout


*** Keywords ***
User Team

    Open Config In Browser
    Login                                username=${USERNAME}            password=${PASSWORD}
    Open User Team

Logout
    Logout To System
    

*** Test Cases ***

Verify the Team Details
    [Setup]        User Team
    [Teardown]     Logout
    
    Search And Click Next                team_name=${TEAMNAME}
    ${team_details}                      Check Team Details                   exp_name=${TEAMNAME}    exp_desc=${EXP_DESC}    exp_lead=${EXP_TLNAME}    exp_loc=${EXP_LOC}    exp_type=${EXP_TYPE}    exp_last_upd=${EXT_LAST_UPD}
    Log Dictionary                       ${team_details}
    Log To Console                       ${team_details}
    
    ${result}                            Get User Team Db                     tname=${TEAMNAME}
    Log Dictionary                       ${result}
    Log To Console                       ${result}

    # Comparison between UI and DB
    Should Be Equal As Strings           ${team_details['Team Name']}                ${result['Team Name']}
    Should Be Equal As Strings           ${team_details['Team Description']}         ${result['Team Description']}
    Should Be Equal As Strings           ${team_details['Team Lead']}                ${result['Team Lead']}
    Should Be Equal As Strings           ${team_details['Team Location']}            ${result['Team Location']}
    Should Be Equal As Strings           ${team_details['Team Type']}                ${result['Team Type']}
    Should Be Equal As Strings           ${team_details['Team Status']}              ${result['Team Status']}




Verify completeness of fields, labels, and buttons for User Teams Editor Page
    [Setup]        User Team
    [Teardown]     Logout
    
    ${team_list}                         Check Team List Table                exp_tllbl=${EXP_TLLBL}                exp_namelbl=${EXP_TBL_NAMELBL}        exp_leadlbl=${EXP_TBL_TLLBL}        exp_loclbl=${EXP_TBL_LOCLBL}        exp_typelbl=${EXP_TBL_TYPELBL}        exp_statuslbl=${EXP_TBL_STATUSLBL}        exp_lupdlbl=${EXP_TBL_LSTUPDLBL}
    Log Dictionary                       ${team_list}
    Log To Console                       ${team_list}
    
    Search And Click Next                team_name=${TEAMNAME}
    
    ${update}                            Check Update Section                 exp_vulbl=${EXP_VULBL}                exp_vu_namelbl=${EXP_VU_NAMELBL}      exp_vu_tdlbl=${EXP_VU_TDLBL}        exp_vu_tllbl=${EXP_VU_TLLBL}        exp_vu_loclbl=${EXP_VU_LOCLBL}        exp_vu_typelbl=${EXP_VU_TYPELBL}        exp_vu_statuslbl=${EXP_VU_STATUSLBL}        exp_vu_lstupdlbl=${EXP_VU_LSTUPDLBL}
    Log Dictionary                       ${update}
    Log To Console                       ${update}
    
    ${reminder}                          Check Reminder Section               exp_rmndrlbl=${EXP_RMNDR_LBL}         exp_alerttext=${EXP_RMNDR_TXT}
    Log Dictionary                       ${reminder}
    Log To Console                       ${reminder}


Create New Team
    [Setup]        User Team
    [Teardown]     Logout

    Click Create Team
    ${form_input}                        Fillout Form                               exp_cntlbl=${EXP_CNTLBL}            in_name=${IN_CNT_NAME}                  in_desc=${IN_CNT_TD}                in_lead=${IN_CNT_TL}                in_loc=${IN_CNT_LOC}                in_type=${IN_CNT_TYPE}              in_status=${IN_CNT_STATUS}
    Log Dictionary                       ${form_input}
    Log To Console                       ${form_input}
    
    # Click Save

    ${result}                            Get User Team Db                           tname=${IN_CNT_NAME}
    Log Dictionary                       ${result}
    Log To Console                       ${result}

    # Comparison between UI and DB
    Should Be Equal As Strings           ${form_input['Team Name']}                ${result['Team Name']}
    Should Be Equal As Strings           ${form_input['Team Description']}         ${result['Team Description']}
    Should Be Equal As Strings           ${form_input['Team Lead']}                ${result['Team Lead']}
    Should Be Equal As Strings           ${form_input['Team Location']}            ${result['Team Location']}
    Should Be Equal As Strings           ${form_input['Team Type']}                ${result['Team Type']}
    Should Be Equal As Strings           ${form_input['Team Status']}              ${result['Team Status']}


Edit / Modify Existing Team
    [Setup]        User Team
    [Teardown]     Logout
    
    Search And Click Next                team_name=${TEAMNAME}
    ${form_edit}                         Edit Team                                exp_vulbl=${EXP_VULBL}        ed_name=${ED_VU_NAME}        ed_desc=${ED_VU_TD}        ed_lead=${ED_VU_TL}        ed_loc=${ED_VU_LOC}        ed_type=${ED_VU_TYPE}        ed_status=${ED_VU_STATUS}
    Log Dictionary                       ${form_edit}
    Log To Console                       ${form_edit}
    
    # Click Save
    
    ${result}                            Get User Team Db                         tname=${ED_VU_NAME}
    Log Dictionary                       ${result}
    Log To Console                       ${result}

    # Comparison between UI and DB
    Should Be Equal As Strings           ${form_edit['Team Name']}                ${result['Team Name']}
    Should Be Equal As Strings           ${form_edit['Team Description']}         ${result['Team Description']}
    Should Be Equal As Strings           ${form_edit['Team Lead']}                ${result['Team Lead']}
    Should Be Equal As Strings           ${form_edit['Team Location']}            ${result['Team Location']}
    Should Be Equal As Strings           ${form_edit['Team Type']}                ${result['Team Type']}
    Should Be Equal As Strings           ${form_edit['Team Status']}              ${result['Team Status']}



Database Query
    ${result}                            Get User Team Db                   tname=${TEAMNAME}
    Log Dictionary                       ${result}
    Log To Console                       ${result}









