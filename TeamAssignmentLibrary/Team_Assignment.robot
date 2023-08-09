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

    
    # ${team_name}                         Set Variable                        ${result['Team Name']} Roster
    ${team_editor}                       Check Team Editor                   exp_falbl=Free Agents            exp_trosterlbl=${result['Team Name']} Roster        exp_fafltr=Filter Free Agents        exp_rosfltr=Filter Rostered Agents
    Log Dictionary                       ${team_editor}
    Log To Console                       ${team_editor}

    ${result_uid}                        Get Agent Uid                       agent_name=kleo4 test
    Assign Agent                         agent_name=kleo4 test               agent_uid=${result_uid}


    # Sleep    10


Add Agent Team Assignment API
    ${response}                          Add Agent Api                uid=8f5ac28b-b9af-11e2-b3e7-80ee733c5b56          teamId=53447587-455a-4713-827c-79fd4f43f70c
    Log                                  ${response}
    Log To Console                       ${response}


Remove Agent Team Assignment API
    ${response}                          Remove Agent Api             uid=8f5ac28b-b9af-11e2-b3e7-80ee733c5b56
    Log                                  ${response}
    Log To Console                       ${response}


Database Query
    ${result}                            Get Teamassignment Db        tname=Y test
    Log Dictionary                       ${result}
    Log To Console                       ${result}
    








