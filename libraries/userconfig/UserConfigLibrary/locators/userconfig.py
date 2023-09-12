USERCONFIG_ELEMENTS = {
    'Status Dropdown': '//button[@data-id="activeLevelList"]',
    'Location Dropdown': '//button[@data-id="userLocation"]',
    'Team Dropdown': '//button[@data-id="userTeam"]',
    'Position Dropdown': '//button[@data-id="userPosition"]',
    'Agent Dropdown': '//button[@data-id="activeAgentList"]',
    'Start Date': '//input[@id="startDate"]',
    'Date Selector': '//span[@title="Select a Date"]',
    'Clear Date': '//span[@title="Clear"]',
    'Go': '//button[@id="go"]',
    'Download': '//img[@alt="Download Icon"]',
    'User Config Table': '//div[@id="maindiv"]',
    'Save': '//button[@id="save"]'
}
AGENT_SEARCH:str = "//div[@class='dropdown-menu show']//input[@aria-label='Search']"

def AGENT_SEARCH_RESULT(agent: str):
    return f"//span[@class='text' and text()='{agent}']"

def NEW_LOCATION(location: str):
    return f"//td[normalize-space()='{location}']"

AGENT_DESELECT_ALL:str = "//button[normalize-space()='Deselect All']"
USER_CONFIG_ALERT: str = "//div[@role='alert']"
AGENT_LOCATION_ARROW: str = "(//div[@class='htAutocompleteArrow'][contains(text(),'▼')])[2]"
AGENT_LOCATION_CELL: str = "//tbody/tr[1]/td[5]"

USERNAME_HEADER: str = "(//span[@id='header-username'])[4]"

USERNAME_ONE: str = "//body[1]/div[1]/div[1]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]"
USERNAME_TWO: str = "//body[1]/div[1]/div[1]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]"
USERNAME_THREE: str = "//body[1]/div[1]/div[1]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]"
FIRST_LOCATION: str = "//tbody/tr[1]/td[5]"
SAVED_TOAST_MESSAGE: str = "//span[@data-notify='message' and contains(text(), 'Saved')]"
