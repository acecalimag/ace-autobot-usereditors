
from dataclasses import dataclass
from typing import TypedDict
from robot.api.deco import keyword, library
from autocore.Database import Database



class UserTeamDB:

    def __init__(self, db: Database):
        self.__db = db

    @keyword
    def get_user_team_db(self, tname: str):
        """ TODO: Create a database query to retrieve the User Team Details."""
        query = "SELECT ut.name as Team_Name, ut.description as Team_Description, u.name as Team_Lead, ul.code as Team_Location, ut.type as Team_Type, ut.status as Team_Status, ut.updateTime as Last_Updated FROM kjt.userteam AS ut JOIN kjt.user AS u ON ut.teamLead = u.uid JOIN kjt.userlocation AS ul ON ut.location = ul.lid WHERE ut.name = %s;"
        
        result = self.__db.execute(query, (tname,))
        if result and len(result) > 0:
            row = result[0]
            return {
                'Team Name': row['Team_Name'],
                'Team Description': row['Team_Description'],
                'Team Lead': row['Team_Lead'],
                'Team Location': row['Team_Location'],
                'Team Type': row['Team_Type'].capitalize(),
                'Team Status': row['Team_Status'].capitalize(),
                'Last Updated': row['Last_Updated']
            }
        else:
            return None
        


    @keyword
    def get_agent_uid(self, agent_name: str):
        """ TODO: Create a database query to retrieve the Agent's UID."""
        query = "select * from kjt.user where name = %s;"
         
        return self.__db.execute(query, (agent_name,))[0]['uid']



    @keyword
    def get_agent_team(self, agent_name: str):
        """ TODO: Create a database query to retrieve the Agent's Team Assignment Details."""
        query = "SELECT  u.uid as Agent_UID, u.name as Agent_Name, ut.utid as Team_ID, ut.name as Team_Name FROM kjt.usermeta AS um JOIN kjt.user AS u ON um.uid = u.uid JOIN kjt.userteam AS ut ON um.teamId = ut.utid WHERE u.name = %s; "
        
    
        result = self.__db.execute(query, (agent_name,))
        if result and len(result) > 0:
            row = result[0]
            return {
                'Agent UID': row['Agent_UID'],
                'Agent Name': row['Agent_Name'],
                'Team ID': row['Team_ID'],
                'Team Name': row['Team_Name']
            }
        else:
            return {
                'message': "Agent is not assigned to a team."
            }



    @keyword
    def get_lead_uid(self, lead_name: str):
        """ TODO: Create a database query to retrieve the Team Leads's UID."""
        query = "select * from kjt.user where name = %s;"
         
        return self.__db.execute(query, (lead_name,))[0]['uid']



    @keyword
    def get_loc_code(self, loc_code: str):
        """ TODO: Create a database query to retrieve the Team Leads's UID."""
        query = "select * from kjt.userlocation where code = %s;"
         
        return self.__db.execute(query, (loc_code,))[0]['lid']



# QA_DB_CREDS = {
#     "host": "qa-db.letsdochinese.com",
#     "user": "qaauto",
#     "password": "8bbz9k",
#     "port": "3306"
# }
# db = Database(database="kjt", host=QA_DB_CREDS['host'], user=QA_DB_CREDS['user'], password=QA_DB_CREDS['password'],port=QA_DB_CREDS['port'])       
# t = Authority(db=db)
# t.query_name_from_authority_table(aid="df726970-c211-11eb-893a-0afcf0c3c7ed")