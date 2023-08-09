*** Settings ***
Library     SeleniumLibrary
Library     DatabaseLibrary
Library     String
Library     Collections
Resource    Navigation.robot

*** Variables ***
${iframe_aux}               xpath:(//iframe)[1]
${iframe_auto}              //div[@id='react-app']//iframe
${iframe_agent}             xpath:(//agentrankingiframe)[1]
${agent_search}             css:input[placeholder='Select Agent']
${agent_dropdown}           xpath:(//span[@class='dropdown-multiselect__caret'])[4]
${go}                       xpath://button[normalize-space()='GO!']
${QA_RESTO}
${userconfig_tag}           user-configuration
${auxconfig_tag}            aux-configuration
${restaurantconfig_tag}     restaurant-configuration
${2}                        2 seconds
${spinner_loading}          //i[@class='fa fa-spinner fa-pulse fa-spin fa-5x']
${ascending_arrow}          //span[contains(@class, 'ascending')]
${descending_arrow}         //span[contains(@class, 'descending')]
${header_ascending}         div[class='ht_clone_top handsontable'] span[class='colHeader columnSorting sortAction ascending']
${user_config}              User Configuration
${aux_config}               Aux Configuration
${restaurant_config}        Restaurant Configuration
${auto_config}              Auto Assign Configuration
${agent_ranking}            Agent Ranking
${call_restriction}         Call Restriction
${restaurant_group_name}    Restaurant Group Name
${training_grps}            Training Groups
${team_assign}              Team Assignment
${user_teams}               User Teams

&{duration}
...                         ONE=1 second
...                         TWO=2 seconds
...                         THREE=3 seconds
...                         FIVE=5 seconds
...                         TEN=10 seconds

*** Keywords ***
Run keyword until succeeds
    [Arguments]     ${KW}       @{KWARGS}
    wait until keyword succeeds     30s     1s      ${KW}       @{KWARGS}

Go to Call Restriction editor
    [Documentation]    Selects the Call Restrictions editor
    Navigation.Select User Configuration editor      ${call_restriction}
    wait until page does not contain element        ${spinner_loading}

Go to Restaurant Group Name
    [Documentation]    Selects the Restaurant Group Name
    Navigation.Select User Configuration editor      ${restaurant_group_name}
    wait until page does not contain element        ${spinner_loading}

Go to Auto Assign editor
    [Documentation]    Selects the Auto Assign
    Navigation.Select User Configuration editor      ${auto_config}
    wait until page does not contain element        ${spinner_loading}
    Switch to frame via ID      ${iframe_auto}

Go to Agent Ranking editor
    [Documentation]    Selects the Agent Ranking editor
    Navigation.Select User Configuration editor      ${agent_ranking}
    wait until page does not contain element        ${spinner_loading}

Go to Restaurant Configuration editor
    [Documentation]    Selects the Restaurant Configuration editor
    Navigation.Select User Configuration editor      ${restaurant_config}
    wait until page does not contain element        ${spinner_loading}

Go to Aux Configuration editor
    [Documentation]    Selects the Aux Configuration editor
    Navigation.Select User Configuration editor    ${aux_config}
    wait until page does not contain element        ${spinner_loading}
    Select Aux Configuration Frame

Go to User Configuration editor
    [Documentation]    Selects the Aux Configuration editor
    Navigation.Select User Configuration editor    ${user_config}
    wait until page does not contain element        ${spinner_loading}

Unselect Aux Configuration Frame
    [Documentation]    Unselects Aux Config iframe
    unselect frame
    log to console    Successfully unselected to iframe with id: ${iframe_aux}

Select Aux Configuration Frame
    [Documentation]    Selects Aux Config iframe
    Switch to frame via ID    ${iframe_aux}
    log to console    Successfully switched to iframe with id: ${iframe_aux}

Switch to frame via ID
    [Documentation]    Selects iframe via id/xpath
    [Arguments]    ${iframe_id}
    select frame    ${iframe_id}

Verify data of cells via dictionary
    [Arguments]     &{cells}
    @{stored_data}    create list
    FOR     ${key}  ${value}        IN      &{cells}
        ${cell_value}     get text        ${value}
    append to list      ${stored_data}       ${cell_value}
    END
    log to console    Cell value list: @{stored_data}
    set global variable     @{stored_data}

Verify equal element count
    [Documentation]    Verifies if number of elements with the same class are equal with the expected value
    [Arguments]    ${list_element}    ${expected}

    ${actual}    get element count    ${list_element}
    log to console    Actual number of elements: ${actual}
    log to console    Expected number of elements: ${expected}
    should be equal    ${actual}    ${expected}

Verify equal text
    [Documentation]    Verifies equal text from page and expected
    [Arguments]    ${pageTextElement}    ${expectedText}

    ${textFromPage}    get text    ${page_text_element}
    log to console    Actual text: ${text_from_page}
    log to console    Expected text: ${expected_text}
    should be equal    ${text_from_page}    ${expected_text}

Verify elements visibility with dictionary in a dropdown
    [Documentation]    Verifies equal text from page and expected
    [Arguments]    ${dropdown}    &{list}
    Click element       ${dropdown}
    Verify elements visibility with dictionary  &{list}

Verify elements visibility with dictionary
    [Documentation]    Verifies elements are visible using a list
    [Arguments]    &{list}

    FOR    ${key}    ${element}    IN    &{list}
        commands.run keyword until succeeds     element should be visible    ${element}
        ${stripped_element}    strip string    ${element}    characters='
    END
    log to console    Dictionary with elements are displayed properly: &{list}

Select all and display
    [Documentation]    Verifies suer is able to display all data
    [Arguments]    ${dropdown}      ${select_all_element}     ${go_button}
    Click Element       ${dropdown}
    Click Element       ${select_all_element}
    Click Button        ${go_button}

Verify elements visibility with list
    [Documentation]    Verifies elements are visible using a list
    [Arguments]    @{list}

    FOR    ${element}    IN    @{list}
        element should be visible    ${element}
    END
    log to console    List with elements are displayed properly: @{list}
Search for an agent
    [Documentation]    Used for filtering out an agent in Aux Config
    [Arguments]    ${test_user}    ${result}
    Click Element    ${agent_dropdown}
    Click Element    ${agent_search}
    Input text    ${agent_search}    ${test_user}
    Click Element    ${result}
    click element    ${go}

Verify sorting of columns with string values
    [Documentation]    Verify sorting of columns
    [Arguments]    ${header}       &{header_cell_list}
#   ASC
    scroll element into view        ${header}
    ${header_name}    Get text      ${header}
    log to console      Clicking ${header_name} for ascending sort order
    click element       ${header}
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
#   DESC
    scroll element into view        ${header}
    ${header_name}    Get text      ${header}
    log to console      Clicking ${header_name} for descending sort order
    click element       ${header}
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

Verify sorting of columns with int values
    [Documentation]    Verify sorting of columns
    [Arguments]    ${header}  &{header_cell_list}

    run keyword and ignore error    wait until element is visible       ${header}
    scroll element into view        ${header}
    ${header_name}    Get text      ${header}
    log to console      Clicking ${header_name} for ascending sort order
    click element       ${header}
    run keyword and ignore error    wait until element is visible    ${ascending_arrow}
    log to console    Ascending arrow is present
    @{asc_cell_values}    create list
    FOR    ${key}    ${value}    IN    &{header_cell_list}
        ${cell_text}    Get text        ${value}
        append to list      ${asc_cell_values}    ${cell_text}
    END
    log to console      This header has: @{asc_cell_values}
    @{sorted}    Evaluate     sorted(${asc_cell_values}, key=int, reverse=False)
    log to console      Sorted has: @{sorted}
    lists should be equal       ${sorted}       ${asc_cell_values}
    log to console      Sorting via ascending order is working properly

#   DESC
    scroll element into view        ${header}
    ${header_name}    Get text      ${header}
    log to console      Clicking ${header_name} for descending sort order
    click element       ${header}
    run keyword and ignore error    wait until element is visible    ${descending_arrow}
    log to console    Descending arrow is present
    @{desc_cell_values}    create list
    FOR    ${key}    ${value}    IN    &{header_cell_list}
        ${cell_text}    Get text        ${value}
        append to list      ${desc_cell_values}    ${cell_text}
    END
    log to console     This header has: @{desc_cell_values}
    ${sorted}    Evaluate     sorted(${desc_cell_values}, key=int, reverse=True)
    log to console      Reverse sorted: ${sorted}
    lists should be equal       ${sorted}       ${desc_cell_values}
    log to console      Sorting via descending order is working properly

Verify sorting of columns with string values for ASC
    [Documentation]    Verify sorting of columns
    [Arguments]    ${header}       &{header_cell_list}

#   ASC
    scroll element into view        ${header}
    ${header_name}    Get text      ${header}
    log to console      Clicking ${header_name} for ascending sort order
    click element       ${header}
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

Verify sorting of columns with string values for DESC
    [Documentation]    Verify sorting of columns
    [Arguments]    ${header}       &{header_cell_list}

#   DESC
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

Verify sorting of columns with int values for ASC
    [Documentation]    Verify sorting of columns
    [Arguments]    ${header}  &{header_cell_list}

    run keyword and ignore error    wait until element is visible       ${header}
    scroll element into view        ${header}
    ${header_name}    Get text      ${header}
    log to console      Clicking ${header_name} for ascending sort order
    click element       ${header}
    run keyword and ignore error    wait until element is visible    ${ascending_arrow}
    log to console    Ascending arrow is present
    @{asc_cell_values}    create list
    FOR    ${key}    ${value}    IN    &{header_cell_list}
        ${cell_text}    Get text        ${value}
        append to list      ${asc_cell_values}    ${cell_text}
    END
    log to console      This header has: @{asc_cell_values}
    @{sorted}    Evaluate     sorted(${asc_cell_values}, key=int, reverse=False)
    log to console      Sorted has: @{sorted}
    lists should be equal       ${sorted}       ${asc_cell_values}
    log to console      Sorting via ascending order is working properly

Verify sorting of columns with int values for DESC
    [Documentation]    Verify sorting of columns
    [Arguments]    ${header}       &{header_cell_list}

#   DESC
    scroll element into view        ${header}
    ${header_name}    Get text      ${header}
    log to console      Clicking ${header_name} for descending sort order
    click element       ${header}
    run keyword and ignore error    wait until element is visible    ${descending_arrow}
    log to console    Descending arrow is present
    @{desc_cell_values}    create list
    FOR    ${key}    ${value}    IN    &{header_cell_list}
        ${cell_text}    Get text        ${value}
        append to list      ${desc_cell_values}    ${cell_text}
    END
    log to console     This header has: @{desc_cell_values}
    ${sorted}    Evaluate     sorted(${desc_cell_values}, key=int, reverse=True)
    log to console      Reverse sorted: ${sorted}
    lists should be equal       ${sorted}       ${desc_cell_values}
    log to console      Sorting via descending order is working properly


Verify correct checkbox status for test restaurant
    [Arguments]         ${expected_dictionary}      ${actual_dictionary}

    FOR    ${key_status}    ${value_status}    IN    ${expected_dictionary}
        FOR    ${key_list}    ${value_list}    IN    ${actual_dictionary}
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

Await
        [Arguments]     ${duration}
        sleep    ${duration}
        log to console    finished waiting for ${duration}