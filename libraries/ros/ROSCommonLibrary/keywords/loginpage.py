""" This module contains all the keywords related to the Login page of ROS """
from robot.api.deco import keyword
from autocore.none import AUTOCORE_NONE
from autocore.bases import WebLibraryComponent


class LoginPageKeywords(WebLibraryComponent):
    
    @keyword
    def login_to_ros(self, username:str = AUTOCORE_NONE, password: str = AUTOCORE_NONE):
        """Login to ROS using the provided `username` and `password`.
        Regardless if all arguments were provided or not, login attempt will always be made.
        """
        # TODO
        pass 
    
    @keyword
    def verify_ros_login_error_message(self):
        """Verify that the login error message displayed when attempting to login with invalid credentials is correct."""
        #TODO
        pass
    
    @keyword
    def verify_ros_login_page_ui(self):
        "Verifies the static texts and completeness of the element in the ROS login page."
        #TODO
        pass
    
    