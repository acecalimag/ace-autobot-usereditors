
from requests import Response
from autocore.bases import APILibraryBase


class PshApiLibrary(APILibraryBase):
    
    # Method signatures below are from libraries.api.PshApiLibrary.keywords.printerstatus.py
    def request_to_update_printer_status(self, rid: str, pid: str, status: str, status_report: str = '') -> Response:...