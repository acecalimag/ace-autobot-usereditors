from robot.api.deco import keyword, library
from autocore.bases import LibraryBase
from autocore.html import HTML

_ORDER_CREATE_TIME: str = "xpath:(//table[1]//font)[1]"
_ORDER_NUMBER: str = "xpath:(//table[1]//font)[2]"
_RUSH_REASON_EN: str = "xpath:(//font[@face='Aller'])[2]"
_TOTAL: str = "xpath://td[text()='TOTAL:']//following-sibling::td[@class='price']"

@library(scope='GLOBAL')
class RushReceiptLibrary(LibraryBase):

    @keyword(tags=("RushReceipt",))
    def rush_order_receipt_details_should_be(self, html: str, order_number: str = None, phone: str = None,
                                             name: str = None, street: str = None, city: str = None, note: str = None,
                                             rush_reason_en: str = None, total: str = None, order_creation_time: str = None):
        html_obj = HTML(html_string=html)
        sa = self.asserts.SoftAssert()

        sa.assert_equal(actual=html_obj.get_count_of_element_located_by(locator=_ORDER_CREATE_TIME), exp="1",
                        desc="Order create time.")
        sa.assert_that_text_is_not_empty(txt=html_obj.get_text_of_element(locator=_ORDER_CREATE_TIME),
                                         desc="Order Creation Time.")
        
        if order_creation_time is not None:
            sa.assert_equal(actual=html_obj.get_text_of_element(locator=_ORDER_CREATE_TIME), exp=order_creation_time, desc="Order Creation Time.")

        sa.assert_equal(actual=html_obj.get_count_of_element_located_by(locator=_ORDER_NUMBER), exp="1",
                        desc="Order number.")
        if order_number is not None:
            sa.assert_equal(actual=html_obj.get_text_of_element(locator=_ORDER_NUMBER), exp=order_number,
                            desc="Order number.")

        receipt_texts = html_obj.get_text_of_element(locator="id:container")
        receipt_texts = " ".join(
            [i.replace(" ", "") for i in receipt_texts.replace("\xa0", " ").replace("\n", " ").split(" ") if
             len(i) > 0])

        self.logger.debug(f"Receipt texts: {receipt_texts}")

        if phone is not None:
            sa.assert_that_text_contains(txt=receipt_texts, content=f"Phone: {phone}",
                                         s_msg=f"Verified that phone number is {phone}.", desc="Phone.")
        if name is not None:
            sa.assert_that_text_contains(txt=receipt_texts, content=f"Name: {name}",
                                         s_msg=f"Verified that name is {name}.", desc="Name.")

        if street is not None:
            sa.assert_that_text_contains(txt=receipt_texts, content=f"Addr: {street}",
                                         s_msg=f"Verified that address is {street}.", desc="Address.")

        if city is not None:
            sa.assert_that_text_contains(txt=receipt_texts, content=f"City: {city}",
                                         s_msg=f"Verified that city is {city}.", desc="City.")

        if note is not None:
            sa.assert_that_text_contains(txt=receipt_texts, content=f"Note: {note}",
                                         s_msg=f"Verified that note is {note}.", desc="Note.")

        sa.assert_that_text_contains(txt=receipt_texts, content="**客人催单**")
        sa.assert_that_text_contains(txt=receipt_texts, content="RUSH")

        sa.assert_equal(actual=html_obj.get_count_of_element_located_by(locator=_RUSH_REASON_EN), exp="1",
                        desc="Rush reason.")
        if rush_reason_en is not None:
            sa.assert_equal(actual=html_obj.get_text_of_element(locator=_RUSH_REASON_EN), exp=rush_reason_en,
                            desc="Rush reason.")

        sa.assert_equal(actual=html_obj.get_count_of_element_located_by(locator=_TOTAL), exp="1",
                        desc="Verified that total amount is visible.")
        if total is not None:
            sa.assert_equal(actual=html_obj.get_text_of_element(locator=_TOTAL), exp=total,
                            desc="Total.")
        sa.assert_all()
