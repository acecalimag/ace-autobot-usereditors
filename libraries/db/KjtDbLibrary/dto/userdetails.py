from typing import TypedDict


class UserDetails(TypedDict):
    uid: str | None
    username: str | None
    name: str | None
    isAdmin: int | None