from typing import TypedDict


class TestUserAccount(TypedDict):
    """
    - ``username``: username of the test user
    - ``password``: password of the test user
    - ``fullname``: fullname of the test user
    - ``position``: position of the test user
    """
    username: str
    password: str
    fullname: str
    position: str
