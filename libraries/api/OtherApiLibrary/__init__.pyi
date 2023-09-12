from requests import Response
from autocore.bases import APILibraryBase


class OtherApiLibrary(APILibraryBase):
    
    # Method signatures below are from libraries.api.OtherApiLibrary.keywords.openvoxstatus.py
    def request_to_update_restaurant_open_vox_status(self, rid: str, alarm: str, context: str = 'fxo-1', channel_id: str = "1") -> Response:...