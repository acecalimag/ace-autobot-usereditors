from robot.api.deco import library, keyword
from autocore.html import HTML

from libraries.receipts.orderreceiptbase import OrderReceiptLibraryBase

_CONTAINER: str = "id:container"

_RESTAURANT_NAME: str = "xpath:(//div[@id='container']/div)[1]/b/font"
_RESTAURANT_DETAILS: str = "xpath:(//div[@id='container']/div)[1]/font"
_EN_ORDER_TYPE: str = "xpath:(//table)[1]//tr[1]//td[1]//font[@face='en-font']"
_CN_ORDER_TYPE: str = "xpath:(//table)[1]//tr[1]//td[1]//font[@face='cn-font']"
_ORDER_NUMBER: str = "xpath:(//table)[1]//tr[1]//td[2]//font"
_ORDER_CREATE_TIME: str = "xpath:(//table)[1]//tr[2]//font"

_CUSTOMER_PHONE1: str = "xpath://font[text()='Phone: ']//following-sibling::span[1]/font"
_CUSTOMER_PHONE2: str = "xpath://font[text()='Phone: ']//following-sibling::span[2]/font"
_CUSTOMER_NAME: str = "xpath://font[text()='Name: ']//following-sibling::span[1]/font"
_CUSTOMER_ADDRESS1: str = "xpath://font[text()='Addr: ']//following-sibling::span[1]/font"
_CUSTOMER_ADDRESS2: str = "xpath://font[text()='Addr: ']//following-sibling::span[2]/font"
_CUSTOMER_CITY: str = "xpath://font[text()='City: ']//following-sibling::span[1]/font"
_ORDER_REMARK: str = "xpath://font[text()='Note: ']//following-sibling::span[1]/font"

_BORDERS: str = "xpath://div[contains(@style,'border-bottom: 1px solid #000000;')]"

# For counting dishes (english text only)
# param is index
_EN_DISH_DESC_INDEXED: str = "xpath:(//table[2]//td[@class='description']//font[@face='en-font'])[{0}]"
# param is index
_DISH_QTY_INDEXED: str = "xpath:(//table[2]//td[@class='description']//font[@face='en-font'])[{0}]//ancestor::tr//td[@class='qty']"
# param is index
_DISH_SIZE_INDEXED: str = "xpath:(//table[2]//td[@class='description']//font[@face='en-font'])[{0}]//ancestor::tr//td[@class='size']/font"
# param is index
_DISH_PRICE_INDEXED: str = "xpath:(//table[2]//td[@class='description']//font[@face='en-font'])[{0}]//ancestor::tr//td[@class='price']/font"

_CREDIT_CARD_CHARGE: str = "xpath://font[text()='CREDIT CARD:']//ancestor::tr/td[@class='price']/font"
_CASH_CHARGE: str = "xpath://font[text()='CASH:']//ancestor::tr/td[@class='price']/font"

_THANK_YOU: str = "xpath://font[text()='Thank You Very Much']"
_PAY_BY_CREDIT_CARD_NOTE: str = "xpath://font[text()='Pay By Credit Card ']"
_PAY_BY_CASH_INSTEAD: str = "xpath://font[text()='Pay By Cash Instead ']"

_REPRINT_EN_TEXT: str = "xpath://font[starts-with(text(),'REPRINT')]"
_REPRINT_TIME: str = "xpath://font[starts-with(text(),'REPRINT')]//following-sibling::font"
_REPRINT_CN_TEXT: str = "xpath://font[contains(text(),'重复打印')]"


