
from robot.api.deco import library, keyword
import json
import requests
from RequestsLibrary.SessionKeywords import SessionKeywords
from requests import Response


class AddAgentTA:

    @keyword
    def add_agent_api(self, uid: str,  teamId: str):
        url = f"https://qa.letsdochinese.com/userconfigserver/admin/update/user/teams"
        headers = {
        'Authorization': "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhY2FsaW1hZyIsImlhdCI6MTY5MTI0OTE2NX0.Nh6uj9uSOZD6nqz_KQ9D13Lbbl24mQE7fO3e3uazOVg",
        'Content-Type': "application/json"
    }

        payload ={
                "uid": uid,
                "teamId": teamId
            }
        

        response = requests.put(url, headers=headers, data=json.dumps(payload))

        # return response

        if response.status_code == 200:
            return response.json()
        else:
            return None
    


        