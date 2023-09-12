from robot.api.deco import keyword
from autocore.bases import DBLibraryComponent
from libraries.db.RosDbLibrary.dto.onboardingrestaurantdetails import OnboardingRestaurantDetails


class OnboardingRestaurantKeywords(DBLibraryComponent):
    
    @keyword
    def query_using_rid_the_details_in_ros_onboarding_restaurant_table(self, rid: str, _:OnboardingRestaurantDetails = None) -> OnboardingRestaurantDetails:
        query = "SELECT x.* FROM ros.onboardingRestaurant x where rid = %s;"
        results = self.db.execute(query,(rid,))
        if len(results) == 0:
            raise Exception(f"In [{self.globals.env}] environment.No record found in ros.onboardingRestaurant table with rid of {rid}")
        
        details = OnboardingRestaurantDetails(**results[0])
        self.logger.pretty_debug(data=details)
        return details
    
    
