*** Settings ***
Library     SeleniumLibrary
Library     DatabaseLibrary
Library     Collections
Library     ../../../Custom/AuxConfiguration.py
Resource    ../../../../Shared/Keywords/LoginPage.robot
Resource    ../../../../Shared/Keywords/Navigation.robot
Resource    ../../../../Shared/Keywords/Commands.robot
Resource    ../../Data/TestData.robot


*** Variables ***
#Scalar - Declare scalar variables here
${aux_configuration_editor}     Aux Configuration
${aux_configuration}            css:.navbar-brand
${dropdown_list}                css:div.multiselect-dropdown
${header_list}                  css:div[class='ht_clone_top handsontable'] th
${dropdown_count}               ${4}
${header_count}                 ${19}
${license_web}                  css:#hot-display-license-info
${license_expected}
...                             The license key for Handsontable is invalid. Read more on how to install it properly or contact us at support@handsontable.com.
${status_dropdown}              xpath:(//span[@class='dropdown-btn'])[1]
${location_dropdown}            xpath:(//span[@class='dropdown-btn'])[2]
${position_dropdown}            xpath:(//span[@class='dropdown-btn'])[3]
${agent_search_result}          xpath://div[normalize-space()='B110 - B110']
${user_B110}                    B110
${logout_checkbox}              xpath:(//input[@type='checkbox'])[625]
${ready_checkbox}               xpath:(//input[@type='checkbox'])[626]
${callback_checkbox_id}         623
${checked_checkbox}             Checked
${unchecked_checkbox}           Unchecked
${save}                         xpath://button[normalize-space()='Save']
${saved_successfully}            //div[@aria-label='Saved Successfully!']

#List - Declare list variables here
@{user_list}
...                             b110
...                             B110
...                             General
...                             MNL
...                             ${EMPTY}
...                             90004
...                             16775553-51c6-4282-8080-306f7953b9df

#Dictionaries - Declare dictionary variables here
&{aux_webelements}
...                             startDate=css:input[placeholder='Start Date']
...                             selectDate=css:a[title='Select a Date']
...                             clearDate=css:a[title='Clear']
...                             headerList=css:div[class='ht_clone_top handsontable'] th
...                             saveButton=xpath://button[normalize-space()='Save']
...                             go=xpath://button[normalize-space()='GO!']
&{status_list}                  active=xpath://div[normalize-space()='Active']
...                             inactive=//div[normalize-space()='Inactive']
...                             all=xpath://div[normalize-space()='All']
&{position_list}                Position (All)=//div[normalize-space()='Position (All)']
...                             Client Success=//div[normalize-space()='Client Success']
...                             Client Success Asst=//div[normalize-space()='Client Success Asst']
...                             Client Tech=//div[normalize-space()='Client Tech']
...                             Data Content=//div[normalize-space()='Data Content']
...                             Engineering=//div[normalize-space()='Engineering']
...                             Finance=//div[normalize-space()='Finance']
...                             General=//div[normalize-space()='General']
...                             HR & Recruiting=//div[normalize-space()='HR & Recruiting']
...                             Managerial=//div[normalize-space()='Managerial']
...                             Mentor=//div[normalize-space()='Mentor']
...                             Quality=//div[normalize-space()='Quality']
...                             Sales & Marketing=//div[normalize-space()='Sales & Marketing']
...                             Spanish CSR=//div[normalize-space()='Spanish CSR']
...                             Subject Matter Exp=//div[normalize-space()='Subject Matter Exp']
...                             Team Lead=//div[normalize-space()='Team Lead']
...                             Tier I CSR=//div[normalize-space()='Tier I CSR']
...                             Tier II CSR=//div[normalize-space()='Tier II CSR']
...                             Tier III CSR=//div[normalize-space()='Tier III CSR']
...                             Tier IV CSR=//div[normalize-space()='Tier IV CSR']
...                             Trainee=//div[normalize-space()='Trainee']
...                             Training=//div[normalize-space()='Training']
...                             Workforce=//div[normalize-space()='Workforce']
&{location_list}
...                             Office (All)=//div[normalize-space()='Office (All)']
...                             ADV=//div[normalize-space()='ADV']
...                             AKB=//div[normalize-space()='AKB']
...                             DGT=//div[normalize-space()='DGT']
...                             MNL=//div[normalize-space()='MNL']
...                             NYC=//div[normalize-space()='NYC']
...                             QFD=//div[normalize-space()='QFD']
...                             QFM=//div[normalize-space()='QFM']
...                             SDQ=//div[normalize-space()='SDQ']
...                             TEL=//div[normalize-space()='TEL']
...                             TMX=//div[normalize-space()='TMX']
...                             TPP=//div[normalize-space()='TPP']
...                             WKL=//div[normalize-space()='WKL']
&{content_webelements}
...                             Username=b110
...                             Full Name=B110
...                             Position=General
...                             Location=MNL
...                             Start Date=
...                             Workforce Id=90004
...                             UID=16775553-51c6-4282-8080-306f7953b9df
&{aux_checkbox_list}
...                             622=Mgmt
...                             623=Callback
...                             624=Wonders
...                             625=Coaching
...                             626=Pullout
...                             627=Sbs
...                             628=Meeting
...                             629=Restroom
...                             630=Other

&{checkbox_list}
...                             mgmt=xpath:(//input[@type='checkbox'])[622]
...                             callback=xpath:(//input[@type='checkbox'])[623]
...                             wonders=xpath:(//input[@type='checkbox'])[624]
...                             coaching=xpath:(//input[@type='checkbox'])[625]
...                             pullout=xpath:(//input[@type='checkbox'])[626]
...                             sbs=xpath:(//input[@type='checkbox'])[627]
...                             meeting=xpath:(//input[@type='checkbox'])[628]
...                             restroom=xpath:(//input[@type='checkbox'])[629]
...                             other=xpath:(//input[@type='checkbox'])[630]

${username_header}              (//div[@class='relative'])[109]
&{username_cell_list}           one=(//th)[20]/following-sibling::td[1]
...                             two=(//th)[21]/following-sibling::td[1]
...                             three=(//th)[22]/following-sibling::td[1]

${fullname_header}              (//div[@class='relative'])[110]
&{fullname_cell_list}           one=(//th)[20]/following-sibling::td[2]
...                             two=(//th)[21]/following-sibling::td[2]
...                             three=(//th)[22]/following-sibling::td[2]

${position_header}              (//div[@class='relative'])[56]
&{position_cell_list}           one=(//th)[20]/following-sibling::td[3]
...                             two=(//th)[21]/following-sibling::td[3]
...                             three=(//th)[22]/following-sibling::td[3]

${location_header}              (//div[@class='relative'])[57]
&{location_cell_list}           one=(//th)[20]/following-sibling::td[4]
...                             two=(//th)[21]/following-sibling::td[4]
...                             three=(//th)[22]/following-sibling::td[4]

${startdate_header}             (//div[@class='relative'])[58]
&{startdate_cell_list}          one=(//th)[20]/following-sibling::td[5]
...                             two=(//th)[21]/following-sibling::td[5]
...                             three=(//th)[22]/following-sibling::td[5]

${workforce_header}             (//div[@class='relative'])[59]
&{workforce_cell_list}          one=(//th)[20]/following-sibling::td[6]
...                             two=(//th)[21]/following-sibling::td[6]
...                             three=(//th)[22]/following-sibling::td[6]

${uid_header}                   (//div[@class='relative'])[71]
&{uid_cell_list}                one=(//th)[20]/following-sibling::td[18]
...                             two=(//th)[21]/following-sibling::td[18]
...                             three=(//th)[22]/following-sibling::td[18]



*** Keywords ***
Verify Sorting of Aux Configuration Columns
#    Verify sorting of UID column
    Verify sorting of Location column
    Verify sorting of Position column
    Verify sorting of Full Name column
    Verify sorting of Username column
#    Verify sorting of Workforce ID column

Verify sorting of Username column
    Commands.Verify sorting of columns with string values        ${username_header}      &{username_cell_list}
    Reload page
    Select Aux Configuration Frame
Verify sorting of Full Name column
    Commands.Verify sorting of columns with string values        ${fullname_header}      &{fullname_cell_list}
    Reload page
    Select Aux Configuration Frame
Verify sorting of Position column
    Commands.Verify sorting of columns with string values       ${position_header}      &{position_cell_list}
    Reload page
    Select Aux Configuration Frame
Verify sorting of Location column
    Commands.Verify sorting of columns with string values        ${location_header}      &{location_cell_list}
    Reload page
    Select Aux Configuration Frame
#Verify sorting of Start date column
#    Commands.Verify sorting of columns with int values           ${startdate_header}     &{startdate_cell_list}
Verify sorting of Workforce ID column
    Commands.Verify sorting of columns with int values           ${workforce_header}     &{workforce_cell_list}
    Reload page
    Select Aux Configuration Frame
Verify sorting of UID column
    Commands.Verify sorting of columns with string values        ${uid_header}           &{uid_cell_list}
    Reload page
    Select Aux Configuration Frame

Pull content from an agent in aux config
    [Documentation]    Verify cells' content are correct
    [Arguments]    &{content_list}

    @{cell_value}    create list
    FOR    ${key}    ${values}    IN    &{content_list}
        element should be visible    //td[contains(text(),'${values}')]
        append to list      ${cell_value}    ${values}
    END
    log to console    Cell value list: @{cell_value}
    set global variable    @{cell_value}

Verify saving checkbox modification
    FOR    ${key}    ${value}    IN    &{checkbox_list}
            Click element       ${value}
    END
    Click element       ${save}
    run keyword and ignore error    Wait until element is visible       ${saved_successfully}
    log to console      Saved initial modifications for checkboxes
    FOR    ${key}    ${values}    IN    &{aux_checkbox_list}
    @{checkbox_values}      Create list
        IF      ${key}==${callback_checkbox_id}
            ${Is_Checkbox_Selected}    Run Keyword And Return Status    Checkbox Should Be Selected    xpath:(//input[@type='checkbox'])[${key}]
            ${Actual_Chkbx_Value}    Run Keyword If    '${Is_Checkbox_Selected}'== 'True'    Set Variable    Checked
            ...    ELSE IF      '${Is_Checkbox_Selected}'== 'False'    Set Variable    Unchecked
            Run Keyword If      '${agent_alpha}[checkbox_status][callback]'!='${Actual_Chkbx_Value}'    Log to console      ${values} should be checked but it was not
            Run Keyword If      '${checked_checkbox}'!='${Actual_Chkbx_Value}'    Click Element    xpath:(//input[@type='checkbox'])[${key}]
        ELSE
            ${Is_Checkbox_Not_Selected}    Run Keyword And Return Status    Checkbox Should Not Be Selected    xpath:(//input[@type='checkbox'])[${key}]
            ${Actual_Chkbx_Value}    Run Keyword If    '${Is_Checkbox_Not_Selected}'== 'True'    Set Variable    Unchecked
            ...    ELSE IF      '${Is_Checkbox_Not_Selected}'== 'False'    Set Variable    Checked

            Run Keyword If      '${unchecked_checkbox}'!='${Actual_Chkbx_Value}'    Log to console      ${values} should not be checked but was checked
            Run Keyword If      '${unchecked_checkbox}'!='${Actual_Chkbx_Value}'    Unselect checkbox   xpath:(//input[@type='checkbox'])[${key}]
        END
    END
    Click element       ${save}
    run keyword and ignore error    Wait until element is visible       ${saved_successfully}
    log to console      Saved final modifications for checkboxes

Verify correct checkbox status for agent
    FOR    ${key_status}    ${value_status}    IN    &{agent_alpha}[checkbox_status]
        FOR    ${key_list}    ${value_list}    IN    &{checkbox_list}
            IF    '${key_status}'=='${key_list}'
                IF      '${value_status}'=='Checked'
                    TRY
                        Checkbox Should Be Selected     ${value_list}
                        log to console    ${key_status} is checked as expected
                    EXCEPT
                        FATAL ERROR     ${key_status} is unchecked but should be checked
                    END
                ELSE IF     '${value_status}'=='Unchecked'
                    TRY
                        Checkbox Should Not Be Selected     ${value_list}
                        log to console    ${key_status} is unchecked as expected
                    EXCEPT
                        FATAL ERROR     ${key_status} is checked but should be unchecked
                    END
                END

            END
        END
    END

Verify webelements are visible
    [Documentation]    Verifying webelements of Aux Config page are visible

    Commands.Verify equal element count    ${dropdown_list}    ${dropdown_count}
    Commands.Verify equal element count    ${header_list}    ${header_count}
    Commands.Verify equal text    ${license_web}    ${license_expected}
    Commands.Verify elements visibility with dictionary    &{aux_webelements}
    Commands.Verify elements visibility with dictionary in a dropdown    ${status_dropdown}         &{status_list}
    Commands.Verify elements visibility with dictionary in a dropdown    ${location_dropdown}       &{location_list}
    Commands.Verify elements visibility with dictionary in a dropdown    ${position_dropdown}       &{position_list}

Verify agent's data
    Commands.Search for an agent    ${agent_alpha}[agent_details][fullname]    ${agent_search_result}
    AuxConfigurationKeywords.Pull content from an agent in aux config    &{agent_alpha}[agent_details]
    log to console      Default user list: ${user_list}
    lists should be equal       ${cell_value}       ${user_list}
    log to console      Verified that ${agent_alpha}[agent_details][fullname] has the correct details


