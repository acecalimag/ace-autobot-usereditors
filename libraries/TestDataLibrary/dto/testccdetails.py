from typing import TypedDict


class CreditCardDetails(TypedDict):
    """Holds the credit card details.
    - ``cc_num``: Credit card number
    - ``expi_date``: Card expiration date. Format mm/yy. E.g.12/24
    - ``cvc``: Cvc or Cvv of the card.
    - ``zip_code``: Zip code or postal code of the card
    """
    cc_num: str
    expi_date: str
    cvc: str
    zip_code: str
