
from autocore.bases import APILibraryBase
from robot.api.deco import library
from libraries.api.TeamAssignmentApiLibrary.keywords.addagent import AddAgent
from libraries.api.TeamAssignmentApiLibrary.keywords.removeagent import RemoveAgent

# import requests
# from RequestsLibrary.SessionKeywords import SessionKeywords
# from robotlibcore import DynamicCore


@library(scope='GLOBAL')
class TeamAssignmentApiLibrary(APILibraryBase):
    
    def __init__(self):
        super().__init__()
        
        components = [
            AddAgent(library=self),
            RemoveAgent(library=self) 

        ]
        
        self.add_library_components(library_components=components)

