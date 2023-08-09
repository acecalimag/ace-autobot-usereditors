from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import library
from robotlibcore import DynamicCore

from TeamAssignmentLibrary.keywords.browser import Browser
from TeamAssignmentLibrary.keywords.loginpage import LoginPage
from TeamAssignmentLibrary.keywords.openpage import OpenPage
from TeamAssignmentLibrary.keywords.selectteam import SelectTeam
from TeamAssignmentLibrary.keywords.teamdetails import TeamDetails
from TeamAssignmentLibrary.keywords.teamassignmenteditor import TeamAssignmentEditor
from TeamAssignmentLibrary.keywords.assignagenttoteam import AssignAgenttoTeam
from TeamAssignmentLibrary.keywords.removeagenttoteam import RemoveAgenttoTeam


@library(scope='GLOBAL')
class TeamAssignmentLibrary(DynamicCore):
    
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