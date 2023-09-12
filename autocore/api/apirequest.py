from typing import  Any
from jsonpath_ng.ext import parse
from RequestsLibrary.SessionKeywords import SessionKeywords
from requests import Response

from autocore.AssertsLibrary import assert_equal, assert_that_list_does_not_contain, assert_that_list_has_item

class APIRequests:
    
    def post(self, url, data=None, json=None,
             expected_status=None, msg=None, **kwargs) -> Response:
        return SessionKeywords().session_less_post(url=url, data=data, json=json, expected_status=expected_status, msg=msg, **kwargs)

    def get(self, url, params=None,
            expected_status=None, msg=None, **kwargs) -> Response:
        return SessionKeywords().session_less_get(url=url, params=params, expected_status=expected_status, msg=msg, **kwargs)

    def put(self, url, data=None, json=None,
                         expected_status=None, msg=None, **kwargs) -> Response:
        return SessionKeywords().session_less_put(url=url, data=data, json=json, expected_status=expected_status, msg=msg, **kwargs)
    
    def patch(self, url, data=None, json=None,
                           expected_status=None, msg=None, **kwargs):
        return SessionKeywords().session_less_patch(url=url, data=data, json=json, expected_status=expected_status, msg=msg, **kwargs)

class APIValidations:
    
    def status_code_should_be(self, response: Response, exp: int):
        act = response.status_code
        assert_equal(actual=act, exp=exp, e_msg=f"Expecting status code to be {exp} but got {act}")

    def get_header_value(self, response: Response, key: str):
        return response.headers[key]

    def header_value_should_be(self, response: Response, key: str, exp: str):
        act = response.headers[key]
        assert_equal(actual=act, exp=exp, e_msg=f"Expecting value of header {key} to be {exp} but got {act}")

    def get_value_of(self, response: Response, json_path: str) -> Any:
        result = self.__execute(response=response, query=json_path)
    
        if len(result) == 0:
            raise Exception(f"No value found in the response body using json path: {json_path}\nResponse:\n{str(response.json())}")

        return result[0]

    def value_of_should_be(self, response: Response, json_path: str, exp_value: Any, msg: str = None):
        act_value = self.get_value_of(response=response, json_path=json_path)
        
        if msg is None:
            msg = f"Expecting  value of {json_path} to be {exp_value} but got {act_value}."
            
        assert_equal(actual=act_value, exp=exp_value, e_msg=msg)

    def list_of_should_contain(self, response: Response, json_path: str, exp_value: Any, msg: str = None):
        act_value = self.get_value_of(response=response, json_path=json_path)
        
        if msg is None:
            msg = f"Jsonpath: {json_path}. Expecting list of {act_value} to contain {exp_value}."

        assert_that_list_has_item(lst=act_value, content=exp_value, e_msg=msg)

    def list_of_should_not_contain(self, respnse: Response, json_path: str, exp_value: Any, msg: str = None):
        act_value = self.get_value_of(response=respnse)
        
        if msg is None:
            msg = f"Jsonpath: {json_path}. Expecting list of {act_value} to NOT contain {act_value}."

        assert_that_list_does_not_contain(lst=act_value, item=exp_value, e_msg=msg)

    def __execute(self, response: Response, query: str) -> Any:
        query = parse(query)
        result = [match.value for match in query.find(response.json())]
        if len(result) == 0:
            raise Exception(f"The query path: {query} did not match any value in the response. \n{str(response.json())}")
        return result
    
class APICore(APIRequests, APIValidations):
    pass