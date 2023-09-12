from robot.api.deco import keyword
from libraries.contentconfig.ContentConfigCommon.locators import loginpage
from autocore.bases import WebLibraryComponent

class LoginKeywords(WebLibraryComponent):
    
    @keyword(tags=("LoginKeywords","ContentConfigCommonKeywords"))
    def login_to_content_config(self, username: str = None, password: str = None):
        self.web.wait_until_visible(locator=loginpage.LOGIN_BTN)
        if username is not None:
            self.web.input_text(locator=loginpage.USERNAME, text=username)
            
        if password is not None:
            self.web.input_text(locator=loginpage.PASSWORD, text=password)
        
        self.web.click(locator=loginpage.LOGIN_BTN)