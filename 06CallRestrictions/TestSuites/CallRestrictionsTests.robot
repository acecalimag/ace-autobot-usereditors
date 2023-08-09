*** Settings ***
Library             SeleniumLibrary
Resource            ../../Shared/Keywords/TestBase.robot
Resource            ../../Shared/Keywords/LoginPage.robot
Resource            ../../Shared/Keywords/Navigation.robot
Resource            ../../Shared/Keywords/Commands.robot
Resource            ../Resources/Keywords/UiPages/CallRestrictionsKeyword.robot

Test Setup          Start TestCase
Test Teardown       Finish TestCase

*** Test Cases ***

CallRestrictions00010 - Verify webelements are visibile in Call Restrictions page
    [Tags]    call-restrictions    smoke        call-webelements
    LoginPage.Login with default user
    Commands.Go to Call Restriction editor
    CallRestrictionsKeyword.Verify webelements in Call Restrictions are displayed



CallRestrictions00020 - Verify sorting columns feature is working in Call Restrictions
    [Documentation]    This is to ensure that the details of default user agent are correct
    [Tags]    call-restrictions    smoke        call-sorting
    LoginPage.Login with default auth data
    Commands.Go to Call Restriction editor
    Verify sorting of columns for Call Restrictions page


CallRestrictions00030 - Verify saving feature in Training Groups page
    [Documentation]    This is to ensure that the saving is working properly in this page
    [Tags]        smoke        call-saving
    LoginPage.Login with default auth data
