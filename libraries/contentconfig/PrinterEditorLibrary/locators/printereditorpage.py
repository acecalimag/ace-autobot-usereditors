ALL_DISPLAYED_PIDS: str = "xpath://input[@formcontrolname='pid']"
COLUMN_NAMES: str = "xpath://thead//th"
SAVE_BTN: str = "xpath://button[@type='submit']"
ADD_PRINTER: str = "xpath://button[normalize-space()='Add Printer']"
NUCLESS_TOGGLE: str = "id:nuclessToggle"
NUCLESS_DETAILS_LABEL: str = "xpath://h5[text()='NUCless Details']"

# index parameter is the index of the printer
def PID(index: str) -> str:
    return f"xpath:(//input[@formcontrolname='pid'])[{index}]"

def PID_ERR_MSG(index: str) -> str:
    return f"xpath:(//input[@formcontrolname='pid']//following-sibling::div[@class='invalid-feedback'])[{index}]"

def ACTIVE(index: str) -> str:
    return f"xpath:(//input[@formcontrolname='active' and @type='checkbox'])[{index}]"

def NAME(index: str) -> str:
    return f"xpath:(//input[@formcontrolname='name'])[{index}]"

def NAME_ERR_MSG(index: str) -> str:
    return f"xpath:(//input[@formcontrolname='name']//following-sibling::div[@class='invalid-feedback'])[{index}]"

def MASK(index: str) -> str:
    return f"xpath:(//input[@formcontrolname='mask'])[{index}]"

def MASK_ERR_MSG(index: str) -> str:
    return f"xpath:(//input[@formcontrolname='mask']//following-sibling::div[@class='invalid-feedback'])[{index}]"

def MASK_RULE_DROPDOWN(index: str) -> str: 
    return f"xpath:(//ng-multiselect-dropdown[@formcontrolname='maskRule']//span[@class='dropdown-btn'])[{index}]"

def SELECTED_MASK_RULE(index: str) -> str:
    return f"xpath:(//ng-multiselect-dropdown[@formcontrolname='maskRule']//span[contains(@class,'selected-item')])[{index}]"

def MASK_RULE_OPTIONS(index: str) -> str:
    return f"xpath:(//ng-multiselect-dropdown[@formcontrolname='maskRule'])[{index}]//div[@class='dropdown-list']//ul[@class='item2']/li/div"

def MASK_RULE_OPTION(index: str, mask_rule: str) -> str:
    return f"xpath:(//ng-multiselect-dropdown[@formcontrolname='maskRule'])[{index}]//div[text()='{mask_rule}']"

def MASK_RULE_ERR_MSG(index: str) -> str:
    return f"xpath:(//ng-multiselect-dropdown[@formcontrolname='maskRule'])[{index}]//following-sibling::div[@class='custom-invalid-feedback']"

def ORDER_RECEIPT_DROPDOWN(index: str) -> str:
    return f"xpath:(//ng-multiselect-dropdown[@formcontrolname='template']//span[@class='dropdown-btn'])[{index}]"

def ORDER_RECEIPT_ERR_MSG(index: str) -> str:
    return f"xpath:(//ng-multiselect-dropdown[@formcontrolname='template'])[{index}]//following-sibling::div[@class='custom-invalid-feedback']"

def SELECTED_ORDER_RECEIPT(index: str) -> str:
    return f"xpath:(//ng-multiselect-dropdown[@formcontrolname='template']//span[contains(@class,'selected-item')])[{index}]"

def ORDER_RECEIPT_OPTIONS(index: str) -> str:
    return f"xpath:(//ng-multiselect-dropdown[@formcontrolname='template'])[{index}]//div[@class='dropdown-list']//ul[@class='item2']//div"

def ORDER_RECEIPT_OPTION(index: str, template: str) -> str:
    return f"xpath:(//ng-multiselect-dropdown[@formcontrolname='template'])[{index}]//div[@class='dropdown-list']//div[text()=normalize-space('{template}')]"

def CUST_INFO_CHECKBOX(index: str) -> str:
    return f"xpath:(//input[@formcontrolname='custInfoActive'])[{index}]"

def CUST_INFO_FONT_SIZE_SELECT(index: str) -> str:
    return f"xpath:(//select[@formcontrolname='fontSizeCustInfo'])[{index}]"

def ENGLISH_TEXT_CHECKBOX(index: str) -> str: 
    return f"xpath:(//input[@formcontrolname='enActive'])[{index}]"

def ENGLISH_TEXT_FONT_SIZE_SELECT(index: str) -> str:
    return f"xpath:(//select[@id='fontSizeEn'])[{index}]"

def ENGLISH_TEXT_BOLD_TOGGLE(index: str) -> str:
    return f"xpath:(//input[@id='boldEnToggle'])[{index}]"

def CHINESE_TEXT_CHECKBOX(index: str) -> str:
    return f"xpath:(//input[@formcontrolname='cnActive'])[{index}]"

