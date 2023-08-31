RESTAURANTS: str = "xpath://ul[@class='list-inline']//li"
USERNAME: str = "id:username"

ACTIVE_RESTAURANTS: str = "xpath://td[contains(.,'Active:')]//span[@id='restaurantstatus-count-open']"
ONBOARDING_RESTAURANTS: str = "xpath://td[contains(.,'Onboarding:')]//span[@id='restaurantstatus-count-new']"
OFFBOARDING_RESTAURANTS: str = "xpath://td[contains(.,'Offboarding:')]//span[@id='restaurantstatus-count-closed']"

MY_SCHEDULE_BTN: str = "xpath://button[@id='scheduleBtn' and normalize-space()='MySchedule']"
MISTAKE_AND_COACHING_BTN: str = "xpath://button[@id='mistakeBtn' and normalize-space()='Mistake &Coaching']"
NEWS_BTN: str = "xpath://button[@id='msgBtn' and contains(.,'News')]"
CALL_HISTORY_BTN: str = "xpath://button[@id='callHistoryBtn' and normalize-space()='CallHistory']"
STATUS_BTN: str = "id:statusBtn"
OTHER_STATUS_OPTIONS: str = "xpath://div[@id='statusGroup']//ul//li[not(contains(@class,'divider'))]"

CALL_COUNT: str = "xpath://th[text()='Inbound Contacts']//parent::tr//following-sibling::tr//td[@id='callcount']"
AVE_DURATION_TIME: str = "xpath://th[text()='ATT']//parent::tr//following-sibling::tr//td[@id='avgdurationtime']"
AVE_WRAP_UP_TIME: str = "xpath://th[text()='AWT']//parent::tr//following-sibling::tr//td[@id='avgwrapuptime']"
TOTAL_TIME: str = "xpath=//th[text()='AHT']//parent::tr//following-sibling::tr//td[@id='totaltime']"
