from robot.api.deco import library
from autocore.bases import LibraryBase
from libraries.TestDataLibrary.keywords.testcreditcard import TestCreditCard
from libraries.TestDataLibrary.keywords.testcustomer import TestCustomer
from libraries.TestDataLibrary.keywords.testrestaurant import TestRestaurant
from libraries.TestDataLibrary.keywords.testuseraccounts import TestUserAccounts

@library(scope='GLOBAL')
class TestDataLibrary(LibraryBase):

    def __init__(self):
        LibraryBase.__init__(self)
        components = [
            TestCustomer(library=self),
            TestUserAccounts(library=self),
            TestCreditCard(library=self),
            TestRestaurant(library=self)
        ]
        
        self.add_library_components(library_components=components)

   
