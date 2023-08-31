from typing import TypedDict


class OrderBillDetails(TypedDict, total=False):
    """Hold the values for the order bill details. Dollar or Currency signs are excluded.

    - ``discount``: The discount amount.
    - ``subtotal``: The subtotal amount.
    - ``tax``: The tax amount.
    - ``delivery``: The delivery amount.
    - ``total``: The total amount.

    """
    discount: str | None
    subtotal: str | None
    tax: str | None
    delivery: str | None
    total: str | None
