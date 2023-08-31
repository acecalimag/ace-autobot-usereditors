from typing import TypedDict


class CustomerOrderFormDetails(TypedDict, total=False):
    """Holds the values for the Customer Order Form Details

    - ``selected_order_type``: List of the selected order type.
    - ``phone_number1``: Value of the phone number 1 field.
    - ``phone_number2``: Value of the phone number 2 field.
    - ``name``: Value of the name field.
    - ``street``: Value of the street field.
    - ``address_type``: Label of the selected radio button for address type.
    - ``miles``: Value of the miles field.
    - ``city``: Value of the city field.
    - ``order_remark``: Value of the remark field.
    - ``conf_note``: Value of the conf note field.
    - ``selected_call_skill``: Label of the selected radio button for the call skill.
    """

    selected_order_type: list[str] | None
    phone_number1: str | None
    phone_number2: str | None
    name: str | None
    street: str | None
    address_type: str | None
    miles: str | None
    city: str | None
    order_remark: str | None
    conf_note: str | None
    selected_call_skill: str | None
