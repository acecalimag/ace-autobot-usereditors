from robot.api.deco import library
from libraries.userconfig.UserConfigLibrary.keywords.landingpage import LandingPageKeywords
from libraries.userconfig.UserConfigLibrary.keywords.userconfig import UserConfigKeywords
from libraries.userconfig.UserMetaCommon import UserMetaCommon
from libraries.userconfig.UserMetaCommon.config import USER_CONFIG_LANDING_TIMEOUT


@library(scope='GLOBAL')
class UserConfigLibrary(UserMetaCommon):

    def __init__(self):
        UserMetaCommon.__init__(self)
        library_components = [
            LandingPageKeywords(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
            UserConfigKeywords(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
        ]
        self.add_library_components(library_components=library_components)
        
