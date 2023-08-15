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

Verify completeness of fields, labels, and buttons for Team Assignment Editor Page
    [Setup]        User Team
    [Teardown]     Logout
    
    ${result_tlead_uid}                  Get Lead Uid                         lead_name=${EXP_TLNAME}
    ${result_loc_code}                   Get Loc Code                         loc_code=${EXP_LOC}    
    Search And Click Next                team_name=${TEAMNAME}
    ${team_details}                      Check Team Details                   exp_name=${TEAMNAME}    exp_desc=Test Team    exp_lead=${EXP_TLNAME}    exp_lead_uid=${result_tlead_uid}    exp_loc=${EXP_LOC}    exp_loc_code=${result_loc_code}    exp_type=${EXP_TYPE}    exp_last_upd=${EXT_LAST_UPD}
    Log Dictionary                       ${team_details}
    Log To Console                       ${team_details}
    
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


# Database Query
#     ${result}                            Get User Team Db                   tname=${TEAMNAME}
#     Log Dictionary                       ${result}
#     Log To Console                       ${result}
    
#     ${result}                            Get Agent Team                      agent_name=${AGENT_NAME} 
#     Log Dictionary                       ${result}
#     Log To Console                       ${result}








