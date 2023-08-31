from libraries.TestDataLibrary.dto.testccdetails import CreditCardDetails


QA_TEST_CREDIT_CARDS: dict = {
    'visa': CreditCardDetails(cc_num='4111111111111111', expi_date='10/30', cvc='999', zip_code='84321')
}

PROD_TEST_CREDIT_CARDS: dict = {
    'visa': CreditCardDetails(cc_num='4511292338511618', expi_date='09/29', cvc='408', zip_code='11101')
}
