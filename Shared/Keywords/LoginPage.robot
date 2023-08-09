*** Settings ***
Library     SeleniumLibrary
Resource    ../../02AuxConfiguration/Resources/Data/TestData.robot
Resource    Commands.robot
*** Variables ***
${login_form}               //form[@id='loginform']
${username_textfield}       //input[@id='username']
${password_textfield}       //input[@id='password']
${login_button}             //button[@id='login']
${configurations menu button}       //a[@id='ConfigNavbarDropdown']

${default_username}         wmaximoff
${default_username_aux}     b110
${default password}         kjt
${default team}             ENGINEERING


*** Keywords ***
Login with auth data
    [Documentation]    Sign in using the username and password from the test data
    Login as    ${data}[auth][username]    ${data}[auth][password]

Login with default user
    [Documentation]    Sign in using the default username and password
    Login as    ${default_username}    ${default_password}

Login with default aux user
    [Documentation]    Sign in using the default username and password
    Login as    ${agent_alpha}[auth][username]      ${agent_alpha}[auth][password]

Login with default auth data
    [Documentation]    Sign in using the default username and password via test data
    Login as    ${agent_alpha}[auth][username]      ${agent_alpha}[auth][password]

Login as
    [Documentation]    Sign in using the provided username and password
    [Arguments]    ${username}    ${password}

    commands.run keyword until succeeds        wait until element is visible    ${login_form}
    input text    ${username_textfield}    ${username}
    input password    ${password_textfield}    ${password}
    commands.await      ${duration}[TWO]
    commands.run keyword until succeeds        click button    ${login_button}