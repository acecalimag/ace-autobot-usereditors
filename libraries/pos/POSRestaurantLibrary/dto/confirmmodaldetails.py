from typing import TypedDict


class ConfirmModalDetails(TypedDict, total=False):
    """Hold the values of the Confirm Modal.

      - ``title``: the title of the modal.
      - ``message``: the message in the modal.

      """
    title: str | None
    message: str | None
    order_number: str | None
