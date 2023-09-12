import random
import secrets
import string
from robot.api.deco import keyword
from autocore import envlabels
from autocore.bases import LibraryComponentBase
from libraries.TestDataLibrary.dto.testcxdetails import TestCustomerDetails
from libraries.TestDataLibrary.data.testcustomers import QA_TEST_CUSTOMERS, PROD_TEST_CUSTOMERS

def _generate_random_phone(prefix: str = "111", fmt: bool = True):
    if not prefix.startswith("1"):
        raise Exception(
            "Test phone number should start with 1 to avoid accidentally sending message to real person.")

    digits = 7

    if len(prefix) > 3:
        prefix = prefix[:3]

    elif len(prefix) < 3:
        digits = 10 - len(prefix)
    phone_number = prefix

    for i in range(digits):
        num = secrets.choice("0123456789")
        phone_number = phone_number + num

    if fmt:
        return f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"
    else:
        return phone_number


def _generate_random_string(length):
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string.upper()


def _check_phone(phone: str):
    phone = "".join([i for i in phone if i.isdigit()])
    if not phone.startswith("1"):
        raise Exception(
            "Test phone number should start with 1 to avoid accidentally sending message to real person.")

class TestCustomer(LibraryComponentBase):
    
    @keyword(tags=("TestCustomer",))
    def get_test_customer(self, new: bool = False, _: TestCustomerDetails = None) -> TestCustomerDetails:
        """Get test customer and return details as an object of `TestCustomerDetails`

        - ``new``: If True, will generate a random phone number.
        """
        if self.globals.env == envlabels.QA_ENV:
            TEST_CUSTOMERS = QA_TEST_CUSTOMERS
        elif self.globals.env == envlabels.PROD_ENV:
            TEST_CUSTOMERS = PROD_TEST_CUSTOMERS
        else:
            raise Exception(f"No test customer ready for {self.globals.env} environment.")
        
        if new:
            phone_number1 = _generate_random_phone()
            phone_number2 = _generate_random_phone()
            details = random.choice(TEST_CUSTOMERS)
            details['phone1'] = phone_number1
            details['phone2'] = phone_number2

            name = details['name'].split(" ")
            name[len(name) - 1] = _generate_random_string(6)
            details['name'] = " ".join(name)
        else:
            details = random.choice(TEST_CUSTOMERS)

        _check_phone(details['phone1'])
        if details.get('phone2') is not None:
            _check_phone(details['phone2'])

        self.logger.debug(details)
        return details