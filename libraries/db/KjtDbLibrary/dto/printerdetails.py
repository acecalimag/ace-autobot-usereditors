from datetime import datetime
from typing import TypedDict


class PrinterDetails(TypedDict, total=True):
    pid: str | None
    rid: str | None
    name: str | None
    active: int | None
    nucless: int | None
    mask: str | None
    maskRule: str | None
    template: str | None
    templateSettings: str | None
    ccTemplate: str | None
    creditCardVoid: int | None
    printInternalMeta: int | None
    printExternalMeta: int | None
    status: str | None
    lastNormalTime: datetime | None
    lastContactTime: datetime | None
    statusReport : str | None
    lastUpdatedBy: str | None
    createTime: datetime | None
    updateTime: datetime |None