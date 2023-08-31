from robot.api.deco import library
from libraries.userconfig.UserTeamsLibrary.keywords.userteams import UserTeamsKeywords
from libraries.userconfig.UserMetaCommon import UserMetaCommon
from libraries.userconfig.UserMetaCommon.config import USER_CONFIG_LANDING_TIMEOUT


@library(scope='GLOBAL')
class UserTeamsLibrary(UserMetaCommon):

    def __init__(self):
        UserMetaCommon.__init__(self)
        library_components = [
            UserTeamsKeywords(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
        ]
        self.add_library_components(library_components=library_components)
        
