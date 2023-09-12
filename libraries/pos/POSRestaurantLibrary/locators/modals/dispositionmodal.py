MODAL: str = "xpath://div[@id='dispositionModal']//*[contains(@class,'modal-dialog')]"
DISPOSITION_LABEL: str = "xpath://p[@class='dispositionLabel']"
HEADER: str = "xpath://div[@id='dispositionModal']//*[contains(@class,'modal-header')]"
ORDER_REMARK_AREA: str = "id:dispositionReason"
CONTINUE_BTN: str = "id:dispositionBtn"
CANCEL: str = "id:cancelDispositionBtn"
DISPOSITIONS: str = "xpath://div[@id='dispositionsContainer']/button"

# For interacting with each reason through 1 based index
DISPOSITIONS_INDEXED_TPL: str = "xpath:(//div[@id='dispositionsContainer']/button)[{0}]"
