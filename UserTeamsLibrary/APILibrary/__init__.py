from robotlibcore import DynamicCore
from robot.api.deco import library, keyword
import requests
from RequestsLibrary.SessionKeywords import SessionKeywords
from robotlibcore import DynamicCore

from UserTeamsLibrary.APILibrary.createuserteam import CreateUserTeam
from UserTeamsLibrary.APILibrary.modifyuserteam import ModifyUserTeam


@library
class APILibrary(DynamicCore):
    
    def __init__(self):
        
        components = [
            CreateUserTeam(),
            ModifyUserTeam() 

        ]
        
        DynamicCore.__init__(self, library_components=components)