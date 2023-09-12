from libraries.dashboard.ClientTechDashboardLibrary.dto.acknowledgemodaldetails import AcknowdledgeModalDetails
from libraries.dashboard.ClientTechDashboardLibrary.locators import acknowledgemodal, frame
from robot.api.deco import keyword
from autocore.bases import WebLibraryComponent

class AcknowledgeModalKeywords(WebLibraryComponent):
    
    @keyword(tags=("ClientTechDashBoardKeywords","PrinterPaneKeywords"))
    def take_action_on_acknowledge_modal(self, action: str = 'OK', _:AcknowdledgeModalDetails = None) -> AcknowdledgeModalDetails:
        self.web.select_frame(locator=frame.CLIENT_TECH_FRAME)
        try:
            self.web.wait_until_visible(locator=acknowledgemodal.HEADER)
            header = self.web.get_text(locator=acknowledgemodal.HEADER)
            self.web.wait_until_visible(locator=acknowledgemodal.BODY)
            body = self.web.get_text(locator=acknowledgemodal.BODY)
            details = AcknowdledgeModalDetails(header=header, body=body)
            
            action = action.strip().upper()
            if action == 'OK':
                self.web.click(locator=acknowledgemodal.OKAY_BTN)
                self.web.wait_until_not_visible(locator=acknowledgemodal.HEADER)
            elif action == 'CANCEL':
                self.web.click(locator=acknowledgemodal.CANCEL_BTN)
                self.web.wait_until_not_visible(locator=acknowledgemodal.HEADER)
            elif action == 'NO_ACTION':
                pass
            else:
                raise Exception(f"The action: {action} is not supported.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
        self.logger.debug_json(data=details)
        return details