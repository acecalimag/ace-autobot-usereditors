from typing import TypedDict


class OrderDetails(TypedDict, total=False):
    """Hold the details of the selected order from MORE display > Order list area and order details area.

    - ``oid``: id of the selected order.
    - ``order_number``: order number of the selected order. E.g. C4
    - ``order_version``: version of the selected order. E.g. 2
    - ``create_time``: the time displayed in the order details area. E.g. 05/05/2023 09:24 PM
    - ``agent``: the name of the agent
    - ``payment_type``: the payment type of the selected order. E.g. CC-WPAY-VOICE
    - ``tip``: tip amount. E.g. +10.00
    - ``order_type``: order type of the selected order. E.g. DELIVERY
    - ``order_status``: status of the selected order. E.g. CANCELED
    - ``estimated_time``: E.g. 70 - 75 mins
    - ``new_cust``: True for new customers, else False
    - ``phone1``: Phone1 of the customer. E.g. (112) 313-2313
    - ``phone2``: Phone2 of the customer.
    - ``customer_name``: Name of the customer.
    - ``street1``: Street 1 of the customer.
    - ``address_type``: Address type of the customer. E.g. hse, biz, apt
    - ``street2``: Street 2 of the customer.
    - ``city``: City of the customer.
    - ``order_remark``
    - ``conf_note``
    - ``rush_comment``
    - ``void_comment``
    """

    oid: str | None
    order_number: str | None
    order_version: str | None
    create_time: str | None
    agent: str | None
    payment_type: str | None
    tip: str | None
    order_type: str | None
    order_status: str | None
    estimated_time: str | None
    new_cust: bool | None
    phone1: str | None
    phone2: str | None
    customer_name: str | None
    street1: str | None
    address_type: str | None
    street2: str | None
    city: str | None
    order_remark: str | None
    conf_note: str | None
    rush_comment: str | None
    void_comment: str | None


class DisplayedOrders(TypedDict, total=False):
    """    
    - ``sent_orders``: List of order ids of sent orders displayed in the order list.
    - ``cancelled_orders``: List of order ids of cancelled orders displayed in the order list.
    - ``saved_order``: List of orders ids of saved orders displayed in the order list.
    """
    sent_orders: list[str] | None
    cancelled_orders: list[str] | None
    saved_orders: list[str] | None
    