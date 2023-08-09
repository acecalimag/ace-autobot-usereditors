*** Settings ***
Library     SeleniumLibrary
Resource    ../Config/DefaultConfigs.robot


*** Keywords ***
Start TestCase
    ${chrome_options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver

    Call Method    ${chrome_options}    add_argument    --test-type
    Call Method    ${chrome_options}    add_argument    --disable-extensions
    Call Method    ${chrome_options}    add_argument    --disable-gpu
    Call Method    ${chrome_options}    add_argument    --no-sandbox
    Call Method    ${chrome_options}    add_argument    --incognito
    Call Method    ${chrome_options}    add_argument    --ignore-certificate-errors
    Call Method    ${chrome_options}    add_argument    --disable-popup-blocking
    Call Method    ${chrome_options}    add_argument    --disable-default-apps
    Call Method    ${chrome_options}    add_argument    --disable-extensions-file-access-check
    Call Method    ${chrome_options}    add_argument    --disable-infobars

#    Load test data
    set selenium speed              .7 seconds
    set selenium implicit wait      30 seconds
    set selenium timeout            30 seconds

    open browser
#    set browser implicit wait    20 seconds
    ...     https://qa.letsdochinese.com/KJTCore/resources/userconfigclient/usermetaeditor.html
#    ...     https://qa.letsdochinese.com/KJTCore/resources/index.html?agent=agentmetrics
    ...     ${browser}
    ...     options=${chrome_options}
    delete all cookies
    set window size    1920    1080
    ${width}    ${height}    get window size
    log to console    ${width}
    log to console    ${height}
    maximize browser window

Finish TestCase
    close browser

#Load test data
 #    [Documentation]    Convert ``test data string`` to JSON and make it global
    #    set global variable    ${data}    ${DataDriver_TEST_DATA}[arguments][\${test_data}]
