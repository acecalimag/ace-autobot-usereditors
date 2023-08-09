*** Settings ***
Library    TeamAssignmentLibrary
Library    TeamAssignmentLibrary.DatabaseLibrary
Library    TeamAssignmentLibrary.APILibrary
Library    RequestsLibrary
Library    SeleniumLibrary
Library    Collections



*** Variables ***



*** Test Cases ***
Team Assignment
#   
    Open Config In Browser
    Login                                username=acalimag            password=kjt
    Open Page
    
    Select Team                          team_name=Xrp
    ${team_details}                      Check Team Details                   exp_name=Xrp              exp_lead=Adam Warlock            exp_loc=DGT
    Log Dictionary                       ${team_details}
    Log To Console                       ${team_details}
    
    ${result}                            Get Teamassignment Db                tname=Xrp
    Log Dictionary                       ${result}
    Log To Console                       ${result}


    # Comparison between UI and DB
    Should Be Equal As Strings           ${team_details['Team Name']}        ${result['Team Name']}
    Should Be Equal As Strings           ${team_details['Team Lead']}        ${result['Team Lead']}
    Should Be Equal As Strings           ${team_details['Team Location']}    ${result['Team Location']}


    # Verify completeness of fields, labels, and buttons for Team Assignment Editor Page
    ${result_uid}                        Get Agent Uid                       agent_name=kleo4 test
    Select Agent                         agent_uid=${result_uid}
                             
    ${team_editor}                       Check Team Editor                   exp_falbl=Free Agents             exp_trosterlbl=${result['Team Name']} Roster                       exp_fafltr=Filter Free Agents        exp_rosfltr=Filter Rostered Agents
    Log Dictionary                       ${team_editor}
    Log To Console                       ${team_editor}
    
    Unselect Agent                       agent_uid=${result_uid}
    Sleep                                10s

    # Add Agent Team Assignment
    ${result_uid}                        Get Agent Uid                       agent_name=kleo4 test
    Select Agent                         agent_uid=${result_uid}
    Assign Agent                         agent_uid=${result_uid}
    Sleep    5s


    # Remove Agent Team Assignment
    ${result_uid}                        Get Agent Uid                       agent_name=kleo4 test
    Unselect Agent                       agent_uid=${result_uid}
    Sleep    5s
    Remove Agent                         agent_name=kleo4 test               agent_uid=${result_uid}


    # # Add Agent Team Assignment by Input
    # ${result_uid}                        Get Agent Uid                       agent_name=kleo4 test
    # Assign Agent Input                   agent_name=kleo4 test               agent_uid=${result_uid}


    # # Remove Agent Team Assignment
    # ${result_uid}                        Get Agent Uid                       agent_name=kleo4 test
    # Remove Agent                         agent_name=kleo4 test               agent_uid=${result_uid}


    # Sleep    10


Add Agent Team Assignment API
    ${result_uid}                        Get Agent Uid                       agent_name=kleo4 test
    ${result}                            Get Teamassignment Db               tname=Xrp
    ${response}                          Add Agent Api                       uid=${result_uid}          teamId=${result['Team ID']}          
    Log                                  ${response}
    Log To Console                       ${response}


Remove Agent Team Assignment API
    ${result_uid}                        Get Agent Uid                       agent_name=kleo4 test
    ${response}                          Remove Agent Api                    uid=${result_uid}        
    Log                                  ${response}
    Log To Console                       ${response}


Database Query
    ${result}                            Get Teamassignment Db        tname=Y test
    Log Dictionary                       ${result}
    Log To Console                       ${result}
    








