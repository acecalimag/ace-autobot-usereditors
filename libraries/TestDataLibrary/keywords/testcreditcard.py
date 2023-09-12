import random
from robot.api.deco import keyword
from autocore.bases import LibraryComponentBase
from libraries.TestDataLibrary.dto.testccdetails import CreditCardDetails
from autocore import envlabels
from libraries.TestDataLibrary.data.creditcards import QA_TEST_CREDIT_CARDS, PROD_TEST_CREDIT_CARDS

class TestCreditCard(LibraryComponentBase):
    
    @keyword(tags=("CreditCardDetails",))
    def get_test_credit_card(self, card_id: str = None, _: CreditCardDetails = None) -> CreditCardDetails:
        """Get a test credit card and return the details as an object of `CreditCardDetails`.

        - ``card_id``: If not provided, a random credit card from the available credit cards will be returned.
        Accepted values: ``visa``
        """
        if self.globals.env == envlabels.QA_ENV:
            credit_cards = QA_TEST_CREDIT_CARDS
        elif self.globals.env == envlabels.PROD_ENV:
            credit_cards = PROD_TEST_CREDIT_CARDS
        else:
            raise Exception(
                f"No test credit cards set for [ {self.globals.env} ] environment.")

        if card_id is None:
            random_key = random.choice(list(credit_cards.keys()))
            details = credit_cards.get(random_key)
        else:
            details = credit_cards.get(card_id.lower().strip())
            if details is None:
                raise Exception(
                    f"No credit card with id [{card_id}] in [{self.globals.env}] environment.")

        self.logger.debug(details)
        return details