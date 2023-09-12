from libraries.db.KjtDbLibrary.dto.agentdetails import AgentDetails
from autocore.AssertsLibrary import assert_equal
from autocore.bases import DBLibraryComponent
from robot.api.deco import keyword

class Agent(DBLibraryComponent):

    @keyword(tags=("kjt", "Agent"))
    def query_agent_details(self, uid: str, _: AgentDetails = None) -> AgentDetails:
        """Query the details of the agent using the ``uid`` provided and return it as `AgentDetails`"""    
        query = """SELECT u.uid, u.username, u.name, um.position, ul.code 
                   FROM kjt.user u join kjt.usermeta um on u.uid = um.uid join kjt .userlocation ul on um.lid = ul.lid 
                   WHERE u.uid = %s;"""
        results = self.db.execute(query, (uid,))
        result = results[0]
        details = AgentDetails(
            uid=result['uid'], username=result['username'], name=result['name'], position=result['position'], location=result['code']
        )
        self.logger.pretty_debug(data=details)
        return details
    
    @keyword(tags=("kjt", "Agent"))
    def agent_location_code_should_be(self, uid: str, exp_loc: str):
        agent_details = self.query_agent_details(uid=uid)
        self.logger.pretty_debug(data=agent_details)
        act_loc_code = agent_details['location']
        assert_equal(actual=act_loc_code, exp=exp_loc, desc="Agent location.")

       