*** Settings ***
Library     SeleniumLibrary
Library     DatabaseLibrary
Library     Collections
Resource    ../../../../Shared/Keywords/LoginPage.robot
Resource    ../../../../Shared/Keywords/Commands.robot
Resource    ../../Data/TestData.robot

*** Variables ***
#Scalar - Declare scalar variables here
${alert_list_expected_count}            ${4}
${alert_list_element}                   //div[@class='alert alert-info alert-dismissible']
${select_all}                           //div[@class='dropdown-menu show']//button[@type='button'][normalize-space()='Select All']
${one_searched_agent}                       //div[@aria-expanded='true']//a[@role='option']
#List - Declare list variables here
&{test_restaurants}
...                                     *HOUSE OF CHINA*=7f03b0f8-fef8-11e8-8435-0af3d8aa5476
...                                     ASIAN BOWL=209ce5ef-e9d3-11e4-b5e5-80ee733c5b56
...                                     SKT DEMO RESTAURANT=3f00ecca-6645-4cce-95e7-33b697abbeba
#Dictionaries - Declare dictionary variables here
&{agent_ranking_webelements}
...                                     Restaurant List=//button[@data-id='restList']
...                                     User Location=//button[@data-id='userLocation']
...                                     User Position=//button[@data-id='userPosition']
...                                     Agent List=//button[@data-id='agentList']
...                                     Go=//button[@id='go']
...                                     Populate User Restaurant=//button[@id='populateRestaurant']
...                                     Generate Report=//button[@id='generate']
...                                     Save=//button[@id='save']

