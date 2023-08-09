*** Settings ***
Library             SeleniumLibrary
Resource            ../../Shared/Keywords/TestBase.robot
Resource            ../../Shared/Keywords/LoginPage.robot
Resource            ../../Shared/Keywords/Navigation.robot
Resource            ../../Shared/Keywords/Commands.robot
Resource            ../Resources/Keywords/UiPages/AuxConfigurationKeywords.robot

Test Setup          Start TestCase
Test Teardown       Finish TestCase

Force Tags          regression

*** Test Cases ***

AuxConfig00010 - Verify webelements are displayed in Aux Configuration page
    [Documentation]    This is to ensure that the web elements in aux configuration editor are displayed properly
    [Tags]    aux-configuration     smoke       webelements-aux

    LoginPage.Login with default auth data
    Commands.Go to Aux Configuration editor
    AuxConfigurationKeywords.Verify webelements are visible

AuxConfig00020 - Verify sorting of columns are working in Aux Configuration page
    [Documentation]    This is to ensure that the details of default user agent are correct
    [Tags]    aux-configuration     smoke       sorting-aux

    LoginPage.Login with default auth data
    Commands.Go to Aux Configuration editor
    AuxConfigurationKeywords.Verify Sorting of Aux Configuration Columns

AuxConfig00030 - Verify saving feature in Aux Configuration page
    [Documentation]    This is to ensure that the saving is working properly in this page
    [Tags]    aux-configuration     smoke       saving-aux

    LoginPage.Login with default auth data
    Commands.Go to Aux Configuration editor
    AuxConfigurationKeywords.Verify agent's data
    AuxConfigurationKeywords.Verify saving checkbox modification
    AuxConfigurationKeywords.Verify correct checkbox status for agent