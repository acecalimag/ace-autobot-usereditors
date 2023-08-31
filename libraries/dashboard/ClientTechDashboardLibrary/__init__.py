from libraries.dashboard.ClientTechDashboardLibrary.keywords.acknowledgemodal import AcknowledgeModalKeywords
from libraries.dashboard.ClientTechDashboardLibrary.keywords.failedpane import FailedPaneKeywords
from libraries.dashboard.ClientTechDashboardLibrary.keywords.portpane import PortPaneKeywords
from libraries.dashboard.ClientTechDashboardLibrary.keywords.printerpane import PrinterPaneKeywords
from libraries.dashboard.ClientTechDashboardLibrary.locators import failedpane, frame, portpane, printerpane
from libraries.dashboard.DashboardCommon import DashboardCommon
from robot.api.deco import library, keyword

from libraries.dashboard.config import DASHBOARD_GLOBAL_TIMEOUT

@library(scope='GLOBAL')
class ClientTechDashboardLibrary(DashboardCommon):
    def __init__(self):
        DashboardCommon.__init__(self)
        self.__wa = self.create_web_action(timeout=DASHBOARD_GLOBAL_TIMEOUT)
        library_components = [
            AcknowledgeModalKeywords(library=self, timeout=DASHBOARD_GLOBAL_TIMEOUT),
            FailedPaneKeywords(library=self, timeout=DASHBOARD_GLOBAL_TIMEOUT),
            PrinterPaneKeywords(library=self, timeout=DASHBOARD_GLOBAL_TIMEOUT),
            PortPaneKeywords(library=self, timeout=DASHBOARD_GLOBAL_TIMEOUT)
        ]
        self.add_library_components(library_components=library_components)
        
    @keyword(tags=("ClientTechDashBoardKeywords",))
    def wait_until_client_tech_dashboard_is_visible(self):
        self.__wa.select_frame(locator=frame.CLIENT_TECH_FRAME)
        try:
            self.__wa.wait_until_visible(locator=failedpane.FAILED_PANE)
            self.__wa.wait_until_visible(locator=portpane.PORT_PANE)
            self.__wa.wait_until_visible(locator=printerpane.PRINTER_PANE)
        except Exception as e:
            raise e
        finally:
            self.__wa.unselect_frame()
            
        
        