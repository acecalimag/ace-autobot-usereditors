from datetime import datetime
from typing import TypedDict


class KjtOrderDetails(TypedDict, total=True):
    oid: str | None
    createTime: datetime | None
