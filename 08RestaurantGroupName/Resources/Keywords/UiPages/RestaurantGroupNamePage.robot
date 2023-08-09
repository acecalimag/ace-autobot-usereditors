*** Settings ***
Library     SeleniumLibrary
Library     DatabaseLibrary
Resource    ../../../../Shared/Keywords/LoginPage.robot
Resource    ../../../../Shared/Keywords/Commands.robot

*** Variables ***
&{rest_name}
...                                 restaurant_groups=//h5[normalize-space()='Restaurant Groups']
...                                 name=//th[contains(text(),'Name')]
...                                 description=//th[contains(text(),'Description')]
...                                 type=//th[contains(text(),'Type')]
...                                 status=//th[contains(text(),'Status')]
...                                 lastupdated=//th[contains(text(),'Last Updated')]
...                                 previous1=//li[@id='rest-groups-tbl_previous']
...                                 previous=//a[normalize-space()='Previous']
...                                 next1=//a[normalize-space()='Next']
...                                 next=//li[@id='rest-groups-tbl_next']



*** Keywords ***
Verify Web Elements are displayed on Restaurant Group Name page
    [Documentation]    Verify Web Elements are displayed on Restaurant Group Name page
    Commands.Verify elements visibility with dictionary     &{rest_name}