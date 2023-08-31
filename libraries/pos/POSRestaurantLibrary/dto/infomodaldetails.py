from typing import TypedDict


class InfoModalDetails(TypedDict, total=False):
    """Hold the values of the Info Modal.

      - ``title``: the title of the modal.
      - ``message``: the message in the modal.

      """
    title: str | None
    message: str | None
