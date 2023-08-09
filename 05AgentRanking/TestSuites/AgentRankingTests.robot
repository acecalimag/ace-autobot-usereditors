*** Settings ***
Library             SeleniumLibrary
Resource            ../../Shared/Keywords/TestBase.robot
Resource            ../../Shared/Keywords/LoginPage.robot
Resource            ../../Shared/Keywords/Navigation.robot
Resource            ../../Shared/Keywords/Commands.robot
Resource            ../Resources/Keywords/UiPages/AgentRankingKeywords.robot

Test Setup          Start TestCase
Test Teardown       Finish TestCase

Force Tags        regression


*** Test Cases ***
AgentRanking00010 - Verify webelements are displayed in Agent Ranking page
    [Documentation]    This is to ensure that the web elements in Agent Ranking page are displayed properly
    [Tags]    agent-ranking      smoke      agent-web
    LoginPage.Login with default auth data
    Commands.Go to Agent Ranking editor
    AgentRankingKeywords.Display test restaurant
    AgentRankingKeywords.Verify webelements are visible in Agent Ranking Configuration

AgentRanking00020 - Verify sorting of columns are working in Agent Ranking page
    [Documentation]    This is to ensure that sorting of columns are working in Agent Ranking page
    [Tags]    agent-ranking      smoke    agent-sort
    LoginPage.Login with default auth data
    Commands.Go to Agent Ranking editor
    AgentRankingKeywords.Display test restaurant
    AgentRankingKeywords.Verify sorting for Restaurant in Agent Ranking page

AgentRanking00030 - Verify saving feature in Agent Ranking page
    [Documentation]    This is to ensure that saving feature in Agent Ranking editor are working as expected
    [Tags]    agent-ranking     smoke    agent-data
    LoginPage.Login with default auth data
    Commands.Go to Agent Ranking editor
    AgentRankingKeywords.Display test agent
    AgentRankingKeywords.Verify restaurants data for test restaurant








