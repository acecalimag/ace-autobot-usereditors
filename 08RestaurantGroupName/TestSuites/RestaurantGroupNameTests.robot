*** Settings ***
Library             SeleniumLibrary
Resource            ../../Shared/Keywords/TestBase.robot
Resource            ../../Shared/Keywords/LoginPage.robot
Resource            ../../Shared/Keywords/Navigation.robot
Resource            ../../Shared/Keywords/Commands.robot
Resource            ../Resources/Keywords/UiPages/RestaurantGroupNamePage.robot

Test Setup          Start TestCase
Test Teardown       Finish TestCase

*** Test Cases ***

RestaurantGroupName00010 - Verify webelements are displayed in Training Groups page
    [Documentation]    This is to ensure that the web elements in aux configuration editor are displayed properly
    [Tags]    smoke    restaurant-group-name
    LoginPage.Login with default auth data
    Commands.Go to Restaurant Group Name
    RestaurantGroupNamePage.Verify Web Elements are displayed on Restaurant Group Name page


RestaurantGroupName00020 - Verify data is displayed
    [Documentation]    This is to ensure that the details of default user agent are correct
    [Tags]    smoke
    LoginPage.Login with default auth data


TrainingGroups00030 - Verify saving feature in Training Groups page
    [Documentation]    This is to ensure that the saving is working properly in this page
    [Tags]    smoke
    LoginPage.Login with default auth data
