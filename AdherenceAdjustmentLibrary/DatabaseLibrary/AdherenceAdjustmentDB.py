
from robot.api.deco import keyword
from autocore.Database import Database

class AdherenceAdjustmentDB:

    def __init__(self, db: Database):
        self.__db = db

    @keyword
    def get_user_details(self, username: str):
        """ TODO: Create a database query to retrieve the Agent's UID."""
        query = "SELECT u.username, um.position, ul.code FROM kjt.usermeta AS um JOIN kjt.user AS u ON um.uid = u.uid JOIN kjt.userlocation AS ul ON um.lid = ul.lid WHERE u.username = %s;"
         
        result = self.__db.execute(query, (username,))
        if result and len(result) > 0:
            row = result[0]
            return {
                'username': row['username'].upper(),
                'position': row['position'].upper(),
                'location': row['code'].upper()
            }
        else:
            return None
        
        
        








    @keyword
    def get_user_team_db(self, tname: str):
        """ TODO: Create a database query to retrieve the User Team Details."""
        query = "SELECT ut.name as Team_Name, ut.description as Team_Description, u.name as Team_Lead, ul.code as Team_Location, ut.type as Team_Type, ut.status as Team_Status, ut.updateTime as Last_Updated FROM kjt.userteam AS ut JOIN kjt.user AS u ON ut.teamLead = u.uid JOIN kjt.userlocation AS ul ON ut.location = ul.lid WHERE ut.name = %s;"
        
        result = self.__db.execute(query, (tname,))
        if result and len(result) > 0:
            row = result[0]

            # Convert and format the Team Type
            team_type = row['Team_Type'].lower()
            formatted_team_type = team_type.replace('nonoperational', 'Non-Operational').title()

            return {
                'Team Name': row['Team_Name'],
                'Team Description': row['Team_Description'],
                'Team Lead': row['Team_Lead'],
                'Team Location': row['Team_Location'],
                'Team Type': formatted_team_type,
                'Team Status': row['Team_Status'].capitalize(),
                'Last Updated': row['Last_Updated']
            }
        else:
            return None
        


 



# QA_DB_CREDS = {
#     "host": "qa-db.letsdochinese.com",
#     "user": "qaauto",
#     "password": "8bbz9k",
#     "port": "3306"
# }
# db = Database(database="kjt", host=QA_DB_CREDS['host'], user=QA_DB_CREDS['user'], password=QA_DB_CREDS['password'],port=QA_DB_CREDS['port'])       
# t = Authority(db=db)
# t.query_name_from_authority_table(aid="df726970-c211-11eb-893a-0afcf0c3c7ed")