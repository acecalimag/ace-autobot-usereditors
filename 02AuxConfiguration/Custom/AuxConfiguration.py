import time

from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn

import json

@library
class AuxConfiguration:
    @keyword
    def verification_message(self,status):
        if  status == True:
            pass
        else :
            raise Exception(" 'MGMT' should have been selected but was not.")
