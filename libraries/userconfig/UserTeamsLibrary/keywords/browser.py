
from autocore.bases import WebLibraryComponent
from robot.api.deco import keyword
from libraries.userconfig.UserMetaCommon.config import USER_CONFIG_LOGIN_PAGE_URL

# from SeleniumLibrary import SeleniumLibrary


def _get_url(env: str):
    env = env.lower().strip()
    url = USER_CONFIG_LOGIN_PAGE_URL.get(env)
    if url is None:
        raise Exception(f'No URL configured for [ {env} ] environment yet.')
    return url



class Browser(WebLibraryComponent):
    
    # def __init__(self, ctx: SeleniumLibrary):
    #     self.__ctx = ctx
        
    @keyword(tags=("BrowserKeywords","UserTeamsCommonKeywords")) 
    def open_config_in_browser1(self):
        """Open User config login page in browser."""
        self.web.open_browser(url="https://qa.letsdochinese.com/KJTCore/resources/userconfigclient/userteameditor.html",
                                browser="chrome")
        self.web.se_lib.maximize_browser_window()


