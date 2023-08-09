from robotlibcore import DynamicCore
from robot.api.deco import library, keyword
import requests
from RequestsLibrary.SessionKeywords import SessionKeywords
from robotlibcore import DynamicCore

from TeamAssignmentLibrary.APILibrary.AddAgentTA import AddAgentTA
from TeamAssignmentLibrary.APILibrary.RemoveAgentTA import RemoveAgentTA


@library
class APILibrary(DynamicCore):
    
    def __init__(self):
        
        components = [
            AddAgentTA(),
            RemoveAgentTA() 

        ]
        
        DynamicCore.__init__(self, library_components=components)