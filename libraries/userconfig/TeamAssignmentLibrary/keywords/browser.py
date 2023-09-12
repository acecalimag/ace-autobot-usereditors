

from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword

class Browser:
    
    def __init__(self, ctx: SeleniumLibrary):
        self.__ctx = ctx
        
    @keyword 
    def open_config_in_browser(self):
        self.__ctx.open_browser(url="https://qa.letsdochinese.com/KJTCore/resources/userconfigclient/teamassignmenteditor.html",
                                browser="chrome")
        self.__ctx.maximize_browser_window()