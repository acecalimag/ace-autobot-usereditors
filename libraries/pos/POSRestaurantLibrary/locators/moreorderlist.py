ORDER_LIST_LOADER_IMG: str = "xpath://div[@id='orderdiv']//*[@id='orderlist']//*[@class='ordtable']//img"

ORDER_AREA: str = "xpath://div[@id='orderdiv']//*[@id='orderlist']"

ORDERS: str = "xpath://div[@id='orderlist']//div[@id]"


def ORDERS_DIV(index):
    return f"xpath:(//div[@id='orderlist']//div[@id])[{index}]"


def ORDER_DESC(index):
    return f"xpath:(//div[@id='orderlist']//div[@id]/div)[{index}]"


def ORDER_DESC_USING_ID(el_id):
    return f"//div[@id='{el_id}']/div"


SENT_ORDERS: str = "xpath://div[@id='orderlist']//div[contains(@class,'status_new')]"


def SENT_ORDERS_DIV(index):
    return f"xpath:(//div[@id='orderlist']//div[contains(@class,'status_new')])[{index}]"


def SENT_ORDER_DESC(index):
    return f"xpath:(//div[@id='orderlist']//div[contains(@class,'status_new')]/div)[{index}]"


SAVED_ORDERS: str = "xpath://div[@id='orderlist']//div[contains(@class,'status_onhold')]"


def SAVED_ORDERS_DIV(index):
    return f"xpath:(//div[@id='orderlist']//div[contains(@class,'status_onhold')])[{index}]"


def SAVED_ORDER_DESC(index):
    return f"xpath:(//div[@id='orderlist']//div[contains(@class,'status_onhold')]/div)[{index}]"


CANCELLED_ORDERS: str = "xpath://div[@id='orderlist']//div[contains(@class,'status_canceled')]"


def CANCELLED_ORDERS_DIV(index):
    return f"xpath:(//div[@id='orderlist']//div[contains(@class,'status_canceled')])[{index}]"


def CANCELLED_ORDER_DESC(index):
    return f"xpath:(//div[@id='orderlist']//div[contains(@class,'status_canceled')]/div)[{index}]"
