
from datetime import datetime
from typing import TypedDict


class OnboardingRestaurantDetails(TypedDict):
    rid: str
    enName: str
    cnName: str 
    exName: str 
    status: str
    menuLink: str 
    comment: str 
    template: str 
    templateName: str
    scheduleInput: str
    hasDelivery: int 
    hasStudyGuidePublished: int
    sizeInfo: str 
    isAdvance: int 
    templateIndicator: str
    targetDateTime: datetime
    endDateTime: datetime
    createTime: datetime
    updateTime: datetime
    createdBy: str 
    updatedBy: str