TEAMLIST: str = "//*[@id='teamList']"

# TNAME: str = "//h3[@class='text-capitalize']//span[@class='teamName']"
TNAME: str = "//span[@id='teamName']"
TLEAD: str = "//span[@id='teamLead']"
TLOC: str = "//span[@id='teamLocation']"

TNAMELBL: str = "//span[normalize-space()='Team Name:']"
TLEADLBL: str = "//span[normalize-space()='Team Lead:']"
TLOCLBL: str = "//span[normalize-space()='Team Location:']"

FREEAGENTSLBL: str = "//h5[normalize-space()='Free Agents']"
TEAMROSTERLBL: str = "//div[2]/h5"

FREEAGENTSFLTR: str = "//input[@id='filterFreeAgents']"
TEAMROSTERFLTR: str = "//input[@id='filterRosteredAgents']"

MOVEALLBTN: str = "//button[@id='freeAgentMoveAll']"
MOVESLCBTN: str = "//button[@id='freeAgentMoveSelected']"

REMOVEALLBTN: str = "//button[@id='rosteredAgentRemoveAll']"
REMOVESLCBTN: str = "//button[@id='rosteredAgentRemoveSelected']"

FREEAGENTSLIST: str = "//select[@id='freeAgentsList']"
TEAMROSTERLIST: str = "//select[@id='rosteredAgentsList']"

SAVEBTN: str = "//button[@id='saveAgents']"
CANCELBTN: str = "//button[@id='cancelAgents']"

ALERT: str = "//div[@role='alert']"
ALERTTEXT: str = "//div[@role='alert']//li"
INFO_CIRCLE: str = "//i[@class='fa fa-info-circle']"
RMNDR: str = "//div[@role='alert']//strong"
DISMISS_ALERT_BTN: str = "//button[@aria-label='Close']"