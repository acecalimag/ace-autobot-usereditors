*** Settings ***
Library    UserTeamsLibrary
Library    UserTeamsLibrary.DatabaseLibrary
Library    UserTeamsLibrary.APILibrary
Library    RequestsLibrary
Library    SeleniumLibrary
Library    Collections
Variables  resource/variables.py

# Test Setup        Team Assignment
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
    
    # ${result_tlead_uid}                  Get Lead Uid                         lead_name=${EXP_TLNAME}
    # ${result_loc_code}                   Get Loc Code                         loc_code=${EXP_LOC}    
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
    
    Check Team List Table                exp_tllbl=${EXP_TLLBL}        exp_namelbl=${EXP_TBL_NAMELBL}        exp_leadlbl=${EXP_TBL_TLLBL}        exp_loclbl=${EXP_TBL_LOCLBL}        exp_typelbl=${EXP_TBL_TYPELBL}        exp_statuslbl=${EXP_TBL_STATUSLBL}        exp_lupdlbl=${EXP_TBL_LSTUPDLBL}
    Search And Click Next                team_name=${TEAMNAME}
    Check View Update Section            exp_vulbl=${EXP_VULBL}        exp_vu_namelbl=${EXP_VU_NAMELBL}      exp_vu_tdlbl=${EXP_VU_TDLBL}        exp_vu_tllbl=${EXP_VU_TLLBL}        exp_vu_loclbl=${EXP_VU_LOCLBL}        exp_vu_typelbl=${EXP_VU_TYPELBL}        exp_vu_statuslbl=${EXP_VU_STATUSLBL}        exp_vu_lstupdlbl=${EXP_VU_LSTUPDLBL}






    



    # ${result}                            Get Lead Uid                         lead_name=${EXP_TLNAME}
#     Log Dictionary                       ${result}
#     Log To Console                       ${result}


#     # Comparison between UI and DB
#     Should Be Equal As Strings           ${team_details['Team Name']}        ${result['Team Name']}
#     Should Be Equal As Strings           ${team_details['Team Lead']}        ${result['Team Lead']}
#     Should Be Equal As Strings           ${team_details['Team Location']}    ${result['Team Location']}
    
    
#     ${result_uid}                        Get Agent Uid                       agent_name=${AGENT_NAME} 
#     Select Agent                         agent_name=${AGENT_NAME}            agent_uid=${result_uid}
                             
#     ${team_editor}                       Check Team Editor                   exp_falbl=${EXP_FALBL}             exp_trosterlbl=${EXP_TROSTERLBL}                      exp_fafltr=${EXP_FAFLTR}        exp_rosfltr=${EXP_ROSFLTR}
#     Log Dictionary                       ${team_editor}
#     Log To Console                       ${team_editor}
    
#     Unselect Agent                       agent_uid=${result_uid}



# Verify Saving of Agent to Team
#     [Setup]        User Team
#     [Teardown]     Logout

#     Select Team                          team_name=${TEAMNAME}

#     ${result_uid}                        Get Agent Uid                       agent_name=${AGENT_NAME} 
    
#     Assign Agent Input                   agent_name=${AGENT_NAME}            agent_uid=${result_uid}
#     ${result}                            Get Agent Team                      agent_name=${AGENT_NAME} 
#     Log Dictionary                       ${result}
#     Log To Console                       ${result}

#     Unselect Agent                       agent_uid=${result_uid}
#     Remove Agent                         agent_name=${AGENT_NAME}            agent_uid=${result_uid}
#     ${result}                            Get Agent Team                      agent_name=${AGENT_NAME} 
#     Log Dictionary                       ${result}
#     Log To Console                       ${result}




# Add Agent Team Assignment API
#     ${result_uid}                        Get Agent Uid                       agent_name=${AGENT_NAME}
#     ${result}                            Get User Team Db                    tname=${TEAMNAME}
#     ${response}                          Add Agent Api                       uid=${result_uid}                  teamId=${result['Team ID']}          
#     Log                                  ${response}
#     Log To Console                       ${response}
    
#     ${result}                            Get Agent Team                      agent_name=${AGENT_NAME} 
#     Log Dictionary                       ${result}
#     Log To Console                       ${result}



# Remove Agent Team Assignment API
#     ${result_uid}                        Get Agent Uid                       agent_name=${AGENT_NAME}
#     ${response}                          Remove Agent Api                    uid=${result_uid}        
#     Log                                  ${response}
#     Log To Console                       ${response}
    
#     ${result}                            Get Agent Team                      agent_name=${AGENT_NAME} 
#     Log Dictionary                       ${result}
#     Log To Console                       ${result}


Database Query
    ${result}                            Get User Team Db                   tname=${TEAMNAME}
    Log Dictionary                       ${result}
    Log To Console                       ${result}
    
#     ${result}                            Get Agent Team                      agent_name=${AGENT_NAME} 
#     Log Dictionary                       ${result}
#     Log To Console                       ${result}








