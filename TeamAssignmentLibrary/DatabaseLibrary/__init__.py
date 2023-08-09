from robotlibcore import DynamicCore
from robot.api.deco import library
from autocore.Database import Database

from TeamAssignmentLibrary.DatabaseLibrary.TeamAssignmentDB import TeamAssignmentDB



@library
# (scope='GLOBAL')
class DatabaseLibrary(DynamicCore):
    
    def __init__(self):
        
        QA_DB_CREDS = {
            "host": "qa-db.letsdochinese.com",
            "user": "qaauto",
            "password": "8bbz9k",
            "port": "3306"
        }
        
        kjt_db = Database(database="kjt", host=QA_DB_CREDS['host'], user=QA_DB_CREDS['user'], password=QA_DB_CREDS['password'],port=QA_DB_CREDS['port'])
                
        components = [
            TeamAssignmentDB(db=kjt_db)

            
            
        ]
        
        DynamicCore.__init__(self, library_components=components)
