from libraries.db.KjtDbLibrary.dto.userteamsdetails import UserTeamsDetails
from autocore.AssertsLibrary import assert_equal
from autocore.bases import DBLibraryComponent
from robot.api.deco import keyword

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

       