from libraries.dashboard.DashboardCommon.keywords.browser import BrowserKeywords
from libraries.dashboard.DashboardCommon.keywords.landing import LandingKeywords
from libraries.dashboard.DashboardCommon.keywords.login import LoginKeywords
from robot.api.deco import library
from libraries.dashboard.config import DASHBOARD_GLOBAL_TIMEOUT

from autocore.bases import WebLibraryBase



@library(scope='GLOBAL')
class DashboardCommon(WebLibraryBase):

    def __init__(self):
        WebLibraryBase.__init__(self)

        components = [
            BrowserKeywords(library=self),
            LoginKeywords(library=self, timeout=DASHBOARD_GLOBAL_TIMEOUT),
            LandingKeywords(library=self, timeout=DASHBOARD_GLOBAL_TIMEOUT)
        ]
    
        self.add_library_components(library_components=components)