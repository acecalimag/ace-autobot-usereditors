from typing import TypedDict


class VoidOrderModalDetails(TypedDict, total=False):
    """Holds the values visible in the void order modal.
    - ``title``: title of the modal
    - ``order_number``: the order number. E.g. 10
    - ``cust_phone``: the customer phone.
    - ``time``: the time displayed in the modal
    - ``selected_option``: the selected void remark
    - ``available_options``: list of the available void remarks.
    """
    title: str | None
    order_number: str | None
    cust_phone: str | None
    time: str | None
    selected_option: str | None
    available_options: list[str] | None
