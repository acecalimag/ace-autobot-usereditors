from datetime import datetime
from robot.api.deco import keyword
from autocore.bases import WebLibraryComponent
from autocore.none import AUTOCORE_NONE


class ROSLandingPageKeywords(WebLibraryComponent):
    
    @keyword
    def search_restaurant_in_onboarding_restaurant_list(self, search_keyword: str):
        """Types the `search_keyword` in the search field then wait for the results to be loaded."""
        # TODO
        pass 
    
    @keyword
    def restaurant_details_displayed_in_onboarding_restaruant_list_should_be(self, restaurant_name: str, 
                                                                             restaurant_id: str = AUTOCORE_NONE, schedule_input: str = AUTOCORE_NONE, 
                                                                             cloned_date: str | datetime = AUTOCORE_NONE, target_go_live: str | datetime = AUTOCORE_NONE,
                                                                             day_tracker: str = AUTOCORE_NONE, task_status: str = AUTOCORE_NONE):
        """Verifies that the details  of the `restaurant_name` displayed in the onboarding restaurant list matches the arguments."""
        # TODO
        pass 
    
    @keyword
    def open_create_restaurant_form_in_ros_landing_page(self):
        # TODO
        pass
    
    @keyword
    def fillout_create_restaurant_form_in_ros_landing_page(self, template: str, advanced: bool = False, restaurant_name: str = AUTOCORE_NONE, restaurant_id: str = AUTOCORE_NONE,
                                       target_go_live_available: bool = True, target_go_live_date: str | datetime = AUTOCORE_NONE, save_form: bool = False):
        """Fillout the create restaurant form using the provided arguments.
        If `save_form` is `True`, this will attempt to save the form otherwise no attempt to save will be made.
        """
        #TODO
        pass 
    
    @keyword
    def verify_create_restaurant_form_ui_in_ros_landing_page(self):
        """Verify the ui behavior and completeness of elements and labels of the create restaurant form."""
        # TODO
        pass
    
    @keyword
    def open_restaurant_in_onboarding_restaurant_list(self, restaurant_name: str):
        # TODO
        pass 
    
    @keyword
    def logout_from_ros(self):
        # TODO
        pass
    
    @keyword
    def verify_ros_landing_page_ui(self):
        """Verify the ui behavior and completeness of elements and labels of the ROS landing page."""
        # TODO
        pass
    
    @keyword
    def open_list_of_live_restaurants_from_ros_landing_page(self):
        # TODO
        pass 