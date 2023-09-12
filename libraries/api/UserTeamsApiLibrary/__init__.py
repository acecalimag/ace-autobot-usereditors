
from autocore.bases import APILibraryBase
from robot.api.deco import library
from libraries.api.UserTeamsApiLibrary.keywords.createuserteam import CreateUserTeam
from libraries.api.UserTeamsApiLibrary.keywords.modifyuserteam import ModifyUserTeam

# from robotlibcore import DynamicCore
# from RequestsLibrary.SessionKeywords import SessionKeywords
# import requests



@library(scope='GLOBAL')
class UserTeamsApiLibrary(APILibraryBase):
    
    def __init__(self):
        super().__init__()
        
        components = [
            CreateUserTeam(library=self),
            ModifyUserTeam(library=self) 

        ]
        
        self.add_library_components(library_components=components)