from robot.api.deco import library
from libraries.userconfig.UserMetaCommon import UserMetaCommon
from libraries.userconfig.UserMetaCommon.config import USER_CONFIG_LANDING_TIMEOUT
from libraries.userconfig.UserTeamsLibrary.keywords.userteams import UserTeamsKeywords
# from libraries.userconfig.UserTeamsLibrary.keywords.browser import Browser
from libraries.userconfig.UserTeamsLibrary.keywords.createteam import CreateTeam
from libraries.userconfig.UserTeamsLibrary.keywords.editteam import EditTeam
from libraries.userconfig.UserTeamsLibrary.keywords.login_logout_page import LoginPage
from libraries.userconfig.UserTeamsLibrary.keywords.login_logout_page import LogoutPage
from libraries.userconfig.UserTeamsLibrary.keywords.openpage import OpenPage
from libraries.userconfig.UserTeamsLibrary.keywords.selectuserteam import SelectUserTeam
from libraries.userconfig.UserTeamsLibrary.keywords.userteamdetails import UserTeamDetails
from libraries.userconfig.UserTeamsLibrary.keywords.userteamseditor import UserTeamsEditor


@library(scope='GLOBAL')
class UserTeamsLibrary(UserMetaCommon):

    def __init__(self):
        UserMetaCommon.__init__(self)
        library_components = [
            UserTeamsKeywords(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
            # Browser(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
            CreateTeam(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
            EditTeam(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
            LoginPage(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
            LogoutPage(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
            OpenPage(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
            SelectUserTeam(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
            UserTeamDetails(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
            UserTeamsEditor(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT)
            
        ]
        self.add_library_components(library_components=library_components)
        
