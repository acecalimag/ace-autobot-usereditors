

from robot.api.deco import library
from libraries.userconfig.UserMetaCommon import UserMetaCommon
from libraries.userconfig.UserMetaCommon.config import USER_CONFIG_LANDING_TIMEOUT
# from libraries.userconfig.TeamAssignmentLibrary.keywords.browser import Browser
from libraries.userconfig.TeamAssignmentLibrary.keywords.login_logout_page import LoginPage
from libraries.userconfig.TeamAssignmentLibrary.keywords.login_logout_page import LogoutPage
from libraries.userconfig.TeamAssignmentLibrary.keywords.openpage import OpenPage
from libraries.userconfig.TeamAssignmentLibrary.keywords.selectteam import SelectTeam
from libraries.userconfig.TeamAssignmentLibrary.keywords.teamdetails import TeamDetails
from libraries.userconfig.TeamAssignmentLibrary.keywords.teamassignmenteditor import TeamAssignmentEditor
from libraries.userconfig.TeamAssignmentLibrary.keywords.assignagenttoteam import AssignAgenttoTeam
from libraries.userconfig.TeamAssignmentLibrary.keywords.removeagenttoteam import RemoveAgenttoTeam


# from robotlibcore import DynamicCore
# from SeleniumLibrary import SeleniumLibrary


@library(scope='GLOBAL')
class TeamAssignmentLibrary(UserMetaCommon):
    
    def __init__(self): 
        UserMetaCommon.__init__(self)
        library_components = [
            # Browser(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
            LoginPage(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
            OpenPage(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
            SelectTeam(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT), 
            TeamDetails(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT), 
            TeamAssignmentEditor(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
            AssignAgenttoTeam(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
            RemoveAgenttoTeam(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT),
            LogoutPage(library=self, timeout=USER_CONFIG_LANDING_TIMEOUT)
        ]
        self.add_library_components(library_components=library_components)


