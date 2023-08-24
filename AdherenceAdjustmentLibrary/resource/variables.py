from datetime import datetime, timedelta

# Start Date
today = datetime.now()
two_weeks_ago = today - timedelta(weeks=2)
days_until_previous_monday = (two_weeks_ago.weekday() - 0) % 7
previous_monday = two_weeks_ago - timedelta(days=days_until_previous_monday)
EXP_FLTR_SDPLHDR = previous_monday.strftime('%Y-%m-%d')
EXP_FLTR_SDLBL: str = "Start Date:"

# End Date
current_datetime = datetime.now()
EXP_FLTR_EDPLHDR = current_datetime.strftime('%Y-%m-%d')
EXP_FLTR_EDLBL: str = "End Date:"


USERNAME: str = "acalimag"
PASSWORD: str = "kjt"

DISP_AGENT_NAME: str = "tqa4"
UDID: str = "271cf76b-cab5-4964-8e19-7ef10aa84f11"


EXP_HDR_ADADJLBL: str = "Adherence Adjustment"
EXP_HDR_USER: str = "${result['username']} - ${result['position']}"
EXP_URL: str = "https://qa.letsdochinese.com/KJTCore/resources/adherenceadjustment.html"



TEAMNAME: str = "Xrp"
EXP_DESC: str = "Test Team"
EXP_TLNAME: str = "Adam Warlock"
EXP_LOC: str = "DGT"
EXP_TYPE: str = "Operational"
EXP_ESTATUS: str = "True"
EXP_DSTATUS: str = "False"
EXT_LAST_UPD: str = "Aug 15, 2023 5:50 AM"
AGENT_NAME: str = "kleo4 test"
EXP_TLLBL: str = "TEAM LIST"
EXP_VULBL: str = "View/Update"

EXP_TBL_RTR_LBL: str = "Requested Time Range"
EXP_TBL_UNAME_LBL: str = "Username"
EXP_TBL_LOC_LBL: str = "Location"
EXP_TBL_TEAM_LBL: str = "Team"
EXP_TBL_STAT_LBL: str = "Status"
EXP_TBL_RVWR_LBL: str = "Reviewer"
EXP_TBL_RVWDAT_LBL: str = "Reviewed At"
EXP_TBL_CRTD_LBL: str = "Created"

EXP_RMNDR_LBL: str = "Reminder"
EXP_RMNDR_TXT: str = "Any changes related to the team assignment should only be done after 9AM-3AM (next day)." 

EXP_CNTLBL: str = "Create New Team"
IN_CNT_NAME: str = "Auto_Test_1"
IN_CNT_TD: str = "Auto_Test_1"
IN_CNT_TL: str = "Adam Warlock"
IN_CNT_LOC: str = "MNL"
IN_CNT_TYPE: str = "Non-Operational"
IN_CNT_STATUS: str = "Disabled"

ED_VU_NAME: str = "Xrp"
ED_VU_TD: str = "Test Team1"
ED_VU_TL: str = "Adam Warlock"
ED_VU_LOC: str = "MNL"
ED_VU_TYPE: str = "Operational"
ED_VU_STATUS: str = "Disabled"


EXP_ADS_HDR: str = "Adherence/Dispute Information"
EXP_ADS_FNAME_LBL: str = "Full Name:"
EXP_ADS_STAT_LBL: str = "Status:"
EXP_ADS_CTR_LBL: str = "Current Time Range:"
EXP_ADS_RTR_LBL: str = "Requested Time Range:"
EXP_ADS_WHRS_LBL: str = "Work Hours:"
EXP_ADS_RSN_LBL: str = "Reason:"
EXP_ADS_CRT_LBL: str = "Created At:"
EXP_ADS_LOC_LBL: str = "Location:"
EXP_ADS_TEAM_LBL: str = "Team:"
EXP_ADS_CACT_LBL: str = "Current Activity:"
EXP_ADS_RACT_LBL: str = "Requested Activity:"
EXP_ADS_PHRS_LBL: str = "Pay Hours:"
EXP_ADS_REVSEC_LBL: str = "Review Section"
EXP_ADS_CMNT_LBL: str = "Comment:"
EXP_ADS_INOTES_LBL: str = "Internal Notes:"
EXP_ADS_REVBY_LBL: str = "Reviewed By:"
EXP_ADS_REVAT_LBL: str = "Reviewed At:"
EXP_ADS_CNFRMAT_LBL: str = "Confirmed At:"
EXP_ADS_AUPSCHED_LBL: str = "Auto-update Schedule"
EXP_ADS_AUACT_LBL: str = "Auto-update Activity"
EXP_ADS_MANUP_LBL: str = "Manual Update"