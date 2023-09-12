
PE_PAGE_TITLE: str = "xpath://h3[@id='editor-name' and normalize-space()='Printer Editor']"
PE_RESTAURANTS_DD: str = "xpath://app-restaurant-list//span[contains(@class,'dropdown-btn')]"
PE_RESTAURANTS_DD_SELECTED_ITEM: str = "xpath://app-restaurant-list//span[contains(@class,'dropdown-btn')]//*[@class='selected-item']"
PE_RESTAURANTS_DD_PLACEHOLDER: str = "xpath://span[contains(text(),'Enter Restaurant')]"
PE_RESTAURANT_SEARCH_BOX: str = "xpath://app-restaurant-list//li[@class='filter-textbox']/input"
PE_RESTAURANTS: str = "xpath://app-restaurant-list//ul[@class='item2']//div"
def PE_RESTAURANTS_DD_OPTION_TPL(text: str) -> str:
    return f"xpath://app-restaurant-list//div[normalize-space()='{text}']"