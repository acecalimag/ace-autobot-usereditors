from requests import Response
from robot.api.deco import keyword
from autocore.bases import APILibraryComponent

from autocore.coreutils import get_est_timestamp_as_list


class OpenVoxStatus(APILibraryComponent):

    @keyword
    def request_to_update_restaurant_open_vox_status(self, rid: str, alarm: str, context: str = 'fxo-1', channel_id: str = "1") -> Response:
        return self.api.put(
            url=f"{self.base_url}/fpm/openvox/check/and/update/status",
            json={
                "rid": rid,
                "context": context,
                "channelId": int(channel_id),
                "alarm": alarm,
                "time": get_est_timestamp_as_list()
            }
        )
