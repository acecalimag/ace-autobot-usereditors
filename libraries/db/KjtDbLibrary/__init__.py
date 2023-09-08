from autocore.bases import DBLibraryBase
from libraries.db.KjtDbLibrary.keywords.user import Users
from libraries.db.KjtDbLibrary.keywords.restaurant import Restaurant
from libraries.db.KjtDbLibrary.keywords.kjtorder import KjtOrder
from libraries.db.KjtDbLibrary.keywords.printer import Printer
from libraries.db.KjtDbLibrary.keywords.printtask import PrintTask
from libraries.db.KjtDbLibrary.keywords.agent import Agent
from libraries.db.KjtDbLibrary.keywords.userteams import UserTeams
from robot.api.deco import library


@library(scope='GLOBAL')
class KjtDbLibrary(DBLibraryBase):
    
    def __init__(self):
        super().__init__(db="kjt")
        components = [
            Users(library=self),
            Restaurant(library=self),
            KjtOrder(library=self),
            Printer(library=self),
            PrintTask(library=self),
            Agent(library=self),
            UserTeams(library=self)
        ]
        self.add_library_components(library_components=components)


        