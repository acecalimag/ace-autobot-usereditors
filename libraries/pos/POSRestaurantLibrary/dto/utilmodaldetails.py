from typing import TypedDict


class UtilModalDetails(TypedDict, total=False):
    """Holds the details visible in the Util Modal.

    - ``title``: Title of the modal.
    - ``body``: Text description in the modal.
    """
    title: str | None
    body: str | None
