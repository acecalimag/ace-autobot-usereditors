from typing import TypedDict


class CreditCardModalDetails(TypedDict, total=False):
    """Hold the details of the selected order from MORE display > Order list area and order details area.

    - ``modal_info``: the text description in the credit card modal.
    - ``cc_charge``: the amount in the credit card charge field.
    - ``cash_charge``: the amount in the cash charge field.
    - ``tip``: the amount in the tip field.
    - ``card_number``: the card number.
    - ``expi_date``: the expiration date of the card. Format mm/yy.
    - ``cvv``: the cvv.
    - ``postal_code``: the postal code or zip code.
    - ``cc_charge_error_msg``: the credit card charge error message.
    - ``cash_charge_error_msg``: the cash charge error message.
    - ``propay_error_msg``: error message in the propay form.
    - ``propay_cc_num_err_msg``: error message in the propay form credit card field.
    - ``propay_cvv_err_msg``: error message in the propay form cvv field.
    - ``non_propay_cc_num_err_msg``: error message in the non propay form credit card field.
    - ``non_propay_expi_date_err_msg``: error message in the non propay form expiration date field.
    - ``non_propay_cvv_err_msg``: error message in the non propay form cvv field.
    - ``non_propay_postal_code_err_msg``: error message in the non propay form postal code field.
    - ``non_propay_repeat_expi``: repeat message in the non propay form expiration date field.
    - ``non_propay_repeat_cvv``: repeat message in the non propay form cvv field.
    - ``non_propay_repeat_zip``: repeat message in the non propay form zip field.
    - ``visible_fields``: visible fields in the form.
    - ``existing_card_number``: card number in the existing credit card form.
    """

    modal_info: str | None
    cc_charge: str | None
    cc_charge_error_msg: str | None
    cash_charge: str | None
    cash_charge_err_msg: str | None
    propay_err_msg: str | None
    propay_cc_num_err_msg: str | None
    propay_cvv_err_msg: str | None
    non_propay_cc_num_err_msg: str | None
    non_propay_expi_date_err_msg: str | None
    non_propay_cvv_err_msg: str | None
    non_propay_postal_code_err_msg: str | None
    non_propay_repeat_expi: str | None
    non_propay_repeat_cvv: str | None
    non_propay_repeat_zip: str | None
    tip: str | None
    card_number: str | None
    expi_date: str | None
    cvv: str | None
    postal_code: str | None
    visible_fields: list[str] | None
    existing_card_number: str | None
