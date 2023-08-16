TEAMLIST: str = "//table[@id='teams']"
NEXTBTN: str = "//a[normalize-space()='Next']"

TNAME: str = "//input[@id='name']"
TDESC: str = "//textarea[@id='description']"

TSTAT_ENB: str = "//input[@id='enabled']"
TSTAT_DISB: str = "//input[@id='disabled']"
UPDTIME: str = "//span[@id='updatetime']"

VIEW_UPDATE_LBL: str = "//h5[@id='formTitle']"
TEAM_LIST_LBL: str = "//h5[normalize-space()='Team List']"

TBL_NAME_LBL: str = "//th[contains(text(),'Name')]"
TBL_TLEAD_LBL: str = "//th[contains(text(),'Team Lead')]"
TBL_TLOC_LBL: str = "//th[contains(text(),'Location')]"
TBL_TTYPE_LBL: str = "//th[contains(text(),'Type')]"
TBL_TSTAT_LBL: str = "//th[contains(text(),'Status')]"
TBL_TLUPD_LBL: str = "//th[contains(text(),'Last Updated')]"

VU_NAMELBL: str = "//label[@for='name']"
VU_TDLBL: str = "//label[normalize-space()='Description']"
VU_TLLBL: str = "//label[normalize-space()='Team Lead']"
VU_LOCLBL: str = "//label[@for='location']"
VU_TYPELBL: str = "//label[@for='type']"
VU_STATUSLBL: str = "//label[normalize-space()='Status']"
VU_LSTUPDLBL: str = "//label[normalize-space()='Last Updated']"

SAVEBTN: str = "//button[@id='save']"
CANCELBTN: str = "//button[@id='cancel']"

ALERT: str = "//div[@role='alert']"
ALERTTEXT: str = "//div[@role='alert']//li"
INFO_CIRCLE: str = "//i[@class='fa fa-info-circle']"
RMNDR: str = "//div[@role='alert']//strong"
DISMISS_ALERT_BTN: str = "//button[@aria-label='Close']"


CR_TEAM_BTN: str = "//button[@id='createTeam']"



# TLEAD: str = "//select[@id='teamlead']"
def TLEAD_LOC(lead: str):
    return f"xpath://option[text()='{lead}']"


# TLOC: str = "//select[@id='location']"
def TLOC_LOC(loc: str):
    return f"xpath://option[text()='{loc}']"


# TTYPE: str = "//select[@id='type']"
# TTYPE: str = "//option[@value='{}']"
def TTYPE_LOC(type: str):
    return f"xpath://option[@value='{type}']"
