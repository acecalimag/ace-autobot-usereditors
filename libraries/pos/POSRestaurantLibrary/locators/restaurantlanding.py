# Bill details section
DISCOUNT: str = "id:discount"
SUBTOTAL: str = "id:subtotal"
TAX_AMOUNT: str = "id:taxamount"
DELIVERY_FEE: str = "id:devfee"
GRAND_TOTAL: str = "id:grandtotal"

# Buttons in the landing page
HOME_BTN: str = "id:cancel"
SEND_BTN: str = "id:send"
CREDIT_CARD_BTN: str = "id:pay"
PICKUP_BTN: str = "id:pickup"
DELIVERY_BTN: str = "id:delivery"
ONLINE_BTN: str = "id:online"
MORE_BTN: str = "id:more"
SAVE: str = "id:save"
ADD_ORDER_QTY_BTN: str = "id:add"
MINUS_QUANTITY_BTN: str = "id:minus"

SUB_ORDER_NUMBER: str = "id:subOrderNumber"
SUB_ORDERS_BANNER: str = "xpath://button[@id='moreSubOrders' and text()='SUB-ORDERS']"

# Restaurant display area
DISPLAY_AREA_RESTAURANT_COMMENT: str = "xpath://div[@id='resdisplayarea']//*[@id='rescomment']"

# Selected dishes area
ORDER_DISPLAY: str = "id:orderdisplay"
ORDERED_DISH_ITEM_NAMES: str = "xpath://div[@id='orderdisplay']//div[contains(@class,'itemName')]"
ORDER_ITEM_DIV: str = "//div[@id='orderdisplay']/div[@class='table']/div[not(contains(@class,'th'))]"
ORDER_QUANTITY_INDEXED_TPL: str = "(//div[@id='orderdisplay']//div[contains(@class,'tr dish')])[{0}]/div[@class='td qty']"  # param is 1 based index
ORDER_SIZE_INDEXED_TPL: str = "(//div[@id='orderdisplay']//div[contains(@class,'tr dish')])[{0}]/div[@class='td size']"  # param is 1 based index
ORDER_DESCRIPTION_INDEXED_TPL: str = "(//div[@id='orderdisplay']//div[contains(@class,'tr dish')])[{0}]/div[@class='td itemName description']"  # param is 1 based index
ORDER_PRICE_INDEXED_TPL: str = "(//div[@id='orderdisplay']//div[contains(@class,'tr dish')])[{0}]/div[4]"  # param is 1 based index

# Customer Order Form
PHONE_NUMBER1_FLD: str = "id:originPhone"
PHONE_NUMBER2_FLD: str = "id:originPhone2"
NAME_FLD: str = "id:name"
STREET_FLD: str = "id:address1"
ADDRESS2_FLD: str = "id:address2"
MILES: str = "id:miles"
CITY_FLD: str = "id:city"
ORDER_REMARK_FLD: str = "id:custspnote"
CONF_NOTE_FLD: str = "id:comment"
APT_ADDRESS_TYPE_BTN: str = "id:addressType_apt"
HOUSE_ADDRESS_TYPE_BTN: str = "id:addressType_hse"
BIZ_ADDRESS_TYPE_BTN: str = "id:addressType_biz"
CALL_SKILL_DF: str = "id:cskill-diff"
CALL_SKILL_SP: str = "id:cskill-esp"
CALL_SKILL_CH: str = "id:cskill-ch"
CALL_SKILL_SB: str = "id:cskill-swb"
NEW_SUB_ORDER_BTN: str = "id:newSubOrder"