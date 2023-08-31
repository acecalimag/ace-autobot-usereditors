from datetime import timedelta
from robot.api.deco import keyword
from libraries.pos.POSRestaurantLibrary.dto.orderbilldetails import OrderBillDetails
from libraries.pos.POSRestaurantLibrary.dto.selecteddishdetails import SelectedDishDetails
from libraries.pos.POSRestaurantLibrary.locators.frame import POS_RESTAURANT_FRAME
from libraries.pos.POSRestaurantLibrary.locators import restaurantlanding, morelanding
from autocore.bases import WebLibraryComponent
from autocore.web.webactions import sleep


class MoreLandingKeywords(WebLibraryComponent):

    @keyword(tags=("MoreDisplayKeywords",))
    def click_mistake_button_on_more_display_view(self):
        """Click the ``MISTAKE`` button on the more display view."""
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            if self.__is_more_button_selected():
                self.web.wait_until_visible(
                    locator=morelanding.MISTAKE_BTN)
                self.web.click(locator=morelanding.MISTAKE_BTN)
            else:
                raise Exception(
                    "Mistake button is not visible in more display view.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("MoreDisplayKeywords",))
    def click_repeat_button_on_more_display_view(self):
        """Click the ``REPEAT`` button on the more display view."""
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            if self.__is_more_button_selected():
                self.web.wait_until_visible(
                    locator=morelanding.REPEAT_BTN)
                self.web.click(locator=morelanding.REPEAT_BTN)
            else:
                raise Exception(
                    "Repeat button is not visible in more display view.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("MoreDisplayKeywords",))
    def click_reprint_button_on_more_display_view(self):
        """Click the ``REPRINT`` button on the more display view."""
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            if self.__is_more_button_selected():
                self.web.wait_until_visible(
                    locator=morelanding.REPRINT_BTN)
                self.web.click(locator=morelanding.REPRINT_BTN)
            else:
                raise Exception(
                    "Reprint button is not visible in more display view.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("MoreDisplayKeywords",))
    def click_void_button_on_more_display_view(self):
        """Click the ``VOID`` button on the more display view."""
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            if self.__is_more_button_selected():
                self.web.wait_until_visible(
                    locator=morelanding.VOID_BTN)
                self.web.click(locator=morelanding.VOID_BTN)
            else:
                raise Exception(
                    "Void button is not visible in more display view.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("MoreDisplayKeywords",))
    def click_rush_button_on_more_display_view(self):
        """Click the ``RUSH`` button on the more display view."""
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            if self.__is_more_button_selected():
                self.web.wait_until_visible(
                    locator=morelanding.RUSH_BTN)
                self.web.click(locator=morelanding.RUSH_BTN)
            else:
                raise Exception(
                    "Rush button is not visible in more display view.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("MoreDisplayKeywords",))
    def click_close_button_on_more_display_view(self):
        """Click the ``CLOSE`` button on the more display view."""
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            if self.__is_more_button_selected():
                self.web.wait_until_visible(
                    locator=morelanding.CLOSE_BTN)
                self.web.click(locator=morelanding.CLOSE_BTN)
                self.web.wait_until_not_visible(
                    locator=morelanding.CLOSE_BTN)
            else:
                raise Exception(
                    "Close button is not visible in more display view.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("MoreDisplayKeywords",))
    def click_modify_button_on_more_display_view(self):
        """Click the ``MODIFY`` button on the more display view."""
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            if self.__is_more_button_selected():
                self.__click_modify()
                self.__wait_until_an_order_type_is_selected()
                self.web.click(
                    locator=restaurantlanding.PHONE_NUMBER1_FLD)
            else:
                raise Exception(
                    "Modify button is not visible in more display view.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("RestaurantKeywords",))
    def get_order_bill_details_in_more_display(self) -> OrderBillDetails:
        """Get the order bill details displayed in more display and return it as `OrderBillDetails` object.

        Pre-requisite: To use this keyword make sure that an order is selected. See `View Details Of Order`.

        Examples:
            | ${details}    |   Get Order Bill Details In More Display              |
            | Log           |   ${details}[discount]                                |           
            | ${details}    |   Get Order Bill Details In More Display              |
            | Log           |   ${details}[total]                                   |
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(
                locator=morelanding.MTOTAL)
            details = OrderBillDetails(
                discount=self.web.get_text(
                    locator=morelanding.MDISCOUNT),
                subtotal=self.web.get_text(
                    locator=morelanding.MSUBTOTAL).split("$")[1],
                tax=self.web.get_text(
                    locator=morelanding.MTAX).replace("$", ""),
                delivery=self.web.get_text(
                    locator=morelanding.MDELIVERY).replace("$",""),
                total=self.web.get_text(
                    locator=morelanding.MTOTAL).split('$')[1]
            )
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
        
        self.logger.debug(details)
        return details

    def __click_modify(self):
        self.web.wait_until_visible(locator=morelanding.MODIFY_BTN)

        try_count = 6
        while self.web.is_visible(locator=morelanding.MODIFY_BTN, timeout=timedelta(seconds=1)):
            if try_count == 0:
                self.web.capture_page_screenshot()
                raise Exception("Can't click MODIFY button.")

            self.web.click(locator=morelanding.MODIFY_BTN)
            try:
                self.web.wait_until_not_visible(
                    locator=morelanding.MODIFY_BTN, timeout=timedelta(seconds=5))
                break
            except Exception:
                try_count -= 1

    def __is_more_button_selected(self) -> bool:
        return self.web.attribute_ends_with(locator=restaurantlanding.MORE_BTN, attribute="class",
                                             exp_value="selected")

    def __wait_until_an_order_type_is_selected(self):
        for i in range(10):
            if self.web.attribute_ends_with(locator=restaurantlanding.PICKUP_BTN, attribute="class",
                                             exp_value="selected"):
                break
            if self.web.attribute_ends_with(locator=restaurantlanding.DELIVERY_BTN, attribute="class",
                                             exp_value="selected"):
                break
            sleep(seconds=0.5)


    @keyword(tags=("RestaurantKeywords", "OrderDisplayKeywords"))
    def get_details_of_the_ordered_dishes_in_more_display(self, _: SelectedDishDetails = None) -> list[SelectedDishDetails]:
        """Get the details of the selected dishes from the more order display area and return is as an object of `SelectedDishDetails`.

        Pre-requisite: To use this keyword make sure that an order is selected in more display view. See `View Details Of Order`.

        Examples:
            | ${details}    |   Get Details Of The Selected Dishes              |
            | Log           |   ${details}[quantity]                            |
            | ${details}    |   Get Details Of The Selected Dishes              |
            | Log           |   ${details}[price]                               |
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(locator=morelanding.ORDER_DISPLAY)
            item_count = self.web.count(locator=morelanding.ORDER_ITEM_DIV)

            details = []
            for i in range(1, item_count + 1):
                details.append(
                    SelectedDishDetails(
                        quantity=self.web.get_text(locator=morelanding.ORDER_QUANTITY_INDEXED_TPL.format(i)),
                        size=self.web.get_text(locator=morelanding.ORDER_SIZE_INDEXED_TPL.format(i)),

                        description=self.web.get_text(
                            locator=morelanding.ORDER_DESCRIPTION_INDEXED_TPL.format(i)),

                        price=self.web.get_text(
                            locator=morelanding.ORDER_PRICE_INDEXED_TPL.format(i)).replace("$", "")
                    )
                )
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
        self.logger.debug(details)
        return details