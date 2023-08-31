from typing import TypedDict


class HomepageDetails(TypedDict, total=False):
    """Holds the values present in POS homepage.

    - ``button_labels``: Text labels of the buttons.
    - ``status_options``: The text labels of the status options.
    - ``restaurants``: The names of the restaurants. E.g. en_name (ex_name) .
    - ``username``: The username of the user including its position and department.
    - ``inbound_contacts``: The number of inbound contacts.
    - ``att``: The number of ATT.
    - ``awt``: The number of AWT.
    - ``aht``: The number of AHT.
    - ``active``: The number of active restaurants.
    - ``onboarding``: The number of onboarding restaurants.
    - ``offboarding``: The number of offboarding restaurants.
    """

    button_labels: list[str] | None
    status_options: list[str] | None
    restaurants: list[str] | None
    username: str | None
    inbound_contacts: str | None
    att: str | None
    awt: str | None
    aht: str | None
    active: str | None
    onboarding: str | None
    offboarding: str | None
