from autocore.bases import WebLibraryBase
from libraries.pos.POSCommon.dto.homepagedetails import HomepageDetails


class POSCommon(WebLibraryBase):
    # The method signatures below are from libraries.pos.POSCommon.keywords.browser.py
    def open_pos_in_browser(self):...
    def close_pos(self):...
    def reload_pos(self):...
    
    # The method signatures below are from libraries.pos.POSCommon.keywords.loginpage.py
    def login_to_pos(self, username: str = None, password: str = None):...
    
    # The method signatures below are from libraries.pos.POSCommon.keywords.homepage.py
    def open_restaurant_in_pos_homepage(self, rid: str):...
    def wait_until_restaurants_are_visible_in_pos_homepage(self):...
    def get_homepage_details(self, include_restaurants: bool = False, _: HomepageDetails = None) -> HomepageDetails:...
    