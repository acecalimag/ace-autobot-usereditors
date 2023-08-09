*** Settings ***
Library             SeleniumLibrary
Resource            ../../Shared/Keywords/TestBase.robot
Resource            ../../Shared/Keywords/LoginPage.robot
Resource            ../../Shared/Keywords/Navigation.robot
Resource            ../../Shared/Keywords/Commands.robot
Resource            ../Resources/Keywords/UiPages/AutoAssignKeywords.robot

Test Setup          Start TestCase
Test Teardown       Finish TestCase

Force Tags        regression


*** Test Cases ***
AutoAssign00010 - Verify webelements are displayed in Auto Assign Configuration page
    [Documentation]    This is to ensure that the web elements in Agent Ranking page are displayed properly
    [Tags]    auto-assign-configuration      smoke    auto-web
    LoginPage.Login with default auth data
    Commands.Go to Auto Assign editor
    AutoAssignKeywords.Verify webelements are visible in Auto Assign Configuration

AutoAssign00020 - Verify sorting of columns are working in Auto Assign Configuration page
    [Documentation]    This is to ensure that sorting of columns are working in Agent Ranking page
    [Tags]    auto-assign-configuration      smoke    auto-sorting
    LoginPage.Login with default auth data
    Commands.Go to Auto Assign editor
    AutoAssignKeywords.Display three test restaurants
    AutoAssignKeywords.Verify sorting is working in Auto Assign Configuration page

AutoAssign00030 - Verify saving feature in Auto Assign Configuration page
    [Documentation]    This is to ensure that saving feature in Agent Ranking editor are working as expected
    [Tags]    auto-assign-configuration       smoke    auto-data
    LoginPage.Login with default auth data
    Commands.Go to Auto Assign editor
    AutoAssignKeywords.Display test restaurant
    AutoAssignKeywords.Verify restaurants data for test restaurant










