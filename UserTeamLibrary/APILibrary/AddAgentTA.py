
from robot.api.deco import keyword
import json
import requests
from requests import Response

class AddAgentTA:

    @keyword
    def add_agent_api(self, uid: str, teamId: str):
        url = f"https://qa.letsdochinese.com/userconfigserver/admin/update/user/teams"
        headers = {
            'Authorization': "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhY2FsaW1hZyIsImlhdCI6MTY5MDUzOTAyOH0.STxpE7wfTbuvucPK5IV8Uzaxrx599Qlbidar1E2X9Dg",
            'Content-Type': "application/json"
        }

        payload = [
            {
                "uid": uid,
                "teamId": teamId
            }
        ]

        response = requests.put(url, headers=headers, json=payload)

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




# from robot.api.deco import library, keyword
# import json
# import requests
# from RequestsLibrary.SessionKeywords import SessionKeywords
# from requests import Response


# class AddAgentTA:

#     @keyword
#     def add_agent_api(self, uid: str,  teamId: str):
#         url = f"https://qa.letsdochinese.com/userconfigserver/admin/update/user/teams"
#         headers = {
#         'Authorization': "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhY2FsaW1hZyIsImlhdCI6MTY5MDUzOTAyOH0.STxpE7wfTbuvucPK5IV8Uzaxrx599Qlbidar1E2X9Dg",
#         'Content-Type': "application/json"
#     }

#         payload ={
#                 "uid": uid,
#                 "teamId": teamId
#             }

#         response = requests.put(url, headers=headers, data=json.dumps(payload))
        
#         # {
#         #         "uid": uid,
#         #         "teamId": teamId
#         #     }
        



#         # return response

#         if response.status_code == 200:
#             return response.json()
#         else:
#             print("Error response text:")
#             print(response.text)
#             return response.status_code
    
