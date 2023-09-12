from requests import Response
from robot.api.deco import keyword

from autocore.bases import APILibraryComponent


class ContentConfigToken(APILibraryComponent):


    @keyword(tags=("TokenKeywords", "PostRequest"))
    def request_for_a_token(self, username: str, password: str) -> Response:
        return self.api.post(
            url=f"{self.base_url}/contentconfigserver/token",
            files=[],
            data={
                "username": username,
                "password": password
            }
        )

    @keyword(tags=("TokenKeywords", "PostRequest"))
    def request_for_a_token_and_extract_jwt(self, username: str, password: str) -> str:
        response = self.request_for_a_token(
            username=username, password=password)
        
        self.api.status_code_should_be(response=response, exp=200)
        return self.api.get_value_of(response=response, json_path='jwt')

