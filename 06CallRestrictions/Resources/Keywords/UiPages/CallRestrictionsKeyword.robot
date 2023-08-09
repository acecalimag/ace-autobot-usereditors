*** Settings ***
Library     SeleniumLibrary
Library     DatabaseLibrary
Resource    ../../../../Shared/Keywords/LoginPage.robot
Resource    ../../../../Shared/Keywords/Commands.robot

*** Variables ***
&{call_rest}
...                                 go=//button[@id='go']
...                                 save=//button[@id='save']

${alert_list_element_call_restriction}          //div[@class='col-3']//div
${alert_expected_count_call}                    ${4}

${username_header}                      xpath:(//div[@class='relative'])[102]
&{username_cell_list}                   one=(//th)[17]/following-sibling::td[1]
...                                     two=(//th)[18]/following-sibling::td[1]
...                                     three=(//th)[19]/following-sibling::td[1]

${fullname_header}                      xpath:(//div[@class='relative'])[52]
&{fullname_cell_list}                   one=(//th)[17]/following-sibling::td[2]
...                                     two=(//th)[18]/following-sibling::td[2]
...                                     three=(//th)[19]/following-sibling::td[2]

${position_header}                      xpath:(//div[@class='relative'])[53]
&{position_cell_list}                   one=(//th)[17]/following-sibling::td[3]
...                                     two=(//th)[18]/following-sibling::td[3]
...                                     three=(//th)[19]/following-sibling::td[3]

*** Keywords ***

Verify webelements in Call Restrictions are displayed
    Commands.Verify elements visibility with dictionary     &{call_rest}
    Commands.Verify equal element count     ${alert_list_element_call_restriction}          ${alert_expected_count_call}

Verify sorting of columns for Call Restrictions page
    Commands.Verify sorting of columns with string values       ${username_header}      &{username_cell_list}
    Commands.Verify sorting of columns with string values       ${fullname_header}      &{fullname_cell_list}
    Commands.Verify sorting of columns with string values       ${position_header}      &{position_cell_list}

Verify saving of data in Call restrictions page
