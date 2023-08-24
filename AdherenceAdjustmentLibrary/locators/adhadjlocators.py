ADADJLBL: str = "//a[normalize-space()='Adherence Adjustment']"
HDR_USER: str = "//span[@id='username']"

DSPT_LIST: str = "//div[@id='dispute-list-tbl_wrapper']"


CAL_SDPREV: str = "//div[@id='startDate_root']//div[@title='Previous month']"
CAL_SDNEXT: str = "//div[@id='startDate_root']//div[@title='Next month']"

CAL_EDPREV: str = "//div[@id='endDate_root']//div[@title='Previous month']"
CAL_EDNEXT: str = "//div[@id='endDate_root']//div[@title='Next month']"

CAL_SD_PICKER: str = "//table[@id='startDate_table']"
CAL_ED_PICKER: str = "//table[@id='endDate_table']"

CAL_SDTODAY: str = "//div[@id='startDate_root']//button[@type='button'][normalize-space()='Today']"
CAL_EDTODAY: str = "//div[@id='endDate_root']//button[@type='button'][normalize-space()='Today']"

DIS_NEXTBTN: str = "//li[@id='dispute-list-tbl_next']"
DIS_PREVBTN: str = "//li[@id='dispute-list-tbl_previous']"

TNAME: str = "//input[@id='name']"
TDESC: str = "//textarea[@id='description']"
UPDTIME: str = "//span[@id='updatetime']"

VIEW_UPDATE_LBL: str = "//h5[@id='formTitle']"
TEAM_LIST_LBL: str = "//h5[normalize-space()='Team List']"

TBL_RTR_LBL: str = "//th[@class='sorting_asc'][normalize-space()='Requested Time Range']"
TBL_UNAME_LBL: str = "//th[@class='sorting'][normalize-space()='Username']"
TBL_LOC_LBL: str = "//th[@class='sorting'][normalize-space()='Location']"
TBL_TEAM_LBL: str = "//th[@class='sorting'][normalize-space()='Team']"
TBL_STAT_LBL: str = "//th[@class='sorting'][normalize-space()='Status']"
TBL_RVWR_LBL: str = "//th[@class='sorting'][normalize-space()='Reviewer']"
TBL_RVWDAT_LBL: str = "//th[@class='sorting'][normalize-space()='Reviewed At']"
TBL_CRTD_LBL: str = "//th[@class='sorting'][normalize-space()='Created']"

FLTR_SD_LBL: str = "//label[normalize-space()='Start Date:']"
FLTR_SD_INP: str = "//input[@id='startDate']"
FLTR_SD_PLHDR: str = "//div[@class='picker__day picker__day--infocus picker__day--selected picker__day--highlighted']"


FLTR_SD_PLHDR: str = "(//div[@aria-selected='true'])[1]"
FLTR_ED_PLHDR: str = "(//div[@aria-selected='true'])[2]"

FLTR_ED_LBL: str = "//label[normalize-space()='End Date:']"
FLTR_ED_INP: str = "//input[@id='endDate']"



FLTR_LOC_DRPDWN: str = "//button[@data-id='location-select']"

FLTR_STAT_DRPDWN: str = "//button[@data-id='status-select']"
FLTR_STAT_SALL: str = "//div[@class='dropdown-menu show']//button[@type='button'][normalize-space()='Select All']"
def FLTR_STAT_PLHDR(status: str):
    return f"//button[@data-id='status-select' and @title='{status}']"





FLTR_GO_BTN: str = "//button[@id='display-requests-btn']"
FLTR_EXPRT_BTN: str = "//button[@id='export-to-xls']"


SAVEBTN: str = "//button[@id='save']"
CANCELBTN: str = "//button[@id='cancel']"

ALERT: str = "//div[@role='alert']"
ALERTTEXT: str = "//div[@role='alert']//li"
INFO_CIRCLE: str = "//i[@class='fa fa-info-circle']"
RMNDR: str = "//div[@role='alert']//strong"
DISMISS_ALERT_BTN: str = "//button[@aria-label='Close']"



FLTR_USERS_DRPDWN: str = "//button[@data-id='user-select']"
# "//button[@data-id='user-select']"
FLTR_USERS_SRCH: str = "//div[@class='dropdown-menu show']//input[@aria-label='Search']"
FLTR_USERS_RSLT: str = "//a[@class='dropdown-item active']"
def FLTR_USERS_PLHDR(user: str):
    return f"//button[@data-id='user-select' and @title='{user}']"


