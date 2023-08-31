PRINTER_PANE: str ="xpath://div[@class='printer-main']"

def MAIN_PRINTER_TPL(printer: str) -> str:
    return f"xpath:(//div[@class='printer-main']//tbody//td[text()='{printer}'])[1]"

def MAIN_PRINTER_CLOSE_BTN_TPL(printer: str) -> str:
    return f"xpath:(//div[@class='printer-main']//tbody//td[text()='{printer}']//..//button)[1]"

def MAIN_PRINTER_STATUS_TPL(printer: str) -> str:
    return f"(//div[@class='printer-main']//tbody//td[text()='{printer}'])[1]//ancestor::tr/td[3]"

def MAIN_PRINTER_DESCRIPTION_TPL(printer: str) -> str:
    return f"(//div[@class='printer-main']//tbody//td[text()='{printer}'])[1]//ancestor::tr/td[4]"

def MAIN_PRINTER_LAST_UP_TIME_TPL(printer: str) -> str:
    return f"(//div[@class='printer-main']//tbody//td[text()='{printer}'])[1]//ancestor::tr/td[5]"

def ACK_PRINTER_TPL(printer: str) -> str:
    return f"xpath:(//div[@class='printer-ack']//tbody//td[text()='{printer}'])[1]"

def ACK_PRINTER_STATUS_TPL(printer: str) -> str:
    return f"xpath:(//div[@class='printer-ack']//tbody//td[text()='{printer}'])[1]//ancestor::tr/td[2]"

def ACK_PRINTER_DESCRIPTION_TPL(printer: str) -> str:
    return f"xpath:(//div[@class='printer-ack']//tbody//td[text()='{printer}'])[1]//ancestor::tr/td[3]"

def ACK_PRINTER_LAST_UP_TIME_TPL(printer: str) -> str:
    return f"xpath:(//div[@class='printer-ack']//tbody//td[text()='{printer}'])[1]//ancestor::tr/td[4]"