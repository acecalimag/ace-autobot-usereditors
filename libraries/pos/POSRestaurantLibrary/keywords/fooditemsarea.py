import random
from datetime import timedelta

from robot.api.deco import keyword

from libraries.pos.POSRestaurantLibrary.locators.frame import POS_RESTAURANT_FRAME
from libraries.pos.POSRestaurantLibrary.locators import fooditemsarea, restaurantlanding, morelanding
from libraries.pos.POSRestaurantLibrary.locators.modals import infomodal
from autocore.bases import WebLibraryComponent


class FoodItemsAreaKeywords(WebLibraryComponent):

        
    @keyword
    def select_dish_with_subtotal(self, subtotal: str, higher_than_subtotal: bool = True, dismiss_popups: bool = True):
        try:
            subtotal = float(subtotal)
            
            if subtotal < 0:
                raise Exception()
    
        except Exception:
            self.logger.info(f"The subtotal: {subtotal} is not valid. Must be a positive number. Selecting one dish only.")
            return self.select_dish(count=1)
        
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            if dismiss_popups:
                self.__dismiss_delivery_info_modal()
            
            act_subtotal = 0.0
            
            if higher_than_subtotal:
                try_count = 50
                while act_subtotal < subtotal:
                    if try_count == 0:
                        raise Exception(f"Maximum number of tries reached. {try_count}. Consider lowering the subtotal.")
                    self.__select_dish_helper(count=1, dismiss_popups=dismiss_popups)
                    act_subtotal=self.web.get_text(locator=restaurantlanding.SUBTOTAL).split("$")[1]
                    act_subtotal=float(act_subtotal)
                    try_count -= 1
            else:
                self.__select_dish_helper(count=1, dismiss_popups=dismiss_popups)
                act_subtotal=self.web.get_text(locator=restaurantlanding.SUBTOTAL).split("$")[1]
                act_subtotal=float(act_subtotal)
                
                try_count = 50
                while act_subtotal > subtotal:
                    if try_count == 0:
                        raise Exception(f"Maximum number of tries reached. {try_count}. The subtotal may be too low.")
                    self.web.click(locator=restaurantlanding.MINUS_QUANTITY_BTN)
                    self.__select_dish_helper(count=1, dismiss_popups=dismiss_popups)
                    act_subtotal=self.web.get_text(locator=restaurantlanding.SUBTOTAL).split("$")[1]
                    act_subtotal=float(act_subtotal)
                    try_count -= 1
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
        

    @keyword(tags=("RestaurantKeywords", "FoodItemsAreaKeywords"))
    def select_dish(self, count: str = 1, dish_name: str = None, dismiss_popups: bool = True):
        """Select dishes based on the dishes displayed that are selectable.

        If current page is the more display page, it will be automatically closed.

        - ``count``: the number of dishes that will be selected
        - ``dish_name``: the name of dish that will be selected. If not provided, a dish will be selected randomly
        - ``dismiss_popups``: If ``True``, will dismiss popups displayed when selecting a dish. Dish note reminder, Combo Form.

        Pre-requisite: To use this keyword make sure that a restaurant is open. See `Open Restaurant In POS Homepage`.
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            if dismiss_popups:
                self.__dismiss_delivery_info_modal()
            self.__select_dish_helper(count=count, dish_name=dish_name, dismiss_popups=dismiss_popups)
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    def __select_dish_helper(self, count: str = 1, dish_name: str = None, dismiss_popups: bool = True):
        self.__close_more_display()

        self.web.wait_until_visible(locator=fooditemsarea.DISH_AREA)
        
        self.web.wait_until_count_is_greater_than(locator=fooditemsarea.LIST_SELECTABLE_DISHES, count=1)

        # Get Selectable Dishes
        selectable_dishes_count = self.web.count(locator=fooditemsarea.LIST_SELECTABLE_DISHES)
        selectable_dishes_details: list[dict] = []

        for i in range(1, selectable_dishes_count + 1):
            display_text = self.web.get_text(
                locator=fooditemsarea.SELECTABLE_DISHES_TEXT_INDEXED_TPL.format(i), normalize=True)
            dish_id = self.web.get_attribute(
                locator=fooditemsarea.SELECTABLE_DISHES_DIV_INDEXED_TPL.format(i), attribute="id")
            dish_cn = self.web.get_attribute(
                locator=fooditemsarea.SELECTABLE_DISHES_DIV_INDEXED_TPL.format(i), attribute="data-cn")
            selectable_dishes_details.append({
                "display_text": display_text,
                "dish_id": dish_id,
                "dish_cn": dish_cn
            })

        # Select Dishes
        selected_dishes: list[dict] = []
        if dish_name is not None:
            for i in range(int(count)):
                for dish in selectable_dishes_details:
                    if dish.get("display_text").lower().replace(" ", "") == dish_name.lower().replace(" ", ""):
                        self.web.click(locator=f"id:{dish.get('dish_id')}")
                        if dismiss_popups:
                            self.__dismiss_popups()
                        selected_dishes.append(dish)

        else:
            for i in range(int(count)):
                dish = random.choice(selectable_dishes_details)
                self.web.click(locator=f"id:{dish.get('dish_id')}")
                if dismiss_popups:
                    self.__dismiss_popups()
                selected_dishes.append(dish)


    def __dismiss_popups(self):
        self.__dismiss_dish_note_reminder()
        self.__dismiss_combo_form()

    def __dismiss_dish_note_reminder(self):
        if self.web.is_visible(locator=fooditemsarea.DISH_NOTE_REMINDER, timeout=timedelta(seconds=0.3)):
            self.web.click(locator=fooditemsarea.DISH_NOTE_REMINDER_CLOSE_BTN)

    def __dismiss_combo_form(self):
        if self.web.is_visible(locator=fooditemsarea.COMBO_FORM, timeout=timedelta(seconds=0.3)):
            self.web.click(locator=fooditemsarea.COMBO_FORM_CLOSE_BUTTON)
            
    def __dismiss_delivery_info_modal(self):
        if self.web.is_visible(locator=infomodal.HEADER, timeout=timedelta(seconds=0.5)):
                self.web.click(locator=infomodal.OK_BTN)
                self.web.wait_until_not_visible(locator=infomodal.HEADER)

    def __close_more_display(self):
        if self.web.attribute_ends_with(locator=restaurantlanding.MORE_BTN, attribute="class",
                                            exp_value="selected"):
            self.web.click(locator=morelanding.CLOSE_BTN)