VOID_BTN: str = "xpath://button[@id='voidBtn' and text()='Void']"
CANCEL_BTN: str = "xpath://button[@id='cancelVoidBtn' and text()='Cancel']"
MODAL_TITLE: str = "xpath://div[@id='voidOrderModal']//h4[contains(text(),'Void Order')]"
ORDER_NUMBER: str = "xpath://div[@id='voidOrderModal']//td[@id='orderNum']"
CUST_PHONE: str = "xpath://div[@id='voidOrderModal']//td[@id='custPhone']"
TIME: str = "xpath://div[@id='voidOrderModal']//td[@id='time']"
SELECTED_COMMENT: str = "xpath://div[@id='voidOrderModal']//input[@id='orderComment']"
OPTION_LABELS: str = "xpath://div[@id='voidOrderModal']//div[@id='orderCommentOpt']//label"


def OPTION_WITH_LABEL(label):
    return f"xpath://div[@id='voidOrderModal']//div[@id='orderCommentOpt']//label[normalize-space()='{label}']"
