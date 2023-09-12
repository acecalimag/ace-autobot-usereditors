# from libraries.db.KjtDbLibrary.dto.teamassignment import TeamAssignment
from autocore.bases import DBLibraryComponent
from robot.api.deco import keyword

# from autocore.AssertsLibrary import assert_equal
# import datetime
# import arrow


class TeamAssignment(DBLibraryComponent):

    @keyword(tags=("kjt", "TeamAssignment"))
    def get_teamassignment_db(self, tname: str):
        """ TODO: Create a database query to retrieve the Team Assignment Details."""
        query = """SELECT  ut.name as Team_Name, ut.utid as Team_ID, 
                u.name as Team_Lead, ul.code as Team_Location 
                FROM kjt.userteam AS ut 
                JOIN kjt.user AS u ON ut.teamLead = u.uid 
                JOIN kjt.userlocation AS ul ON ut.location = ul.lid 
                WHERE ut.name = %s;"""
        
    
        results = self.db.execute(query, (tname,))
        # if result and len(result) > 0:
        result = results[0]
        
        details =  {
            'Team Name': result['Team_Name'],
            'Team ID': result['Team_ID'],
            'Team Lead': result['Team_Lead'],
            'Team Location': result['Team_Location']
        }
                
        # result = TeamAssignment(**details)
        self.logger.pretty_debug(data=details)
        return details

        


    @keyword(tags=("kjt", "TeamAssignment"))
    def get_agent_team(self, agent_name: str):
        """ TODO: Create a database query to retrieve the Agent's Team Assignment Details."""
        query = """SELECT  u.uid as Agent_UID, u.name as Agent_Name, 
                ut.utid as Team_ID, ut.name as Team_Name 
                FROM kjt.usermeta AS um 
                JOIN kjt.user AS u ON um.uid = u.uid 
                JOIN kjt.userteam AS ut ON um.teamId = ut.utid 
                WHERE u.name = %s;"""
        
    
        result = self.db.execute(query, (agent_name,))
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
    


    @keyword(tags=("kjt", "TeamAssignment"))
    def get_agent_uid(self, agent_name: str):
        """ TODO: Create a database query to retrieve the Agent's UID."""
        query = """Select * from kjt.user where name = %s;"""
         
        return self.db.execute(query, (agent_name,))[0]['uid']