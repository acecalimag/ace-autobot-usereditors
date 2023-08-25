from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import library
from robotlibcore import DynamicCore
from UserTeamsLibrary.keywords.browser import Browser
from UserTeamsLibrary.keywords.login_logout_page import LoginPage
from UserTeamsLibrary.keywords.login_logout_page import LogoutPage
from UserTeamsLibrary.keywords.openpage import OpenPage
from UserTeamsLibrary.keywords.selectuserteam import SelectUserTeam
from UserTeamsLibrary.keywords.userteamdetails import UserTeamDetails
from UserTeamsLibrary.keywords.userteamseditor import UserTeamsEditor
from UserTeamsLibrary.keywords.createteam import CreateTeam
from UserTeamsLibrary.keywords.editteam import EditTeam


@library(scope='GLOBAL')
class UserTeamsLibrary(DynamicCore):
    
    def __init__(self): 
        ctx = SeleniumLibrary(timeout="30s", screenshot_root_directory="EMBED")
        components = [
            Browser(ctx=ctx),
            LoginPage(ctx=ctx),
            OpenPage(ctx=ctx),
            SelectUserTeam(ctx=ctx), 
            UserTeamDetails(ctx=ctx), 
            UserTeamsEditor(ctx=ctx),
            CreateTeam(ctx=ctx),
            EditTeam(ctx=ctx), 
            LogoutPage(ctx=ctx)
        ]
        DynamicCore.__init__(self,library_components=components)