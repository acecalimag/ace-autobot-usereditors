*** Settings ***
Library     SeleniumLibrary
Library     DatabaseLibrary
Library     Collections
Resource    ../../../../Shared/Keywords/LoginPage.robot
Resource    ../../../../Shared/Keywords/Commands.robot
Resource    ../../Data/TestData.robot

*** Variables ***
#Scalar - Declare scalar variables here
${restaurant_dropdown}                  xpath://div[@class='filter-option']
${restaurant_list}                      xpath://select[@id="restaurant-filter"]
${select_all}                           xpath://button[normalize-space()='Select All']
${deselect_all}                         xpath://button[normalize-space()='Deselect All']
${go_button}                            xpath://button[@id='display-restaurants-btn']
${success_message}                      xpath:(//div[@class='toast-header bg-success text-white'])[1]
${search_restaurant}                    xpath://input[@aria-label='Search']
#List - Declare list variables here
@{test_restaurant_data}                 ASIAN BOWL (R88207)
...                                     148
...                                     10
@{edited_test_restaurant_data}          ASIAN BOWL (R88207)
...                                     1
...                                     2
#Dictionaries - Declare dictionary variables here
&{test_restaurants}
...                                     *HOUSE OF CHINA*=7f03b0f8-fef8-11e8-8435-0af3d8aa5476
...                                     ASIAN BOWL=209ce5ef-e9d3-11e4-b5e5-80ee733c5b56
...                                     SKT DEMO RESTAURANT=3f00ecca-6645-4cce-95e7-33b697abbeba
&{restaurant_config_webelements}
...                                     restaurantFilter=xpath://div[@class='filter-option']
...                                     goButton=xpath://button[@id='display-restaurants-btn']
...                                     restaurantHeader=xpath:(//div[@class='relative'])[76]
...                                     minimumAgentsHeader=xpath:(//div[@class='relative'])[39]
...                                     maximumAgentsHeader=xpath:(//div[@class='relative'])[40]
...                                     save=xpath:(//button[normalize-space()='SAVE'])[1]
...                                     alert=xpath://div[@role='alert']

${restaurant_header}                    xpath:(//div[@class='relative'])[72]
&{restaurant_cell_list}                 one=(//th)[5]/following-sibling::td[1]
...                                     two=(//th)[6]/following-sibling::td[1]
...                                     three=(//th)[7]/following-sibling::td[1]

${maa_header}                           xpath:(//div[@class='relative'])[37]
&{maa_cell_list}                        one=(//th)[5]/following-sibling::td[2]
...                                     two=(//th)[6]/following-sibling::td[2]
...                                     three=(//th)[7]/following-sibling::td[2]

${mba_header}                           xpath:(//div[@class='relative'])[38]
&{mba_cell_list}                        one=(//th)[5]/following-sibling::td[3]
...                                     two=(//th)[6]/following-sibling::td[3]
...                                     three=(//th)[7]/following-sibling::td[3]

&{restaurant_data}
...                                     name=(//th)[5]/following-sibling::td[1]
...                                     maa=(//th)[5]/following-sibling::td[2]
...                                     mba=(//th)[5]/following-sibling::td[3]
&{default_test_restaurant_data}         name=ASIAN BOWL (R88207)
...                                     maa=148
...                                     mba=10
&{modified_test_restaurant_data}        name=ASIAN BOWL (R88207)
...                                     maa=1
...                                     mba=2
*** Keywords ***

LoginPage.Login as
Verify webelements are visible in Restaurant Configuration
    [Documentation]    Verify webelements are visible in Restaurant Configuration
    Commands.Select all and display     ${restaurant_dropdown}      ${select_all}       ${go_button}
    Commands.Verify elements visibility with dictionary    &{restaurant_config_webelements}

Verify sorting of columns in Restaurant Configuration
    Click element       ${restaurant_dropdown}
    FOR     ${restaurant}  ${value}     IN     &{test_restaurants}
        select from list by value       ${restaurant_list}      ${value}
    END
    Click button        ${go_button}
    Commands.Verify sorting of columns with string values       ${restaurant_header}        &{restaurant_cell_list}
#    Commands.Verify sorting of columns with int values          ${maa_header}               &{maa_cell_list}
#    Commands.Verify sorting of columns with int values          ${mba_header}               &{mba_cell_list}
Verify data of restaurant via list
    [Arguments]     &{cells}
    @{stored_data}    create list
    FOR     ${key}  ${value}        IN      &{cells}
    ${cell_value}     get text        ${value}
    append to list      ${stored_data}       ${cell_value}
    END
    log to console    Cell value list: @{stored_data}
    set global variable     @{stored_data}

Verify restaurant's data
    Click element       ${restaurant_dropdown}
    input text          ${search_restaurant}        ${data}[common][restaurant_name]
    click element       //span[contains(text(),'${data}[common][restaurant_name]')]
    Click button        ${go_button}
    Verify data of restaurant via list      &{restaurant_data}
    log to console    Test restaurant data: ${test_restaurant_data}
    lists should be equal    ${stored_data}     ${test_restaurant_data}
    log to console      Restaurant data is correct

Verify saving feature
    #MODIFIED
    Update MAA and MBA      ${modified_test_restaurant_data}[maa]       ${modified_test_restaurant_data}[mba]
    Verify data of restaurant via list      &{restaurant_data}
    log to console    Modified restaurant data: ${edited_test_restaurant_data}
    lists should be equal    ${stored_data}     ${edited_test_restaurant_data}
    log to console      Restaurant data is modified successfully
    #REVERT BACK
    Update MAA and MBA      ${default_test_restaurant_data}[maa]       ${default_test_restaurant_data}[mba]
    Verify data of restaurant via list      &{restaurant_data}
    log to console    Test restaurant data: ${test_restaurant_data}
    lists should be equal    ${stored_data}     ${test_restaurant_data}
    log to console      Restaurant data is reverted back to its original value

Update MAA and MBA
    [Arguments]     ${maa}      ${mba}
    #Modify data
    press keys      ${restaurant_data}[maa]     ${maa}
    press keys      ${restaurant_data}[maa]     ENTER
    press keys      ${restaurant_data}[mba]     ${mba}
    press keys      ${restaurant_data}[mba]     ENTER
    click element       ${restaurant_config_webelements}[save]
    wait until element is visible           ${success_message}