@library(scope='GLOBAL')
class DynamicOrderReceiptNoTotalsLibrary(OrderReceiptLibraryBase):

    @keyword
    def receipt_details_should_include(self, html_object: HTML, res_en_name: str = None, res_addr1: str = None, res_addr2: str = None, res_city: str = None, res_state: str = None, res_zipcode: str = None, res_phone: str = None,
                                       en_order_type: str = None, cn_order_type: str = None, order_number: str = None, cx_name: str = None, cx_phone1: str = None, cx_phone2: str = None,
                                       cx_addr1: str = None, cx_addr2: str = None, cx_city: str = None, cx_note: str = None, cc_charge: str = None, cash_charge: str = None):
        sa = self.asserts.SoftAssert()

        sa.assert_equal(actual=html_object.get_text_of_element(
            locator=_RESTAURANT_NAME, normalize=True), exp=res_en_name, desc="Restaurant name.")

        address = res_addr1
        if len(res_addr2) > 0:
            address = f"{res_addr1} {res_addr2}"

        exp_address = f"{address} {res_city}, {res_state} {res_zipcode} {res_phone}"
        sa.assert_equal(actual=html_object.get_text_of_element(locator=_RESTAURANT_DETAILS, normalize=True),
                        exp=exp_address,
                        desc="Restaurant Details.")

        if en_order_type is not None:
            sa.assert_equal(actual=html_object.get_text_of_element(locator=_EN_ORDER_TYPE), exp=en_order_type,
                            desc="EN Order Type.")

        if cn_order_type is not None:
            act_order_type = html_object.get_text_of_element(
                locator=_CN_ORDER_TYPE).split(" ")[0]
            sa.assert_equal(actual=act_order_type, exp=cn_order_type,
                            e_msg=f"Expecting CN order type to be [ {cn_order_type} ] but got [ {act_order_type} ].",
                            s_msg=f"Verified that the displayed CN order type is [ {cn_order_type} ]. Actual: [ {act_order_type} ].")

        if order_number is not None:
            sa.assert_equal(actual=html_object.get_text_of_element(locator=_ORDER_NUMBER), exp=order_number,
                            desc="Order Number.")

        sa.assert_that_text_is_not_empty(txt=html_object.get_text_of_element(locator=_ORDER_CREATE_TIME),
                                         desc="Order Creation Time.")
        sa.assert_that_date_format_is(date=html_object.get_text_of_element(locator=_ORDER_CREATE_TIME), exp_format="%m-%d-%Y  %I:%M %p",
                                      desc="Order Create time format should be: %m-%d-%Y  %I:%M %p")

        if cx_name is not None:
            sa.assert_equal(actual=html_object.get_text_of_element(locator=_CUSTOMER_NAME), exp=cx_name,
                            desc="Customer Name.")

        if cx_phone1 is not None:
            sa.assert_equal(actual=html_object.get_text_of_element(locator=_CUSTOMER_PHONE1), exp=cx_phone1,
                            desc="Customer Phone 1.")

        if cx_phone2 is not None:
            sa.assert_that_strings_are_equal(actual=html_object.get_text_of_element(locator=_CUSTOMER_PHONE2),
                                             exp=cx_phone2, ignore_space=True, desc="Customer Phone 2.")

        if cx_addr1 is not None:
            sa.assert_equal(actual=html_object.get_text_of_element(locator=_CUSTOMER_ADDRESS1),
                            exp=cx_addr1.upper(), desc="Customer Address 1.")

        if cx_addr2 is not None:
            sa.assert_equal(actual=html_object.get_text_of_element(locator=_CUSTOMER_ADDRESS2),
                            exp=cx_addr2.upper(), desc="Customer Address 2.")

        if cx_city is not None:
            sa.assert_equal(actual=html_object.get_text_of_element(locator=_CUSTOMER_CITY), exp=cx_city.upper(),
                            desc="Customer City.")

        if cx_note is not None:
            sa.assert_equal(actual=html_object.get_text_of_element(
                locator=_ORDER_REMARK), exp=cx_note, desc="Note.")

        if cc_charge is not None:
            sa.assert_equal(actual=html_object.get_text_of_element(locator=_CREDIT_CARD_CHARGE),
                            exp=cc_charge,
                            desc="Credit Card Charge.")

        if cash_charge is not None:
            sa.assert_equal(actual=html_object.get_text_of_element(locator=_CASH_CHARGE), exp=cash_charge,
                            desc="Cash Charge.")

        all_receipt_text = html_object.get_text_of_element(
            locator=_CONTAINER).upper()
        self.logger.debug(f"RECEIPT TEXTS: {all_receipt_text}")
        sa.assert_true("SUBTOTAL" not in all_receipt_text,
                       s_msg="Verified that subtotal is not displayed.")
        sa.assert_true("TAX" not in all_receipt_text,
                       s_msg="Verified that tax is not displayed.")
        sa.assert_true("TOTAL" not in all_receipt_text,
                       s_msg="Verified that total is not displayed.")
        sa.assert_all()

    @keyword
    def reprint_details_should_be_displayed(self, html_object: HTML, reprint_number: str, reprint_en_text: str = None, reprint_cn_text: str = None):
        sa = self.asserts.SoftAssert()
        if reprint_en_text is not None:
            sa.assert_equal(actual=html_object.get_text_of_element(locator=_REPRINT_EN_TEXT),
                            exp=f"{reprint_en_text}#{reprint_number}", desc="Reprint english text.")

        if reprint_cn_text is not None:
            sa.assert_that_text_is_not_empty(txt=html_object.get_text_of_element(locator=_REPRINT_TIME),
                                             desc="Reprint type should be visible.")
        sa.assert_equal(actual=html_object.get_text_of_element(locator=_REPRINT_CN_TEXT),
                        exp=f"{reprint_cn_text}{reprint_number}",
                        desc="Reprint cn text.")
        sa.assert_all()

    @keyword
    def thank_you_message_should_be_visible(self, html_object: HTML):
        self.asserts.assert_equal(actual=html_object.get_text_of_element(locator=_THANK_YOU), exp="Thank You Very Much",
                                  desc="Thank you message.")

    @keyword
    def tip_suggestions_should_not_be_displayed(self, html_object: HTML):
        all_receipt_text = html_object.get_text_of_element(
            locator=_CONTAINER).upper()
        self.logger.debug(f"RECEIPT TEXTS: {all_receipt_text}")
        self.asserts.assert_true("TIP SUGGESTIONS" not in all_receipt_text,
                                 s_msg="Verified that tip suggestion is not visible.")

    @keyword
    def en_dish_details_should_be_present(self, html_object: HTML, item_no: str, qty: str = None, size: str = None, description: str = None, price: str = None):
        item_no = int(item_no)
        sa = self.asserts.SoftAssert()
        if description is not None:
            sa.assert_that_strings_are_equal(
                html_object.get_text_of_element(locator=_EN_DISH_DESC_INDEXED.format(item_no)), exp=description,
                desc="Dish Description.", ignore_space=True)
        if qty is not None:
            sa.assert_that_strings_are_equal(
                actual=html_object.get_text_of_element(locator=_DISH_QTY_INDEXED.format(item_no)), exp=qty,
                desc="Dish Quantity.", ignore_space=True)
        if size is not None:
            sa.assert_that_strings_are_equal(
                actual=html_object.get_text_of_element(
                    locator=_DISH_SIZE_INDEXED.format(item_no)),
                exp=size, desc="Dish size.", ignore_space=True)
        if price is not None:
            sa.assert_that_strings_are_equal(
                actual=html_object.get_text_of_element(
                    locator=_DISH_PRICE_INDEXED.format(item_no)),
                exp=price, desc="Dish price.", ignore_space=True)
        sa.assert_all()

    @keyword
    def count_of_divider_lines_should_be(self, html_object: HTML, count: str):
        self.asserts.assert_equal(actual=html_object.get_count_of_element_located_by(locator=_BORDERS), exp=count,
                                  desc="Border Count.")

    @keyword
    def credit_card_charge_should_not_be_visible(self, html_object: HTML):
        all_receipt_text = html_object.get_text_of_element(
            locator=_CONTAINER).upper()
        self.logger.debug(f"RECEIPT TEXTS: {all_receipt_text}")
        self.asserts.assert_true("CREDIT CARD:" not in all_receipt_text,
                                 s_msg="Credit card charge should not be visible.")

    @keyword
    def cash_charge_should_not_be_visible(self, html_object: HTML):
        all_receipt_text = html_object.get_text_of_element(
            locator=_CONTAINER).upper()
        self.logger.debug(f"RECEIPT TEXTS: {all_receipt_text}")
        self.asserts.assert_true("CASH:" not in all_receipt_text,
                                 s_msg="Cash charge should not be visible.")

    @keyword
    def delivery_fee_should_not_be_visible(self, html_object: HTML):
        all_receipt_text = html_object.get_text_of_element(
            locator=_CONTAINER).upper()
        self.logger.debug(f"RECEIPT TEXTS: {all_receipt_text}")
        self.asserts.assert_true("DELIVERY:" not in all_receipt_text,
                                 s_msg="Delivery fee should not be visible.")

    @keyword
    def pay_by_credit_card_note_should_be_visible(self, html_object: HTML):
        self.asserts.assert_equal(actual=html_object.get_count_of_element_located_by(locator=_PAY_BY_CREDIT_CARD_NOTE), exp="1",
                                  desc=f"Pay by credit card note should be visible. Actual text: {html_object.get_text_of_element(locator=_PAY_BY_CREDIT_CARD_NOTE)}")

    @keyword
    def pay_by_credit_card_note_should_not_be_visible(self, html_object: HTML):
        self.asserts.assert_equal(actual=html_object.get_count_of_element_located_by(locator=_PAY_BY_CREDIT_CARD_NOTE), exp="0",
                                  desc=f"Pay by credit card note should not be visible.")

    @keyword
    def customer_address_details_should_not_be_visible(self, html_object: HTML):
        sa = self.asserts.SoftAssert()
        sa.assert_equal(actual=html_object.get_count_of_element_located_by(locator=_CUSTOMER_CITY), exp="0",
                        desc="Customer city should not be visible.")
        sa.assert_equal(actual=html_object.get_count_of_element_located_by(locator=_CUSTOMER_ADDRESS1), exp="0",
                        desc="Customer address1 should not be visible.")
        sa.assert_equal(actual=html_object.get_count_of_element_located_by(locator=_CUSTOMER_ADDRESS2), exp="0",
                        desc="Customer address2 should not be visible.")

        sa.assert_all()
