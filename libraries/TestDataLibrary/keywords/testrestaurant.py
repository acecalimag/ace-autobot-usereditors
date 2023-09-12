import random
from robot.api.deco import keyword
from autocore.bases import LibraryComponentBase
from libraries.TestDataLibrary.dto.testrestodetails import TestRestaurantDetails
from autocore import envlabels
from libraries.TestDataLibrary.data.testrestaurants import QA_TEST_RESTAURANTS, PROD_TEST_RESTAURANTS

class TestRestaurant(LibraryComponentBase):
    
    @keyword(tags=("TestRestaurant",))
    def get_test_restaurant(self, tags: str = None, _: TestRestaurantDetails = None) -> TestRestaurantDetails:
        """Get test restaurants and return the details as an object of `TestRestaurantDetails`.

        - ``tags``= Will be used to select with test restaurant to use. Multiple tags must be separated with spaces.
        If not provided, a random test restaurant will be provided.

        Accepted tags:
        ``external``, ``pos_and_oo``, ``pos_only``, ``oo_only``, ``order-receipt-2.0.ftl``,``suspended``,``ctd``,
        ``open``, ``english-only-order-receipt-2.0-larger-font.ftl``,``dynamic-order-receipt-no-totals.ftl``,
        ``dynamic-kitchen-order-receipt.ftl``, ``dynamic-order-receipt.ftl``
        """
        if self.globals.env == envlabels.QA_ENV:
            restaurants = QA_TEST_RESTAURANTS
        elif self.globals.env == envlabels.PROD_ENV:
            restaurants = PROD_TEST_RESTAURANTS
        else:
            raise Exception(
                f"No test restaurants configured for [ {self.globals.env} ] environment")

        self.logger.debug(f"Available Test Restaurants: {restaurants}")
        details = None
        if tags is None:
            details = random.choice(restaurants).get('details')

        else:
            tags = [i.lower().strip() for i in tags.split(" ") if len(i) > 0]
            self.logger.info(f"Expected tags: {tags}", also_console=True)

            for restaurant in restaurants:
                actual_tags = restaurant.get('tags')
                self.logger.info(f"aActual tags: {actual_tags}", also_console=True)
                if all(item in actual_tags for item in tags):
                    details = restaurant.get('details')
                    break

            if details is None:
                raise Exception(f"No test restaurant found with tags: {tags}!")

        self.logger.debug(details)
        return details