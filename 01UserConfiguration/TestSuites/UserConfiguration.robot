*** Settings ***
Library             SeleniumLibrary
Resource            ../../Shared/Keywords/TestBase.robot
Resource            ../../Shared/Keywords/LoginPage.robot
Resource            ../Resources/Keywords/UiPages/UserConfigurationPage.robot
Resource            ../../Shared/Keywords/Commands.robot

Test Setup          Start TestCase
Test Teardown       Finish TestCase

Force Tags          regression

*** Test Cases ***
UserConfig00010 - Verify webelements are displayed in User Configuration page
    [Documentation]    This is to ensure that the web elements in user configuration editor are displayed properly
    [Tags]      user-configuration        smoke       user-webelements

    LoginPage.Login with default auth data
    UserConfigurationPage.Verify webelements are visible in User Configuration page

UserConfig00020 - Verify sorting of columns are working in User Configuration page
    [Documentation]    This is to ensure that the details of default user agent are correct
    [Tags]      user-configuration        smoke       userconfig-sorting

    LoginPage.Login with default auth data
    UserConfigurationPage.Verify sorting of columns in User Configuration page

UserConfig00030 - Verify user is able to assign a location
    [Documentation]    This is to ensure that the user can successfully assign a location to a user with database validation
    [Tags]      user-configuration        smoke       user-saving

    LoginPage.Login with default user
    UserConfigurationPage.Filter-out default user in aux configuration
    UserConfigurationPage.Assign location to a specific agent
    UserConfigurationPage.Verify kjt locations via query
    UserConfigurationPage.Verify agent is assigned to a location via query
