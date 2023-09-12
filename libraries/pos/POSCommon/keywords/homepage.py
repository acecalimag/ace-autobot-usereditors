from robot.api.deco import keyword
from selenium.common import TimeoutException

from libraries.pos.POSCommon.dto.homepagedetails import HomepageDetails
from libraries.pos.POSCommon.locators import  homepage,frame
from autocore.bases import WebLibraryComponent


class HomepageKeywords(WebLibraryComponent):

    @keyword(tags=("HomepageKeywords",))
    def open_restaurant_in_pos_homepage(self, rid: str):
        """Open restaurant with the provided ``rid``.

        Pre-requisite: To use this keyword, make sure that POS homepage is open.
        To go to POS homepage, see `Login To POS`.
        """
        self.wait_until_restaurants_are_visible_in_pos_homepage()

        self.web.select_frame(locator=frame.POS_RESTAURANT_FRAME)
        try:
            self.web.click(locator=f'id:{rid}')
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("HomepageKeywords",))
    def wait_until_restaurants_are_visible_in_pos_homepage(self):
        """Wait until restaurants are visible in the homepage.

        Pre-requisite: To use this keyword, make sure that POS homepage is open.
        To go to POS homepage, see `Login To POS`.
        """
        self.web.select_frame(locator=frame.POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_count_is_greater_than(locator=homepage.RESTAURANTS, count=10)
        except TimeoutException:
            raise TimeoutException("Can't wait for restaurants to be displayed.")
        finally:
            self.web.unselect_frame()

    @keyword(tags=("HomepageKeywords",))
    def get_homepage_details(self, include_restaurants: bool = False, _: HomepageDetails = None) -> HomepageDetails:
        """Get the details displayed in the homepage and return it as `HomepageDetails` object.

        If ``include_restaurants`` is set to ``True``, it will also get the names of the restaurant but will consume
        some time depending on how many restaurants are there.

        Pre-requisite: To use this keyword, make sure that POS homepage is open.
        To go to POS homepage, see `Login To POS`.

        Examples:
            | ${details}    |   Get Homepage Details            |                                   |
            | Log           |   ${details}[username]            |                                   |
            | ${details}    |   Get Homepage Details            |   include_restaurants=${True}     |
            | Log           |   ${details}[restaurants]         |                                   |
        """

        self.wait_until_restaurants_are_visible_in_pos_homepage()

        inbound_contacts = self.web.get_text(locator=homepage.CALL_COUNT)
        att = self.web.get_text(locator=homepage.AVE_DURATION_TIME)
        awt = self.web.get_text(locator=homepage.AVE_WRAP_UP_TIME)
        aht = self.web.get_text(locator=homepage.TOTAL_TIME)

        button_labels = [
            self.web.get_text(locator=homepage.MY_SCHEDULE_BTN, normalize=True),
            self.web.get_text(locator=homepage.MISTAKE_AND_COACHING_BTN, normalize=True),
            self.web.get_text(locator=homepage.NEWS_BTN, normalize=True),
            self.web.get_text(locator=homepage.CALL_HISTORY_BTN, normalize=True),
            self.web.get_text(locator=homepage.STATUS_BTN, normalize=True)
        ]

        self.web.click(locator=homepage.STATUS_BTN)
        status_options = self.web.get_texts(locator=homepage.OTHER_STATUS_OPTIONS, normalize=True)
        self.web.click(locator=homepage.STATUS_BTN)
        status_options.append(self.web.get_text(locator=homepage.STATUS_BTN, normalize=True))

        self.web.select_frame(locator=frame.POS_RESTAURANT_FRAME)
        try:
            username = self.web.get_text(locator=homepage.USERNAME)

            restaurants = []
            if include_restaurants:
                restaurants = self.web.get_texts(locator=homepage.RESTAURANTS, normalize=True)

            active = self.web.get_text(locator=homepage.ACTIVE_RESTAURANTS)
            onboarding = self.web.get_text(locator=homepage.ONBOARDING_RESTAURANTS)
            offboarding = self.web.get_text(locator=homepage.OFFBOARDING_RESTAURANTS)
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

        details = HomepageDetails(
            username=username,
            inbound_contacts=inbound_contacts,
            att=att,
            awt=awt,
            aht=aht,
            active=active,
            onboarding=onboarding,
            offboarding=offboarding,
            button_labels=button_labels,
            status_options=status_options,
            restaurants=restaurants
        )

        self.logger.debug(details)
        return details
