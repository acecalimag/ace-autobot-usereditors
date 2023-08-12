from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import library
from robotlibcore import DynamicCore

from UserTeamLibrary.keywords.browser import Browser
from UserTeamLibrary.keywords.loginpage import LoginPage
from UserTeamLibrary.keywords.openpage import OpenPage
from UserTeamLibrary.keywords.selectteam import SelectTeam
from UserTeamLibrary.keywords.teamdetails import TeamDetails
from UserTeamLibrary.keywords.teamassignmenteditor import TeamAssignmentEditor
from UserTeamLibrary.keywords.assignagenttoteam import AssignAgenttoTeam
from UserTeamLibrary.keywords.removeagenttoteam import RemoveAgenttoTeam


@library(scope='GLOBAL')
class UserTeamLibrary(DynamicCore):
    
    def __init__(self): 
        ctx = SeleniumLibrary(timeout="30s", screenshot_root_directory="EMBED")
        components = [
            Browser(ctx=ctx),
            LoginPage(ctx=ctx),
            OpenPage(ctx=ctx),
            SelectTeam(ctx=ctx), 
            TeamDetails(ctx=ctx), 
            TeamAssignmentEditor(ctx=ctx),
            AssignAgenttoTeam(ctx=ctx),
            RemoveAgenttoTeam(ctx=ctx)

        ]
        DynamicCore.__init__(self,library_components=components)