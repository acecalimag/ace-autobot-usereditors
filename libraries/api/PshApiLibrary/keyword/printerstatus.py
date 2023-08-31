from robot.api.deco import keyword
from requests import Response
from autocore.bases import APILibraryComponent


class PrinterStatus(APILibraryComponent):

    @keyword(tags=("PrinterStatusKeywords",))
    def request_to_update_printer_status(self, rid: str, pid: str, status: str, status_report: str = '') -> Response:
        return self.api.put(
            url=f"{self.base_url}/psh/papi/restaurant/{rid}/printer/{pid}/status",
            headers={
                'Content-Type':'application/json'
            },
            json={
                'status': status,
                'statusReport': status_report
            }
        )