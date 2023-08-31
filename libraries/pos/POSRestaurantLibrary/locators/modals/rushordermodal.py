TITLE: str = "xpath://div[@id='rushOrderModal']//h4"
ORDER_NUMBER: str = "xpath://div[@id='rushOrderModal']//td[@id='orderNum']"
CUST_PHONE: str = "xpath://div[@id='rushOrderModal']//td[@id='custPhone']"
TIME: str = "xpath://div[@id='rushOrderModal']//td[@id='time']"
SELECTED_COMMENT: str = "xpath://div[@id='rushOrderModal']//input[@id='orderComment']"

COMMENT_LABELS: str = "xpath://div[@id='rushOrderModal']//label[@class='rushLabel']"
RUSH_BTN: str = "xpath://div[@id='rushOrderModal']//button[@id='rushBtn' and text()='Rush']"
CANCEL_BTN: str = "xpath://div[@id='rushOrderModal']//button[@id='cancelRushBtn' and text()='Cancel']"


def COMMENT_LABELS_INDEXED(index):
    return f"xpath:(//div[@id='rushOrderModal']//label[@class='rushLabel'])[{index}]"