FLTR_LOC_DRPDWN: str = "//button[@data-id='location-select']"
def FLTR_LOC_PLHDR(loc: str):
    return f"//button[@data-id='location-select' and @title='{loc}']"


FLTR_TEAM_DRPDWN: str = "//button[@data-id='team-select']"
FLTR_TEAM_SRCH: str= "//div[@class='dropdown-menu show']//input[@aria-label='Search']"
FLTR_TEAM_RSLT: str= "//a[@class='dropdown-item active']"
def FLTR_TEAM_PLHDR(team: str):
    return f"//button[@data-id='team-select' and @title='{team}']"



FLTR_POST_DRPDWN: str = "//button[@data-id='position-select']"
def POST_LOCATOR(position: str):
    return f"xpath://div[@aria-expanded='true']//span[@class='text'][normalize-space()='{position}']"

def FLTR_POST_PLHDR(position: str):
    return f"//button[@data-id='position-select' and @title='{position}']"


# sd_locator = f"//div[@aria-label='{start_date}']"
def SD_LOCATOR(start_date: str):
    return f"xpath://div[@aria-label='{start_date}']"

# ed_locator = f"//div[@aria-label='{end_date}']"
def ED_LOCATOR(end_date: str):
    return f"xpath://div[@aria-label='{end_date}']"



TLEAD: str = "//select[@id='teamlead']"
def TLEAD_LOC(lead: str):
    return f"xpath://option[text()='{lead}']"


TLOC: str = "//select[@id='location']"
def TLOC_LOC(loc: str):
    return f"xpath://option[text()='{loc}']"


TTYPE: str = "//select[@id='type']"
# TTYPE: str = "//option[@value='{}']"
def TTYPE_LOC(type: str):
    return f"xpath://option[@value='{type}']"


TSTAT_ENB: str = "//input[@id='enabled']"
TSTAT_DISB: str = "//input[@id='disabled']"
def TSTATUS_LOC(status: str):
    return f"xpath://input[@id='{status}']"


ADS_HDR: str = "//h4[normalize-space()='Adherence/Dispute Information']"
ADS_FNAME_LBL: str = "//label[normalize-space()='Full Name:']"
ADS_STAT_LBL: str = "//label[normalize-space()='Status:']"
ADS_CTR_LBL: str = "//label[normalize-space()='Current Time Range:']"
ADS_RTR_LBL: str = "//label[normalize-space()='Requested Time Range:']"
ADS_WHRS_LBL: str = "//label[normalize-space()='Work Hours:']"
ADS_RSN_LBL: str = "//label[normalize-space()='Reason:']"
ADS_CRT_LBL: str = "//label[normalize-space()='Created At:']"
ADS_LOC_LBL: str = "//label[normalize-space()='Location:']"
ADS_TEAM_LBL: str = "//label[normalize-space()='Team:']"
ADS_CACT_LBL: str = "//label[normalize-space()='Current Activity:']"
ADS_RACT_LBL: str = "//label[normalize-space()='Requested Activity:']"
ADS_PHRS_LBL: str = "//label[normalize-space()='Pay Hours:']"
ADS_REVSEC_LBL: str = "//div[@class='skt-border-bottom mt-30 skt-form-title col-md-12']"
ADS_CMNT_LBL: str = "//label[normalize-space()='Comment:']"
ADS_INOTES_LBL: str = "//label[normalize-space()='Internal Notes:']"
ADS_REVBY_LBL: str = "//label[normalize-space()='Reviewed By:']"
ADS_REVAT_LBL: str = "//label[normalize-space()='Reviewed At:']"
ADS_CNFRMAT_LBL: str = "//label[normalize-space()='Confirmed At:']"
ADS_AUPSCHED_LBL: str = "//label[normalize-space()='Auto-update Schedule']"
ADS_AUACT_LBL: str = "//label[normalize-space()='Auto-update Activity']"
ADS_MANUP_LBL: str = "//label[normalize-space()='Manual Update']"
ADS_AUPSCHED_RBTN: str = "//input[@id='schedule-auto-update']"
ADS_AUACT_RBTN: str = "//input[@id='activity-auto-update']"
ADS_MANUP_RBTN: str = "//input[@id='manual-update']"
ADS_REJ_BTN: str = "//button[normalize-space()='Reject']"
ADS_SAVE_BTN: str = "//button[@id='dispute-save-btn']"
ADS_APRV_BTN: str = "//button[normalize-space()='Approve']"


def radio_button_check(self, locator):
    radio_button = self.__ctx.find_element(*locator)
    return radio_button.is_enabled()