USERTEAMS_ELEMENTS = {
    'Create Team': 'id:createTeam',
    'Team List Label': '//h5[normalize-space()="Team List"]',
    'Column Name': '//th[contains(@aria-label, "Name")]',
    'Column Team Lead': '//th[contains(@aria-label, "Team Lead")]',
    'Column Location': '//th[contains(@aria-label, "Location")]',
    'Column Type': '//th[contains(@aria-label, "Type")]',
    'Column Status': '//th[contains(@aria-label, "Status")]',
    'Column Last Updated': '//th[contains(@aria-label, "Last Updated")]',
    'Create New Team': 'id:formTitle',
    'Name': '//label[contains(@for, "name")]',
    'Name Input': 'id:name',
    'Description': '//label[contains(@for, "description")]',
    'Description Input': '//textarea[@id="description"]',
    'Team Lead': '//label[contains(@for, "teamlead")]',
    'Team Lead Select': '//select[@id="teamlead"]',
    'Location': '//label[contains(@for, "location")]',
    'Location Select': '//select[@id="location"]',
    'Type': '//label[contains(@for, "type")]',
    'Type Select': '//select[@id="type"]',
    'Status': '//label[contains(text(),"Status")]',
    'Status Enabled': '//input[@id="enabled"]',
    'Status Disabled': '//input[@id="disabled"]',
    'Last Updated': '//label[normalize-space()="Last Updated"]',
    'Update Span': '//span[@id="updatetime"]',
    'Create': 'id:create',
    'Create': 'id:cancel',
    'Previous':'//li[@id="teams_previous"]',
    'Next':'//li[@id="teams_next"]',
    'Save':'id:save',
    'Cancel':'id:cancel'
}

FIRST_TEAM: str = "(//tbody/tr/th)[1]"

def TEAM(team: str):
    return f"//th[contains(text(),'{team}')]"

def TEAM_TYPE(type: str):
    return f"//option[@value='{type}']"

TEAM_NAME: str = "//input[@id='name']"
