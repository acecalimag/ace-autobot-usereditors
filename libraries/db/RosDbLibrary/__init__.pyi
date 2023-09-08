from autocore.bases import DBLibraryBase
from libraries.db.RosDbLibrary.dto.onboardingrestaurantdetails import OnboardingRestaurantDetails
from libraries.db.RosDbLibrary.dto.onboardingtaskdetails import OnboardingTaskDetails


class RosDbLibrary(DBLibraryBase):
    
    # The ff method signature is from libraries.db.RosDbLibrary.keywords.onboardingrestaurant.py
    def query_using_rid_the_details_in_ros_onboarding_restaurant_table(self, rid: str, _:OnboardingRestaurantDetails = None) -> OnboardingRestaurantDetails:...
    
    # The ff method signature is from libraries.db.RosDbLibrary.keywords.onboardingtask.py
    def query_details_from_ros_onboarding_task_table(self, rid: str, name: str, type: str, _:OnboardingTaskDetails = None) ->  list[OnboardingTaskDetails]:...