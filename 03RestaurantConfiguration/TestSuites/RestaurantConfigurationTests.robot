*** Settings ***
Library             SeleniumLibrary
Resource            ../../Shared/Keywords/TestBase.robot
Resource            ../../Shared/Keywords/LoginPage.robot
Resource            ../../Shared/Keywords/Navigation.robot
Resource            ../../Shared/Keywords/Commands.robot
Resource            ../Resources/Keywords/UiPages/RestaurantConfigurationKeywords.robot

Test Setup          Start TestCase
Test Teardown       Finish TestCase

Force Tags        regression


*** Test Cases ***

RestaurantConfig00010 - Verify webelements are displayed in Restaurant Configuration page
    [Documentation]    This is to ensure that the web elements in Restaurant Configuration editor are displayed properly
    [Tags]    restaurant-configuration      smoke       rest-config-web
    LoginPage.Login with default auth data
    Commands.Go to Restaurant Configuration editor
    RestaurantConfigurationKeywords.Verify webelements are visible in Restaurant Configuration

RestaurantConfig00020 - Verify sorting of columns are working in Restaurant Configuration page
    [Documentation]    This is to ensure that sorting of columns are working in Restaurant Configuration page
    [Tags]    restaurant-configuration      smoke       rest-config-sorting
    LoginPage.Login with default auth data
    Commands.Go to Restaurant Configuration editor
    RestaurantConfigurationKeywords.Verify sorting of columns in Restaurant Configuration

RestaurantConfig00030 - Verify saving feature in Restaurant Configuration page
    [Documentation]    This is to ensure that sorting of columns are working in Restaurant Configuration page
    [Tags]    restaurant-configuration      smoke       rest-config-saving
    LoginPage.Login with default auth data
    Commands.Go to Restaurant Configuration editor
    RestaurantConfigurationKeywords.Verify restaurant's data
    RestaurantConfigurationKeywords.Verify saving feature







