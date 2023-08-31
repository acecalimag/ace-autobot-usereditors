from typing import TypedDict


class UserTeamsDetails(TypedDict):
    utid: str | None
    name: str | None
    type: str | None
    status: str | None