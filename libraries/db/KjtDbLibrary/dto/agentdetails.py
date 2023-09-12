from typing import TypedDict


class AgentDetails(TypedDict):
    uid: str | None
    username: str | None
    name: str | None
    position: str | None
    location: str | None