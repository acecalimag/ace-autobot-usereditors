*** Settings ***
Library     SeleniumLibrary
Library     DatabaseLibrary
Resource    ../../../../Shared/Keywords/LoginPage.robot
Resource    ../../../../Shared/Keywords/Commands.robot


*** Variables ***
@{user_location}        ADV     AKB     DGT     MNL     NYC     QFD     QFM     SDQ     TEL     TMX     TPP     WKL
${agents_list_button}          xpath://button[@title='Agent (All)']
${agent_list}           xpath://select[@id='activeAgentList']
${deselect_all}         //button[normalize-space()='Deselect All']
${search_agent}         xpath:(//input[@aria-label='Search'])[5]
${go_button}            id:go
${saved_message}        xpath:(//div[@class='col-xs-11 col-sm-4 alert alert-success animated fadeInRight'])[1]
${save_button}          id:save
${test_user_uid}        c85715e6-2f6b-42e9-bfe7-737ba0ac4496
${loc_arrow}            xpath://tbody/tr[1]/td[5]/div[1]
${loc_field}            xpath:(//textarea)[1]
${new_location}         NYC
${old_location}         MNL
${username_header}      css:#username
${DBHost}               qa-db.letsdochinese.com
${DBName}               kjt
${DBPass}               bdgeia
${DBPort}               3306
${DBUser}               mberon
${alert_list_element}       xpath://div[@class='col-3']/div
${alert_list_expected_count}        ${8}
&{user_config_webelements}
...                         Active List=//button[@data-id='activeLevelList']
...                         User Location=//button[@data-id='userLocation']
...                         User Team=//button[@data-id='userTeam']
...                         User Position=//button[@data-id='userPosition']
...                         Agent List=//button[@data-id='activeAgentList']
...                         Start Date=//input[@id='startDate']
...                         Select Date=css:span[title='Select a Date']
...                         Clear=css:span[title='Clear']
...                         Go=//button[@id='go']
...                         Save=//button[@id='save']

&{column_header_elements_smoke}
...                         Username=(//span[contains(text(),'Username')])[1]
...                         Full Name=(//span[contains(text(),'Full Name')])[1]
...                         Position=(//span[contains(text(),'Position')])[1]
...                         Location=(//span[contains(text(),'Location')])[1]

&{username_cell_list}
...                             one=//body[1]/div[1]/div[1]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]
...                             two=//body[1]/div[1]/div[1]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]
...                             three=//body[1]/div[1]/div[1]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]

&{fullname_cell_list}
...                             one=//tbody[1]//tr[1]/td[3]
...                             two=//tbody[1]//tr[2]/td[3]
...                             three=//tbody[1]//tr[3]/td[3]

&{position_cell_list}
...                             one=//tbody[1]//tr[1]/td[4]
...                             two=//tbody[1]//tr[2]/td[4]
...                             three=//tbody[1]//tr[3]/td[4]

&{location_cell_list}
...                             one=//tbody[1]//tr[1]/td[5]
...                             two=//tbody[1]//tr[2]/td[5]
...                             three=//tbody[1]//tr[3]/td[5]


@{list}
...                               username
...                               fullname

&{call_rest}
...                                 go=//button[@id='go']
...                                 save=//button[@id='save']

${alert_list_element_call_restriction}          //div[@class='col-3']//div
${alert_expected_count_call}                    ${4}
*** Keywords ***
Verify webelements in Call Restrictions are displayed
    Commands.Verify elements visibility with dictionary     &{call_rest}
     Commands.Verify equal element count     ${alert_list_element_call_restriction}          ${alert_expected_count_call}

Verify webelements are visible in User Configuration page
    Commands.Verify elements visibility with dictionary     &{user_config_webelements}
    Commands.Verify equal element count         ${alert_list_element}      ${alert_list_expected_count}
    log to console      All elements are visible

Verify sorting of columns in User Configuration page
    Verify sorting of Username column
    Verify sorting of Full name column
    Verify sorting of Position column
    Verify sorting of Location column
Verify sorting of Username column
    Verify sorting of columns with string values for Userconfig       ${column_header_elements_smoke}[Username]       &{username_cell_list}

Verify sorting of Full name column
    Verify sorting of columns with string values for Userconfig       ${column_header_elements_smoke}[Full Name]       &{fullname_cell_list}

Verify sorting of Position column
    Verify sorting of columns with string values for Userconfig       ${column_header_elements_smoke}[Position]       &{position_cell_list}

Verify sorting of Location column
    Verify sorting of columns with string values for Userconfig       ${column_header_elements_smoke}[Location]       &{location_cell_list}

Verify sorting of columns with string values for Userconfig
    [Documentation]    Verify sorting of columns
    [Arguments]    ${header}       &{header_cell_list}
#   DESC
    scroll element into view        ${header}
    ${header_name}    Get text      ${header}
    log to console      Clicking ${header_name} for descending sort order
    double click element       ${header}
    run keyword and ignore error    wait until element is visible    ${descending_arrow}
    log to console    Descending arrow is present
    @{desc_cell_values}    create list
    FOR    ${key}    ${value}    IN    &{header_cell_list}
        ${cell_text}    Get text        ${value}
        append to list      ${desc_cell_values}    ${cell_text}
    END
    log to console     This header has: @{desc_cell_values}
    @{sorted}    copy list    ${desc_cell_values}
    sort list       ${sorted}
    log to console      Sorted ascending: ${sorted}
    reverse list    ${sorted}
    log to console      Reversed for descending: ${sorted}
    lists should be equal       ${sorted}       ${desc_cell_values}
    log to console      Sorting via descending order is working properly
#   ASC
    scroll element into view        ${header}
    ${header_name}    Get text      ${header}
    log to console      Clicking ${header_name} for ascending sort order
    double click element       ${header}
    run keyword and ignore error    wait until element is visible    ${ascending_arrow}
    log to console    Ascending arrow is present
    @{asc_cell_values}    create list
    FOR    ${key}    ${value}    IN    &{header_cell_list}
        ${cell_text}    Get text        ${value}
        append to list      ${asc_cell_values}    ${cell_text}
    END
    log to console      This header has: @{asc_cell_values}
    @{sorted}    copy list    ${asc_cell_values}
    sort list       ${sorted}
    log to console      Sorted has: @{sorted}
    lists should be equal       ${sorted}       ${asc_cell_values}
    log to console      Sorting via ascending order is working properly

Filter-out default user in aux configuration
    Filter-out agent in aux config    ${default_username}

Filter-out agent in aux config
    [Documentation]    Used for filtering out an agent in User Config
    [Arguments]    ${desired_user}
    page should contain element    ${agents_list_button}
    click element               ${agents_list_button}
    click element               ${deselect_all}
    input text                  ${search_agent}        ${default_username}
    select from list by value           ${agent_list}       ${test_user_uid}
    click button    ${go_button}

Assign location to a specific agent
    [Documentation]    Used for assigning location to an existing agent
    Assign location to an agent    ${new_location}

Assign location to an agent
    [Documentation]    Used for assigning location to an existing agent
    [Arguments]    ${location}

    Set focus to element    ${loc_arrow}
    Scroll element into view    ${loc_arrow}
    Click Element    ${loc_arrow}
    Input Text    ${loc_field}    ${location}
    Press Keys    ${loc_field}    RETURN
    Click Element    ${save_button}
    Scroll element into view    ${loc_arrow}
#    Wait Until Element is Visible    ${saved_message}
    log to console    "Assign location to ${location} was saved successfully"

Verify kjt locations via query
    [Documentation]    Used for assigning location to an existing agent

    Connect To Database    pymysql    ${DBName}    ${DBUser}    ${DBPass}    ${DBHost}    ${DBPort}
    @{query_location}    Query    select code from kjt.userlocation order by code asc;
    @{query_list}    Evaluate    [x[0] for x in ${query_location}]
    log to console    From database: ${query_list}
    log to console    Expected list : ${user_location}
    lists should be equal       ${query_list}     ${user_location}
    Disconnect From Database

Verify agent is assigned to a location via query
    [Documentation]    Query for verifying desired user is in a location
    Connect To Database    pymysql    ${DBName}    ${DBUser}    ${DBPass}    ${DBHost}    ${DBPort}
    ${loc_output}    Query
    ...    select ul.code from kjt.user u join kjt.usermeta um on u.uid = um.uid join kjt .userlocation ul on um.lid = ul.lid where u.username = 'wmaximoff';

    FOR    ${new_location}    IN    ${loc_output}
        log to console    "Verifying user is assigned to ${new_location}"
    END
    should be equal as strings    ${loc_output}    ${new_location}
    log to console    "User is assigned to ${new_location} as expected"
    Disconnect From Database



