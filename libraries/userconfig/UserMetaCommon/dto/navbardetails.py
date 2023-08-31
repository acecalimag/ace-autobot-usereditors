from typing import TypedDict


class NavbarDetails(TypedDict, total=False):
    username: str | None
    position: str | None
    editor_dropdown_options: list[str] | None
    menu_items: list[str] | None