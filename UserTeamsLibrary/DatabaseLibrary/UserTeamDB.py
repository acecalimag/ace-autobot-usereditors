
from robot.api.deco import keyword
from autocore.Database import Database
import arrow

class UserTeamDB:

    def __init__(self, db: Database):
        self.__db = db

    @keyword
    def get_user_team_db(self, tname: str):
        """ TODO: Create a database query to retrieve the User Team Details."""
        query = "SELECT ut.utid as Team_UTID, ut.name as Team_Name, ut.description as Team_Description, u.name as Team_Lead, ul.code as Team_Location, ut.type as Team_Type, ut.status as Team_Status, ut.updateTime as Last_Updated FROM kjt.userteam AS ut JOIN kjt.user AS u ON ut.teamLead = u.uid JOIN kjt.userlocation AS ul ON ut.location = ul.lid WHERE ut.name = %s;"
        
        
        result = self.__db.execute(query, (tname,))
        if result and len(result) > 0:
            row = result[0]

            # Convert and format the Team Type
            team_type = row['Team_Type'].lower()
            formatted_team_type = team_type.replace('nonoperational', 'Non-Operational').title()

            # Last Updated
            last_updated = ""
            if row['Last_Updated']:
                last_updated = arrow.get(row['Last_Updated']).format("MMM DD, YYYY h:mm A")

            return {
                'Team UTID': row['Team_UTID'],
                'Team Name': row['Team_Name'],
                'Team Description': row['Team_Description'],
                'Team Lead': row['Team_Lead'],
                'Team Location': row['Team_Location'],
                'Team Type': formatted_team_type,
                'Team Status': row['Team_Status'].capitalize(),
                'Last Updated': last_updated
            }
        else:
            return None


    @keyword
    def get_user_team_raw_db(self, tname: str):
        """ TODO: Create a database query to retrieve the User Team Details."""
        query = "SELECT ut.utid as Team_UTID, ut.name as Team_Name, ut.description as Team_Description, u.uid as Team_Lead, ul.lid as Team_Location, ut.type as Team_Type, ut.status as Team_Status, ut.updateTime as Last_Updated FROM kjt.userteam AS ut JOIN kjt.user AS u ON ut.teamLead = u.uid JOIN kjt.userlocation AS ul ON ut.location = ul.lid WHERE ut.name = %s;"
        
        
        result = self.__db.execute(query, (tname,))
        if result and len(result) > 0:
            row = result[0]

            # Last Updated
            last_updated = ""
            if row['Last_Updated']:
                last_updated = arrow.get(row['Last_Updated']).format("MMM DD, YYYY h:mm A")

            return {
                'Team UTID': row['Team_UTID'],
                'Team Name': row['Team_Name'],
                'Team Description': row['Team_Description'],
                'Team Lead': row['Team_Lead'],
                'Team Location': row['Team_Location'],
                'Team Type': row['Team_Type'],
                'Team Status': row['Team_Status'].capitalize(),
                'Last Updated': last_updated
            }
        else:
            return None

        

    @keyword
    def get_lead_loc_(self, lname: str):
        """ TODO: Create a database query to retrieve the Agent's Team Assignment Details."""
        query = "SELECT u.username, u.name, u.uid, um.position, ul.code, ul.location, ul.lid FROM kjt.usermeta AS um JOIN kjt.user AS u ON um.uid = u.uid JOIN kjt.userlocation AS ul ON um.lid = ul.lid WHERE u.name = %s; "
        
    
        result = self.__db.execute(query, (lname,))
        if result and len(result) > 0:
            row = result[0]
            return {
                'username': row['username'],
                'name': row['name'],
                'lead_uid': row['uid'],
                'location': row['location'],
                'loc_code': row['code'],
                'loc_id': row['lid'],
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