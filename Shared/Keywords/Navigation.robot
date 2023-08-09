*** Settings ***
Library     SeleniumLibrary
Resource    Commands.robot

*** Variables ***


${configurations menu button}       //a[@id='ConfigNavbarDropdown']
${page title text}                  css:body > nav > a[class='navbar-brand']
${iframe}                           xpath:(//iframe)[1]
${spinner_loading}          //i[@class='fa fa-spinner fa-pulse fa-spin fa-5x']

*** Keywords ***

Select User Configuration editor
    [Documentation]    Selects the configuration page from the dropdown.
    ...    This assumes that you're already logged in
    ...    and can access the configurations menu button.
    [Arguments]    ${editor name}
    commands.run keyword until succeeds        wait until element is visible    ${configurations menu button}
    click element    ${configurations menu button}
    click element    //*[text()[contains(.,"${editor name}")]]
    run keyword and ignore error    wait until element contains    ${page title text}    ${editor name}
    log to console    User is now on ${editor name}
    log    User is now on ${editor name}
