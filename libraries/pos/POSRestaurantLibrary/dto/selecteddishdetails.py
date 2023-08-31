from typing import TypedDict


class SelectedDishDetails(TypedDict):
    """Holds the details of the selected dishes.

    - ``quantity``: quantity of the selected dish.
    - ``size``: size of the selected dish.
    - ``description``: description of the selected dish. (Displayed dish name in the menu.)
    - ``price``: price of the dish, excluding the currency symbol.
    """

    quantity: str | None
    size: str | None
    description: str | None
    price: str | None
