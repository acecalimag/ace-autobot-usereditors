*** Settings ***
Library     SeleniumLibrary
Library     DatabaseLibrary
Library     Collections
Resource    ../../../../Shared/Keywords/LoginPage.robot
Resource    ../../../../Shared/Keywords/Commands.robot
Resource    ../../Data/TestData.robot

*** Variables ***
#Scalar - Declare scalar variables here
${alert_list_expected_count}            ${3}
${alert_list_element}                   xpath:(//div[contains(@role,'alert')])
${select_all}                           //div[@class='dropdown-menu show']//button[@type='button'][normalize-space()='Select All']
${one_searched_agent}                   //div[@aria-expanded='true']//a[@role='option']
#List - Declare list variables here
&{test_restaurants}
...                                     one=*HOUSE OF CHINA*
...                                     two=ASIAN BOWL
...                                     three=SKT DEMO RESTAURANT
#Dictionaries - Declare dictionary variables here
&{auto_assign_webelements}
...                                     Restaurant List=css:.ant-select-selector
...                                     Go=css:.ant-btn.ant-btn-primary.AutoAssignFilterBar_button__3KiHS
...                                     Restaurant Name=xpath:(//th[@role='columnheader'])[2]
...                                     Auto Assign=xpath:(//th[@role='columnheader'])[3]
...                                     Tenure Required=xpath:(//th[@role='columnheader'])[4]
...                                     SP=xpath:(//th[@role='columnheader'])[5]
...                                     CH=xpath:(//th[@role='columnheader'])[6]
...                                     NW=xpath:(//th[@role='columnheader'])[7]
...                                     MGR=xpath:(//th[@role='columnheader'])[8]
...                                     PO=xpath:(//th[@role='columnheader'])[9]
...                                     SME=xpath:(//th[@role='columnheader'])[10]
...                                     CA=xpath:(//th[@role='columnheader'])[11]
...                                     CL=xpath:(//th[@role='columnheader'])[12]
...                                     TIER 3=xpath:(//th[@role='columnheader'])[13]
...                                     Save=xpath:(//button[@type='button'])[5]
...                                     Sync=xpath:(//button[@type='button'])[6]


${restaurant_header}                    xpath:(//th[@role='columnheader'])[2]
&{restaurant_cell_list}                 one=(//td[normalize-space()])[2]
...                                     two=(//td[normalize-space()])[4]
...                                     three=(//td[normalize-space()])[6]

${tenure_required_header}               xpath:(//th[@role='columnheader'])[4]
&{tenure_required_cell_list}                 one=(//td[contains(@role,'cell')])[4]
...                                     two=(//td[contains(@role,'cell')])[17]
...                                     three=(//td[contains(@role,'cell')])[30]

&{test_restaurant_headers}
...                                     Restaurant Name=xpath:(//th[@role='columnheader'])[2]
...                                     Auto Assign=xpath:(//th[@role='columnheader'])[3]
...                                     Tenure Required=xpath:(//th[@role='columnheader'])[4]
...                                     SP=xpath:(//th[@role='columnheader'])[5]
...                                     CH=xpath:(//th[@role='columnheader'])[6]
...                                     NW=xpath:(//th[@role='columnheader'])[7]
...                                     MGR=xpath:(//th[@role='columnheader'])[8]
...                                     PO=xpath:(//th[@role='columnheader'])[9]
...                                     SME=xpath:(//th[@role='columnheader'])[10]
...                                     CA=xpath:(//th[@role='columnheader'])[11]
...                                     CL=xpath:(//th[@role='columnheader'])[12]
...                                     TIER 3=xpath:(//th[@role='columnheader'])[13]

&{test_restaurant_cells}
...                                     Restaurant Name=xpath:(//td[normalize-space()])[2]
...                                     Auto Assign=xpath:(//input[contains(@type,'checkbox')])[1]
...                                     Tenure Required=xpath:(//td[contains(@role,'cell')])[4]
...                                     SP=xpath:(//input[contains(@type,'checkbox')])[2]
...                                     CH=xpath:(//input[contains(@type,'checkbox')])[3]
...                                     NW=xpath:(//input[contains(@type,'checkbox')])[4]
...                                     MGR=xpath:(//input[contains(@type,'checkbox')])[5]
...                                     PO=xpath:(//input[contains(@type,'checkbox')])[6]
...                                     SME=xpath:(//input[contains(@type,'checkbox')])[7]
...                                     CA=xpath:(//input[contains(@type,'checkbox')])[8]
...                                     CL=xpath:(//input[contains(@type,'checkbox')])[9]
...                                     TIER 3=xpath:(//input[contains(@type,'checkbox')])[10]

&{test_restaurant_value}
...                                     Restaurant Name=xpath:(//td[normalize-space()])[2]
...                                     Tenure Required=xpath:(//td[contains(@role,'cell')])[4]

${select_all}                           //div[@class='dropdown-menu show']//button[@type='button'][normalize-space()='Select All']
${restaurant_dropdown}                  //div[@class='ant-select-selection-overflow']
${search_agent}                         //div[@class='dropdown-menu show']//input[@aria-label='Search']
${search_agent_result}                  //div[@aria-expanded='true']//a[@role='option']
*** Keywords ***
Verify webelements are visible in Auto Assign Configuration
    [Documentation]    Verify webelements are visible in Restaurant Configuration
    FOR    ${key}    ${value}    IN     &{test_restaurants}
        click element       ${restaurant_dropdown}
        press keys          ${restaurant_dropdown}      ${value}
        click element       //div[contains(text(),'${value}')]
        click element       ${auto_assign_webelements}[Go]
    END
    Commands.Verify elements visibility with dictionary    &{auto_assign_webelements}
    Commands.Verify equal element count     ${alert_list_element}       ${alert_list_expected_count}

Display test restaurant
    click element       ${restaurant_dropdown}
    press keys          ${restaurant_dropdown}      ${data}[common][restaurant_name_no_RID]
    click element       //div[contains(text(),'${data}[common][restaurant_name_no_RID]')]
    click element       ${auto_assign_webelements}[Go]

Display three test restaurants
    FOR    ${key}    ${value}    IN     &{test_restaurants}
        click element       ${restaurant_dropdown}
        press keys          ${restaurant_dropdown}      ${value}
        click element       //div[contains(text(),'${value}')]
    END
    click element       ${auto_assign_webelements}[Go]
Verify sorting is working in Auto Assign Configuration page
    Verify sorting of columns with string values        ${restaurant_header}            &{restaurant_cell_list}
    Verify sorting of columns with string values           ${tenure_required_header}       &{tenure_required_cell_list}

Verify restaurants data for test restaurant
    Commands.Verify data of cells via dictionary      &{test_restaurant_value}
    ${test_restaurant_data}     create list
    FOR    ${key}       ${value}        IN      &{data}[value]
        append to list    ${test_restaurant_data}     ${value}
    END
    log to console      ${test_restaurant_data}
    lists should be equal           ${test_restaurant_data}     ${stored_data}
    AutoAssignKeywords.Verify correct checkbox status for test restaurant

Verify correct checkbox status for test restaurant
    FOR    ${key_status}    ${value_status}    IN    &{data}[expected_checkbox]
        FOR    ${key_list}    ${value_list}    IN    &{data}[actual_checkbox]
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
                        FATAL ERROR     ${key_status} is unchecked but should be checked    ${key_status} is checked but should be unchecked
                    END
                END
            END
        END
    END