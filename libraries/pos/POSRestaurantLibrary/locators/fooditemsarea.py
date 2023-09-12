# Dishes displayed
DISH_AREA: str = "id:fooditemsarea"
LIST_SELECTABLE_DISHES: str = "//div[@id='fooditemsarea']/div[@title and not(contains(@style,'opacity'))  and not(contains(@class,'hidden'))]/div"
SELECTABLE_DISHES_TEXT_INDEXED_TPL: str = "xpath:(//div[@id='fooditemsarea']/div[@title and not(contains(@style,'opacity'))  and not(contains(@class,'hidden'))]/div)[{0}]"
SELECTABLE_DISHES_DIV_INDEXED_TPL: str = "xpath:(//div[@id='fooditemsarea']/div[@title and not(contains(@style,'opacity'))  and not(contains(@class,'hidden'))])[{0}]"

# Combo form
COMBO_FORM: str = "xpath://div[@aria-describedby='comboform']"
COMBO_FORM_CLOSE_BUTTON: str = "xpath://div[@aria-describedby='comboform']//button[text()='Close']"

# Dish note reminder
DISH_NOTE_REMINDER: str = "xpath://div[@aria-describedby='dishnotereminder']"
DISH_NOTE_REMINDER_CLOSE_BTN: str = "xpath://div[@aria-describedby='dishnotereminder']//button[text()='Close']"



