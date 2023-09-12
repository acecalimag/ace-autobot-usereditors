from robot.api.deco import keyword
from autocore.bases import DBLibraryComponent
from libraries.db.RosDbLibrary.dto.onboardingtaskdetails import OnboardingTaskDetails


class OnboardingTaskKeywords(DBLibraryComponent):
    
    @keyword
    def query_details_from_ros_onboarding_task_table(self, rid: str, name: str, type: str, _:OnboardingTaskDetails = None) ->  list[OnboardingTaskDetails]:
        query = """SELECT x.* FROM ros.onboardingtask x
                    WHERE rid = %s
                    and x.name = %s
                    and x.type = %s;"""
                    
        results = self.db.execute(query, (rid, name, type))
        if len(results) == 0:
            raise Exception(f"In [{self.globals.env}] environment.No record found in ros.onboardingtask table with rid {rid} , name {name} and type {type}")
        
        details = [OnboardingTaskDetails(**result)  for result in results]
        self.logger.pretty_debug(data=details)
        return details