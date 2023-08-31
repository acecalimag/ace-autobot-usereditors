from robot.api.deco import keyword, library
from autocore.bases import LibraryBase
from autocore.html import HTML

_ORDER_CREATE_TIME: str = "xpath:(//table[1]//font)[1]"
_ORDER_NUMBER: str = "xpath:(//table[1]//font)[2]"
_VOID_REASON_EN: str = "xpath:(//font[@face='Aller'])[2]"
_TOTAL: str = "xpath://td[text()='TOTAL:']//following-sibling::td[@class='price']"

@library(scope='GLOBAL')
class VoidReceiptLibrary(LibraryBase):
    
    @keyword(tags=("VoidReceipt",))
    def void_order_receipt_details_should_be(self, html_str: str, order_number: str = None, order_type: str = None,
                                             phone: str = None, name: str = None,
                                             street: str = None, city: str = None, note: str = None,
                                             void_reason_en: str = None, total: str = None, order_creation_time: str = None):
        html_obj = HTML(html_string=html_str)
        sa = self.asserts.SoftAssert()

        sa.assert_equal(actual=html_obj.get_count_of_element_located_by(locator=_ORDER_CREATE_TIME), exp="1",
                        desc="Order create time.")
        sa.assert_that_text_is_not_empty(txt=html_obj.get_text_of_element(locator=_ORDER_CREATE_TIME),
                                         desc="Order Creation Time.")

        if order_creation_time is not None:
            sa.assert_equal(actual=html_obj.get_text_of_element(
                locator=_ORDER_CREATE_TIME), exp=order_creation_time, desc="Order Creation Time.")

        sa.assert_equal(actual=html_obj.get_count_of_element_located_by(locator=_ORDER_NUMBER), exp="1",
                        desc="Order number.")
        if order_number is not None:
            sa.assert_equal(actual=html_obj.get_text_of_element(
                locator=_ORDER_NUMBER), exp=order_number)

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

        if order_type.upper().replace(" ", "") == 'PICKUP':
            sa.assert_true('Addr:' not in receipt_texts, s_msg="Verified that address is not in the receipt.",
                           desc="Address.")
            sa.assert_true('City:' not in receipt_texts, s_msg="Verified that city is not in the receipt.",
                           desc="City.")
        elif order_type.upper() == 'DELIVERY':
            if street is not None:
                sa.assert_that_text_contains(txt=receipt_texts, content=f"Addr: {street}",
                                             s_msg=f"Verified that address is {street}.", desc="Address.")

            if city is not None:
                sa.assert_that_text_contains(txt=receipt_texts, content=f"City: {city}",
                                             s_msg=f"Verified that city is {city}.", desc="City.")

        if note is not None:
            sa.assert_that_text_contains(txt=receipt_texts, content=f"Note: {note}",
                                         s_msg=f"Verified that note is {note}.", desc="Note.")

        sa.assert_that_text_contains(txt=receipt_texts, content="**客人要取消**")
        sa.assert_that_text_contains(
            txt=receipt_texts, content="Customer cancelled order")

        sa.assert_equal(actual=html_obj.get_count_of_element_located_by(locator=_VOID_REASON_EN), exp="1",
                        desc="Void reason.")
        if void_reason_en is not None:
            sa.assert_equal(actual=html_obj.get_text_of_element(locator=_VOID_REASON_EN), exp=void_reason_en,
                            desc=f"Void reason.")

        sa.assert_equal(actual=html_obj.get_count_of_element_located_by(locator=_TOTAL), exp="1",
                        desc="Total amount.")
        if total is not None:
            sa.assert_equal(actual=html_obj.get_text_of_element(locator=_TOTAL), exp=total,
                            desc="Total amount.")
        sa.assert_all()
