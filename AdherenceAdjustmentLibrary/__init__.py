from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import library
from robotlibcore import DynamicCore

from AdherenceAdjustmentLibrary.keywords.browser import Browser
from AdherenceAdjustmentLibrary.keywords.loginpage import LoginPage
from AdherenceAdjustmentLibrary.keywords.openpage import OpenPage
from AdherenceAdjustmentLibrary.keywords.adhadjpage import AdherenceAdjustmentPage
from AdherenceAdjustmentLibrary.keywords.teamdetails import TeamDetails



@library(scope='GLOBAL')
class AdherenceAdjustmentLibrary(DynamicCore):
    
    def __init__(self): 
        ctx = SeleniumLibrary(timeout="30s", screenshot_root_directory="EMBED")
        components = [
            Browser(ctx=ctx),
            LoginPage(ctx=ctx),
            OpenPage(ctx=ctx),
            AdherenceAdjustmentPage(ctx=ctx), 
            TeamDetails(ctx=ctx)

        ]
        DynamicCore.__init__(self,library_components=components)