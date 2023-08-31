from typing import TypedDict


class TestRestaurantDetails(TypedDict):
    """Holds the restaurant details.
       - ``rid``: Restaurant ID
       - ``ex_name``: ex_name of the restaurant
       - ``en_name``: en_name of the restaurant
       - ``address1``: address1 of the restaurant
       - ``address2``: address2 of the restaurant
       - ``city``: city of the restaurant
       - ``state``: state of the restaurant
       - ``zipcode``: zipcode of the restaurant
       - ``contact_phone1``: contact_phone1 of the restaurant
    """
    rid: str
    ex_name: str
    en_name: str
    address1: str
    address2: str | None
    city: str
    state: str
    zipcode: str
    contact_phone1: str

