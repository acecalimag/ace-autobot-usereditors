from typing import TypedDict


class TestCustomerDetails(TypedDict, total=False):
    """Holds the details of the test customers.
    - ``name``: Name of the test customer.
    - ``phone1``: Phone1 of the test customer.
    - ``phone2``: Phone2 of the test customer.
    - ``street``: Street of the test customer.
    - ``City``: City of the test customer.
    """
    name: str
    phone1: str
    phone2: str
    street: str
    city: str
