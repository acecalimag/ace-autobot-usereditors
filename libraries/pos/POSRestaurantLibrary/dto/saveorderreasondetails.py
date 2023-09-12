from typing import TypedDict


class SaveOrderReasonDetails(TypedDict, total=False):
    """Holds the details of the save order modal.

    - ``title`` - title of the modal
    - ``description`` - description of the modal
    - ``reasons`` - save order reasons
    - ``order_remark`` - text in the order remark text area
    """
    title: str | None
    description: str | None
    reasons: list[str] | None
    order_remark: str | None
