from autocore.bases import DBLibraryBase
from robot.api.deco import library

from libraries.db.RosDbLibrary.keywords.onboardingrestaurant import OnboardingRestaurantKeywords
from libraries.db.RosDbLibrary.keywords.onboardingtask import OnboardingTaskKeywords

@library(scope='GLOBAL')
class RosDbLibrary(DBLibraryBase):
    
    def __init__(self):
        super().__init__(db='ros')
        components = [
            OnboardingRestaurantKeywords(library=self),
            OnboardingTaskKeywords(library=self)
        ]
        self.add_library_components(library_components=components)
        
    
    
    