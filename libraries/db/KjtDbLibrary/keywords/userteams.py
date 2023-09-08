from libraries.db.KjtDbLibrary.dto.userteamsdetails import UserTeamsDetails
from libraries.db.KjtDbLibrary.dto.userteamsdetails import UserTeamsDetails1
from autocore.AssertsLibrary import assert_equal
from autocore.bases import DBLibraryComponent
from robot.api.deco import keyword
import datetime
# import arrow


class UserTeams(DBLibraryComponent):

    @keyword(tags=("kjt", "UserTeams"))
    def query_user_teams_details(self, name: str, _: UserTeamsDetails = None) -> UserTeamsDetails:
        """Query the details of the userteam using the ``name`` provided and return it as `UserTeamsDetails`"""    
        query = """SELECT utid, name, location, type, status 
                FROM kjt.userteam 
                WHERE name = %s;"""
        results = self.db.execute(query, (name,))
        result = results[0]
        details = UserTeamsDetails(
            utid=result['utid'], name=result['name'], type=result['type'], status=result['status']
        )
        self.logger.pretty_debug(data=details)
        return details
    

    @keyword(tags=("kjt", "UserTeams"))
    def user_team_type_should_be(self, name: str, exp_type: str):
        ut_details = self.query_user_teams_details(name=name)
        self.logger.pretty_debug(data=ut_details)
        act_ut_type = ut_details['type']
        assert_equal(actual=act_ut_type, exp=exp_type, desc="User team type: ")



##############################################################################################################################



    @keyword
    def get_user_team_details_db(self, tname: str, _: UserTeamsDetails1 = None) -> UserTeamsDetails1:
        """ TODO: Create a database query to retrieve the User Team Details."""
        query = """SELECT ut.utid as Team_UTID, ut.name as Team_Name, ut.description as Team_Description, 
        u.name as Team_Lead, ul.code as Team_Location, ut.type as Team_Type, ut.status as Team_Status, 
        ut.updateTime as Last_Updated 
        FROM kjt.userteam AS ut 
        JOIN kjt.user AS u ON ut.teamLead = u.uid 
        JOIN kjt.userlocation AS ul ON ut.location = ul.lid 
        WHERE ut.name = %s;"""
        
        
        results = self.db.execute(query, (tname,))
        # if result and len(result) > 0:
        result = results[0]

        # Convert and format the Team Type
        team_type = result['Team_Type'].lower()
        formatted_team_type = team_type.replace('nonoperational', 'Non-Operational').title()

            # # Last Updated
            # last_updated = ""
            # if row['Last_Updated']:
            #     last_updated = arrow.get(row['Last_Updated']).format("MMM DD, YYYY h:mm A")


        # Last Updated
        last_updated = ""
        if result['Last_Updated']:
            last_updated_datetime = (datetime.datetime.strptime(result['Last_Updated'], "%Y-%m-%d %H:%M:%S")
                                    if isinstance(result['Last_Updated'], str) else result['Last_Updated'])
            # Format the hour without leading zero
            last_updated_hour = int(last_updated_datetime.strftime("%I"))
            last_updated = last_updated_datetime.strftime("%b %d, %Y {:d}:%M %p").format(last_updated_hour)
        
        details = {
            'Team UTID': result['Team_UTID'],
            'Team Name': result['Team_Name'],
            'Team Description': result['Team_Description'],
            'Team Lead': result['Team_Lead'],
            'Team Location': result['Team_Location'],
            'Team Type': formatted_team_type,
            'Team Status': result['Team_Status'].capitalize(),
            'Last Updated': last_updated
        }

        details = UserTeamsDetails1(**details)
        
        self.logger.pretty_debug(data=details)
        return details



    @keyword(tags=("kjt", "UserTeams"))
    def get_user_team_raw_db(self, tname: str):
        """ TODO: Create a database query to retrieve the User Team Details."""
        query = """SELECT ut.utid as Team_UTID, ut.name as Team_Name, ut.description as Team_Description, 
        u.uid as Team_Lead, ul.lid as Team_Location, ut.type as Team_Type, ut.status as Team_Status, 
        ut.updateTime as Last_Updated 
        FROM kjt.userteam AS ut 
        JOIN kjt.user AS u ON ut.teamLead = u.uid 
        JOIN kjt.userlocation AS ul ON ut.location = ul.lid 
        WHERE ut.name = %s;"""
        
        
        results = self.db.execute(query, (tname,))

        result = results[0]

            # # Last Updated
            # last_updated = ""
            # if row['Last_Updated']:
            #     last_updated = arrow.get(row['Last_Updated']).format("MMM DD, YYYY h:mm A")

        # Last Updated
        last_updated = ""
        if result['Last_Updated']:
            last_updated_datetime = (datetime.datetime.strptime(result['Last_Updated'], "%Y-%m-%d %H:%M:%S")
                                    if isinstance(result['Last_Updated'], str) else result['Last_Updated'])
            last_updated = last_updated_datetime.strftime("%b %d, %Y %#I:%M %p")

        details = {
            'Team UTID': result['Team_UTID'],
            'Team Name': result['Team_Name'],
            'Team Description': result['Team_Description'],
            'Team Lead': result['Team_Lead'],
            'Team Location': result['Team_Location'],
            'Team Type': result['Team_Type'],
            'Team Status': result['Team_Status'].capitalize(),
            'Last Updated': last_updated
        }

        details = UserTeamsDetails1(**details)
        
        self.logger.pretty_debug(data=details)
        return details


        

    @keyword(tags=("kjt", "UserTeams"))
    def get_lead_loc_(self, lname: str):
        """ TODO: Create a database query to retrieve the Agent's Team Assignment Details."""
        query = "SELECT u.username, u.name, u.uid, um.position, ul.code, ul.location, ul.lid FROM kjt.usermeta AS um JOIN kjt.user AS u ON um.uid = u.uid JOIN kjt.userlocation AS ul ON um.lid = ul.lid WHERE u.name = %s; "
        
    
        result = self.db.execute(query, (lname,))
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