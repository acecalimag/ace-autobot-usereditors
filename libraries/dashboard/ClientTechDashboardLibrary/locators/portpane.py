PORT_PANE: str = "xpath://div[@class='port-main']"

def MAIN_RESTAURANT_TPL(en_name: str, ex_name: str):
    return f"xpath:(//div[@class=\"port-main\"]//tbody//td[text()=\"{en_name} ({ex_name})\"])[1]"

def MAIN_CLOSE_BTN_TPL(en_name: str, ex_name: str):
    return f"xpath:(//div[@class=\"port-main\"]//tbody//td[text()=\"{en_name} ({ex_name})\"]//..//button)[1]" 

def MAIN_GATEWAY_TPL(en_name: str, ex_name: str):
    return f"xpath:(//div[@class=\"port-main\"]//tbody//td[text()=\"{en_name} ({ex_name})\"])[1]//ancestor::tr/td[3]"

def MAIN_STATUS_TPL(en_name: str, ex_name: str):
    return f"xpath:(//div[@class=\"port-main\"]//tbody//td[text()=\"{en_name} ({ex_name})\"])[1]//ancestor::tr/td[4]"

def MAIN_DESCRIPTION_TPL(en_name: str, ex_name: str):
    return f"xpath:(//div[@class=\"port-main\"]//tbody//td[text()=\"{en_name} ({ex_name})\"])[1]//ancestor::tr/td[5]"

def MAIN_LAST_UP_TIME_TPL(en_name: str, ex_name: str):
    return f"xpath:(//div[@class=\"port-main\"]//tbody//td[text()=\"{en_name} ({ex_name})\"])[1]//ancestor::tr/td[6]"

def ACK_RESTAURANT_TPL(en_name: str, ex_name: str):
    return f"(//div[@class=\"port-ack\"]//tbody//td[text()=\"{en_name} ({ex_name})\"])[1]"

def ACK_GATEWAY_TPL(en_name: str, ex_name: str):
    return f"(//div[@class=\"port-ack\"]//tbody//td[text()=\"{en_name} ({ex_name})\"])[1]//ancestor::tr/td[2]"
    
def ACK_STATUS_TPL(en_name: str, ex_name: str):
    return f"(//div[@class=\"port-ack\"]//tbody//td[text()=\"{en_name} ({ex_name})\"])[1]//ancestor::tr/td[3]"

def ACK_DESCRIPTION_TPL(en_name: str, ex_name: str):
    return f"(//div[@class=\"port-ack\"]//tbody//td[text()=\"{en_name} ({ex_name})\"])[1]//ancestor::tr/td[4]"

def ACK_LAST_UP_TIME_TPL(en_name: str, ex_name: str):
    return f"(//div[@class=\"port-ack\"]//tbody//td[text()=\"{en_name} ({ex_name})\"])[1]//ancestor::tr/td[5]"