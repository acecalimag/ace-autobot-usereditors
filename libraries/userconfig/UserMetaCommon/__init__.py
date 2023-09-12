
from autocore.bases import WebLibraryBase
from libraries.userconfig.UserMetaCommon.config import USER_CONFIG_GLOBAL_TIMEOUT
from libraries.userconfig.UserMetaCommon.keywords.browser import BrowserKeywords
from libraries.userconfig.UserMetaCommon.keywords.landingpage import LandingPageKeywords
from libraries.userconfig.UserMetaCommon.keywords.loginpage import LoginKeywords



class UserMetaCommon(WebLibraryBase):

    def __init__(self):
        WebLibraryBase.__init__(self)
        library_components = [
            BrowserKeywords(library=self, timeout=USER_CONFIG_GLOBAL_TIMEOUT),
            LoginKeywords(library=self, timeout=USER_CONFIG_GLOBAL_TIMEOUT),
            LandingPageKeywords(library=self, timeout=USER_CONFIG_GLOBAL_TIMEOUT)
        ]
        self.add_library_components(library_components=library_components)
