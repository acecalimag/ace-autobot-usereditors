CONTAINER: str = "xpath://div[@data-notify='container']"
MESSAGE: str = "xpath://div[@data-notify='container']//*[@data-notify='message']"

CC_MINIMUM: str = "xpath://div[@data-notify='container']//font[contains(text(),'Order doesn\u2019t meet the Credit Card minimum.')]"
CC_MINIMUM_CLOSE_BTN: str = "xpath://div[@data-notify='container']//font[contains(text(),'Order doesn\u2019t meet the Credit Card minimum.')]/../../../button"
def MESSAGE_TPL(msg):
    return f"xpath://div[@data-notify='container']//*[@data-notify='message']//*[normalize-space()='{msg}']"

def CLOSE_BTN_OF_TPL(msg):
    return f"xpath://div[@data-notify='container']//*[@data-notify='message']//*[normalize-space()='{msg}']/../../button"
