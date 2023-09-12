

from datetime import datetime
from typing import TypedDict


class OnboardingTaskDetails(TypedDict):
    id: str
    rid: str
    cid: str
    name: str
    type: str
    status: str
    payload: str
    isActive: int
    createTime: datetime
    updateTime: datetime
    createdBy: str 
    updatedBy: str