#${restaurant_header}                    xpath:(//div[@class='relative'])[99]
${restaurant_header}                    xpath://div[@class='ht_clone_top_left_corner handsontable']//th[1]//following::div[1]
&{restaurant_cell_list}                 one=(//th)[12]/following-sibling::td[1]
...                                     two=(//th)[13]/following-sibling::td[1]
...                                     three=(//th)[14]/following-sibling::td[1]

${username_header}                      xpath://div[@class='ht_clone_top_left_corner handsontable']//th[2]//following::div[1]
&{username_cell_list}                   one=(//th)[12]/following-sibling::td[2]
...                                     two=(//th)[13]/following-sibling::td[2]
...                                     three=(//th)[14]/following-sibling::td[2]

${fullname_header}                      xpath:(//div[@class='relative'])[51]
&{fullname_cell_list}                   one=(//th)[12]/following-sibling::td[3]
...                                     two=(//th)[13]/following-sibling::td[3]
...                                     three=(//th)[14]/following-sibling::td[3]

${position_header}                      xpath:(//div[@class='relative'])[52]
&{position_cell_list}                   one=(//th)[12]/following-sibling::td[4]
...                                     two=(//th)[13]/following-sibling::td[4]
...                                     three=(//th)[14]/following-sibling::td[4]

${call_skills_header}                   xpath:(//div[@class='relative'])[53]
&{callskills_cell_list}                 one=(//th)[12]/following-sibling::td[5]
...                                     two=(//th)[13]/following-sibling::td[5]
...                                     three=(//th)[14]/following-sibling::td[5]

${difficult_skills_header}              xpath:(//div[@class='relative'])[54]
&{difficult_cell_list}                  one=(//th)[12]/following-sibling::td[6]
...                                     two=(//th)[13]/following-sibling::td[6]
...                                     three=(//th)[14]/following-sibling::td[6]

${agent_rank_header}                    xpath:(//div[@class='relative'])[55]
&{agent_rank_cell_list}                 one=(//th)[12]/following-sibling::td[7]
...                                     two=(//th)[13]/following-sibling::td[7]
...                                     three=(//th)[14]/following-sibling::td[7]

${client_rank_header}                   xpath:(//div[@class='relative'])[56]
&{client_cell_list}                     one=(//th)[12]/following-sibling::td[8]
...                                     two=(//th)[13]/following-sibling::td[8]
...                                     three=(//th)[14]/following-sibling::td[8]

${uid_header}                           xpath:(//div[@class='relative'])[57]
&{uid_cell_list}                        one=(//th)[12]/following-sibling::td[9]
...                                     two=(//th)[13]/following-sibling::td[9]
...                                     three=(//th)[14]/following-sibling::td[9]

${rid_header}                           xpath:(//div[@class='relative'])[58]
&{rid_cell_list}                        one=(//th)[12]/following-sibling::td[10]
...                                     two=(//th)[13]/following-sibling::td[10]
...                                     three=(//th)[14]/following-sibling::td[10]

&{test_restaurant_cells}
...                                     restaurant_name=(//th)[12]/following-sibling::td[1]
...                                     username=(//th)[12]/following-sibling::td[2]
...                                     full_name=(//th)[12]/following-sibling::td[3]
...                                     position=(//th)[12]/following-sibling::td[4]
...                                     call_skills=(//th)[12]/following-sibling::td[5]
...                                     difficult_skills=(//th)[12]/following-sibling::td[6]
...                                     agent_rank=(//th)[12]/following-sibling::td[7]
...                                     client_rank=(//th)[12]/following-sibling::td[8]
...                                     uid=(//th)[12]/following-sibling::td[9]
...                                     rid=(//th)[12]/following-sibling::td[10]

${select_all}                           //div[@class='dropdown-menu show']//button[@type='button'][normalize-space()='Select All']
${search_restaurant}                    div[class='dropdown-menu show'] input[aria-label='Search']
${restaurant_list}                      //select[@id='restList']
${search_agent}                         //div[@class='dropdown-menu show']//input[@aria-label='Search']
${search_agent_result}                  //div[@aria-expanded='true']//a[@role='option']
*** Keywords ***
Verify sorting for Restaurant in Agent Ranking page
    Commands.Verify sorting of columns with string values       ${restaurant_header}            &{restaurant_cell_list}
    Commands.Verify sorting of columns with string values       ${username_header}              &{username_cell_list}

Verify ASC and DESC sorting for Restaurant
    Commands.Verify sorting of columns with string values for ASC       ${restaurant_header}            &{restaurant_cell_list}
    reload page
    Display test restaurant
    Commands.Verify sorting of columns with string values for DESC      ${restaurant_header}            &{restaurant_cell_list}
    reload page
    Display test restaurant
    Commands.Verify sorting of columns with string values for ASC       ${username_header}              &{username_cell_list}
    reload page
    Display test restaurant
    Commands.Verify sorting of columns with string values for DESC      ${username_header}              &{username_cell_list}
    reload page
    Display test restaurant
    Commands.Verify sorting of columns with string values for ASC    ${position_header}              &{position_cell_list}
    reload page
    Display test restaurant
    Commands.Verify sorting of columns with string values for DESC      ${position_header}              &{position_cell_list}
    reload page
    Display test restaurant
##   Robot framework limitation
#    Commands.Verify sorting of columns with string values for ASC       ${fullname_header}              &{fullname_cell_list}
#    reload page
#    Display test restaurant
#    Commands.Verify sorting of columns with string values for DESC      ${fullname_header}              &{fullname_cell_list}
#    reload page
#    Display test restaurant

Display test restaurant
    select from list by value       ${restaurant_list}      ${test_restaurants}[ASIAN BOWL]
    click element       ${agent_ranking_webelements}[User Position]
    click element       ${select_all}
    click element       ${agent_ranking_webelements}[Agent List]
    click element       ${select_all}
    commands.await      ${duration}[ONE]
    click element       ${agent_ranking_webelements}[Go]

Display test agent
    select from list by value       ${restaurant_list}      ${test_restaurants}[ASIAN BOWL]
    click element       ${agent_ranking_webelements}[User Position]
    click element       ${select_all}
    click element       ${agent_ranking_webelements}[Agent List]
    input text          ${search_agent}     ${agent_alpha}[auth][username]
    click element       ${search_agent_result}
    commands.await      ${duration}[TWO]
    click element       ${agent_ranking_webelements}[Go]

Verify webelements are visible in Agent Ranking Configuration
    [Documentation]    Verify webelements are visible in Restaurant Configuration

    Commands.Verify elements visibility with dictionary    &{agent_ranking_webelements}
    Commands.Verify equal element count     ${alert_list_element}       ${alert_list_expected_count}

Verify restaurants data for test restaurant
    wait until element contains        ${test_restaurant_cells}[restaurant_name]       ${data}[restaurant_alpha][restaurant_name]
    Commands.Verify data of cells via dictionary      &{test_restaurant_cells}
    ${test_restaurant_data}     create list
    FOR    ${key}       ${value}        IN        &{data}[restaurant_alpha]
    append to list    ${test_restaurant_data}     ${value}
    END
    log to console      Expected data list: ${test_restaurant_data}
    lists should be equal           ${test_restaurant_data}     ${stored_data}


