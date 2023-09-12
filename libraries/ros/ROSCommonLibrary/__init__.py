from robot.api.deco import library

from autocore.bases import WebLibraryBase
from libraries.ros.ROSCommonLibrary.keywords.browser import BrowserKeywords
from libraries.ros.ROSCommonLibrary.keywords.restaurantlandingpage import RestaurantLandingPage
from libraries.ros.ROSCommonLibrary.keywords.roslandingpage import ROSLandingPageKeywords
from libraries.ros.ROSCommonLibrary.keywords.loginpage import LoginPageKeywords
from libraries.ros.config import ROS_GLOBAL_TIMEOUT

@library(scope='GLOBAL')
class ROSCommonLibrary(WebLibraryBase):
    
    def __init__(self):
        super().__init__()
        
        components = [
            BrowserKeywords(library=self),
            LoginPageKeywords(library=self, timeout=ROS_GLOBAL_TIMEOUT),
            ROSLandingPageKeywords(library=self, timeout=ROS_GLOBAL_TIMEOUT),
            RestaurantLandingPage(library=self, timeout=ROS_GLOBAL_TIMEOUT)
        ]
        
        self.add_library_components(library_components=components)