from typing import TypedDict


class UserTeamsDetails(TypedDict):
    utid: str | None
    name: str | None
    type: str | None
    status: str | None


class UserTeamsDetails1(TypedDict):
    utid: str | None
    name: str | None
    description: str | None
    lead: str | None
    location: str | None
    type: str | None
    status: str | None
    last_updated: str | None