from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import library
from robotlibcore import DynamicCore

from AdherenceAdjustmentLibrary.keywords.browser import Browser
from AdherenceAdjustmentLibrary.keywords.login_logout_page import LoginPage
from AdherenceAdjustmentLibrary.keywords.login_logout_page import LogoutPage
from AdherenceAdjustmentLibrary.keywords.openpage import OpenPage
from AdherenceAdjustmentLibrary.keywords.adhadjpage import AdherenceAdjustmentPage
from AdherenceAdjustmentLibrary.keywords.selectdispute import SelectDispute
from AdherenceAdjustmentLibrary.keywords.disputedetails import DisputeDetails


@library(scope='GLOBAL')
class AdherenceAdjustmentLibrary(DynamicCore):
    
    def __init__(self): 
        ctx = SeleniumLibrary(timeout="30s", screenshot_root_directory="EMBED")
        components = [
            Browser(ctx=ctx),
            LoginPage(ctx=ctx),
            OpenPage(ctx=ctx),
            AdherenceAdjustmentPage(ctx=ctx), 
            SelectDispute(ctx=ctx),
            DisputeDetails(ctx=ctx),
            LogoutPage(ctx=ctx)
        ]
        DynamicCore.__init__(self,library_components=components)