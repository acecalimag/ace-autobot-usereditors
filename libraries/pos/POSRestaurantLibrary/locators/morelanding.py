# Buttons in the more display landing page
CLOSE_BTN: str = "xpath://div[@id='close']//div[text()='CLOSE']"
MODIFY_BTN: str = "xpath://div[@id='modify']//div[text()='MODIFY']"
VOID_BTN: str = "xpath://div[@id='void']//div[text()='VOID']"
RUSH_BTN: str = "xpath://div[@id='rush']//div[text()='RUSH']"
REPRINT_BTN: str = "xpath://div[@id='print']//div[text()='REPRINT']"
REPEAT_BTN: str = "xpath://div[@id='repeat']//div[text()='REPEAT']"
MISTAKE_BTN: str = "xpath://div[@id='mistake']//div[text()='MISTAKE']"

# Bill Details in the more display page
MDISCOUNT: str = "xpath://td[text()='DISCOUNT:']//following-sibling::td//span[@id='mdiscount']"
MSUBTOTAL: str = "xpath://td[text()='SUBTOTAL:']//following-sibling::td[@id='msubtotal']"
MTAX: str = "xpath://td[contains(text(),'TAX')]//following-sibling::td[@id='mtaxamount']"
MDELIVERY: str = "xpath://td[text()='DELIVERY:']//following-sibling::td[@id='mdeliveryfee']"
MTOTAL: str = "xpath://td[text()='TOTAL:']//following-sibling::td[@id='mgrandtotal']"

# Ordered dish details in more display page
ORDER_DISPLAY: str = "id:morderinfo"
ORDER_ITEM_DIV: str = "xpath://div[@id='morderinfo']/div[@class='table']/div[not(contains(@class,'th'))]"
ORDER_QUANTITY_INDEXED_TPL: str = "xpath:(//div[@id='morderinfo']//div[contains(@class,'tr dish')])[{0}]/div[@class='td qty']"  # param is 1 based index
ORDER_SIZE_INDEXED_TPL: str = "xpath:(//div[@id='morderinfo']//div[contains(@class,'tr dish')])[{0}]/div[@class='td size']"  # param is 1 based index
ORDER_DESCRIPTION_INDEXED_TPL: str = "xpath:(//div[@id='morderinfo']//div[contains(@class,'tr dish')])[{0}]/div[@class='td itemName description']"  # param is 1 based index
ORDER_PRICE_INDEXED_TPL: str = "xpath:(//div[@id='morderinfo']//div[contains(@class,'tr dish')])[{0}]/div[4]"  # param is 1 based index

# Order details in more display page
ORDER_DETAILS_AREA: str = "id:custdisplay"
ORDER_NUMBER: str = "xpath://div[@id='custdisplay']//th[text()='Order ' and @class='ordnum']//span"
ORDER_VERSION: str = "xpath://div[@id='custdisplay']//*[text()='Version #' and @class='ordver']//span"
AGENT: str = "xpath://div[@id='custdisplay']//th[text()='Agent']//following-sibling::td[@class='server']"
PAYMENT_TYPE: str = "xpath://div[@id='custdisplay']//th[text()='Agent']//following-sibling::td[contains(@class,'trans')]"
ORDER_TYPE: str = "xpath://div[@id='custdisplay']//th[text()='Order Type']//following-sibling::td[@class='ordtype']"
ORDER_STATUS: str = "xpath://div[@id='custdisplay']//th[text()='Order Type']//following-sibling::td[contains(@class,'custstatus')]"
PHONE: str = "xpath://div[@id='custdisplay']//th[text()='Phone']//following-sibling::td[@class='custphone']"
CUSTOMER_NAME: str = "xpath://div[@id='custdisplay']//th[text()='Name']//following-sibling::td[@class='custname']"
STREET1: str = "xpath://div[@id='custdisplay']//th[text()='Street']//following-sibling::td[@class='address']"
ADDRESS_TYPE: str = "xpath://div[@id='custdisplay']//th[text()='Street']//following-sibling::td[@class='address']/span"
STREET2: str = "xpath://div[@id='custdisplay']//th[text()='Street2']//following-sibling::td[@class='address2']"
CITY: str = "xpath://div[@id='custdisplay']//th[text()='City']//following-sibling::td[@class='custcity']"
ORDER_REMARK: str = "xpath://div[@id='custdisplay']//th[text()='Order Remark']//following-sibling::td[contains(@class,'spnote')]"
CONF_NOTE: str = "xpath://div[@id='custdisplay']//th[text()='Conf Note']//following-sibling::td[contains(@class,'cfnote')]"
TIME_DISPLAY: str = "xpath://div[@id='custdisplay']//*[contains(@class,'time')]"
RUSH_COMMENT: str = "xpath://div[@id='custdisplay']//th[text()='Rush Comment']//following-sibling::td[@class='rushComment']"
VOID_COMMENT: str = "xpath://div[@id='custdisplay']//th[text()='Void Comment']//following-sibling::td[@class='voidComment']"
ESTIMATED_TIME: str = "xpath://div[@id='custdisplay']//th[text()='Est. Time']//following-sibling::td[@class='estimatedTime']"

