
from autocore.bases import APILibraryComponent
from robot.api.deco import keyword
import json

# import requests
# from requests import Response

class CreateUserTeam(APILibraryComponent):

    @keyword
    def create_user_team_api(self, name: str, desc: str, teamlead: str, loc: str, type: str, status: str):
        url = f"https://qa.letsdochinese.com/userconfigserver/admin/userteam"
        headers = {
            'Authorization': "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhY2FsaW1hZyIsImlhdCI6MTY5MzAxMzExNn0.us65pijGY2PDlB1G1Z8XleUxeQ7GM0NuvqL-Qt1O-dE",
            'Content-Type': "application/json"
        }

        payload = {
            "utid": None,
            "name": name,
            "description": desc,
            "teamlead": teamlead,
            "location": loc,
            "type": type,
            "status": status
        }

        response = self.api.post(url, headers=headers, json=payload)

        if response.text:  # Check if response content is not empty
            try:
                response_json = response.json()
                return response_json
            except json.JSONDecodeError as e:
                print("Error decoding JSON:", e)
        else:
            print("Empty response content")
        
        # return None
        return response.status_code