def CHINESE_TEXT_FONT_SIZE_SELECT(index: str) -> str:
    return f"xpath:(//select[@id='fontSizeCn'])[{index}]"

def CHINESE_TEXT_BOLD_TOGGLE(index: str) -> str:
    return f"xpath:(//input[@id='boldCnToggle'])[{index}]"

def SPACING_SELECT(index: str) -> str:
    return f"xpath:(//select[@id='spacingSizeSelector'])[{index}]"

def ALWAYS_PRINT_QTY_CHECKBOX(index: str) -> str:
    return f"xpath:(//input[@formcontrolname='alwaysPrintQty'])[{index}]"

def MODIFIED_DISH_ONLY(index: str) -> str:
    return f"xpath:(//input[@formcontrolname='modifiedDishesOnly'])[{index}]"

def LINE_SELECT(index: str) -> str:
    return f"xpath:(//select[@id='lineSelector'])[{index}]"

def PREVIEW(index: str) -> str:
    return f"xpath:(//i[contains(@class,'fa-eye text-dark')])[{index}]"

def CC_TEMPLATE_DROPDOWN(index: str) -> str:
    return f"xpath:(//ng-multiselect-dropdown[@formcontrolname='ccTemplate']//span[@class='dropdown-btn'])[{index}]"

def SELECTED_CC_TEMPLATE(index: str) -> str:
    return f"xpath:(//ng-multiselect-dropdown[@formcontrolname='ccTemplate']//span[contains(@class,'selected-item')])[{index}]"

def CC_TEMPLATE_OPTIONS(index: str) -> str:
    return f"xpath:(//ng-multiselect-dropdown[@formcontrolname='ccTemplate'])[{index}]//div[@class='dropdown-list']//ul[@class='item2']//div"

def CC_TEMPLATE_OPTION(index: str, cc_template: str) -> str:
    return f"xpath:(//ng-multiselect-dropdown[@formcontrolname='ccTemplate'])[{index}]//div[@class='dropdown-list']//div[text()=normalize-space('{cc_template}')]"

def CC_VOID_RECEIPT_CHECKBOX(index: str) -> str:
    return f"xpath:(//input[@formcontrolname='creditCardVoid'])[{index}]"

def LAST_UPDATED(index: str) -> str:
    return f"xpath:(//input[@formcontrolname='creditCardVoid'])[{index}]//ancestor::td//following-sibling::td[1]"

def LAST_UPDATED_BY(index: str) -> str:
    return f"xpath:(//input[@formcontrolname='creditCardVoid'])[{index}]//ancestor::td//following-sibling::td[2]"

def NUCLESS_HOST(index: str) -> str:
    return f"xpath:(//b[normalize-space()='Host']//following-sibling::input)[{index}]"

def NUCLESS_HOST_ERR_MSG(index: str) -> str:
    return f"xpath:(//b[normalize-space()='Host']//following-sibling::div[@class='invalid-feedback'])[{index}]"

def NUCLESS_PRINTER_PORT(index: str) -> str:
    return f"xpath:(//b[normalize-space()='Printer Port']//following-sibling::input)[{index}]"

def NUCLESS_PRINTER_PORT_ERR_MSG(index: str) -> str:
    return f"(//b[normalize-space()='Printer Port']//following-sibling::div[@class='invalid-feedback'])[{index}]"

def NUCLESS_STATUS_PORT(index: str) -> str:
    return f"xpath:(//b[normalize-space()='Status Port']//following-sibling::input)[{index}]"

def NUCLESS_STATUS_PORT_ERR_MSG(index: str) -> str:
    return f"(//b[normalize-space()='Status Port']//following-sibling::div[@class='invalid-feedback'])[{index}]"

def SELECTED_MODEL(index: str) -> str:
    return f"xpath:(//b[normalize-space()='Model']//following-sibling::*[@formcontrolname='model']//span[@class='selected-item'])[{index}]"

def MODEL_OPTIONS(index: str) -> str:
    return f"xpath:(//*[@formcontrolname='model'])[{index}]//ul[@class='item2']//li/div"

def MODEL_OPTION(index: str, model: str) -> str:
    return f"xpath:(//*[@formcontrolname='model'])[{index}]//ul[@class='item2']//li/div[normalize-space()='{model}']"

def MODEL_DROPDOWN(index: str) -> str:
    return f"xpath:(//*[@formcontrolname='model'])[{index}]//span[@class='dropdown-btn']"

def MODEL_ERR_MSG(index: str) -> str:
    return f"xpath:(//b[normalize-space()='Model']//following-sibling::div[@class='custom-invalid-feedback'])[{index}]"

def NUCLESS_DETAILS_LABELS(index: str) -> str:
    return f"(//div[contains(@class,'nucless-config-wrapper')])[{index}]/div/b"