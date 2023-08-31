from datetime import timedelta
import json
from autocore.AssertsLibrary import SoftAssert, assert_equal, assert_false, assert_that_list_contains_all, assert_true
from robot.api.deco import keyword
from autocore.bases import WebLibraryComponent
from libraries.contentconfig.PrinterEditorLibrary.locators import iframe, printereditorpage
from libraries.contentconfig.PrinterEditorLibrary.helpers.printerindexfinder import get_index_of_printer

class ValidationKeywords(WebLibraryComponent):

    def __init__(self, library, timeout:timedelta=...):
        super().__init__(library=library, timeout=timeout)
        self.__timeout = timedelta(seconds=0.1)
    

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def printer_should_be_active(self, pid: str, ):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            is_selected = self.web.is_selected(
                locator=printereditorpage.ACTIVE(index=idx))
            assert_true(e_msg=is_selected,
                        desc="Active Checkbox should be checked.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def printer_should_not_be_active(self, pid: str, ):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            is_selected = self.web.is_selected(
                locator=printereditorpage.ACTIVE(index=idx))
            assert_false(e_msg=is_selected,
                         desc="Active Checkbox should NOT be checked.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def printer_details_should_be(self, pid: str, name: str = None, mask: str = None, mask_rule: str = None, order_receipt_tpl: str = None,
                                  line: str = None, cc_template: str = None, last_updated: str = None, last_updated_by: str = None, cx_info_txt_font_size: str = None,
                                  cn_txt_font_size: str = None, en_txt_font_size: str = None, spacing: str = None, active: str = None, nucless: str = None):

        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            sa = SoftAssert()

            if nucless == '1':
                sa.handle(func=self.__element_should_be_selected,
                          locator=printereditorpage.NUCLESS_TOGGLE, el_name="Nucless toggle")
            if nucless == '0':
                sa.handle(func=self.__element_should_not_be_selected,
                          locator=printereditorpage.NUCLESS_TOGGLE, el_name="Nucless toggle")

            sa.assert_equal(actual=self.web.get_value(locator=printereditorpage.PID(
                index=idx)), exp=pid, desc=f"PID.")

            if active == '1':
                sa.handle(func=self.__element_should_be_selected, locator=printereditorpage.ACTIVE(
                    index=idx), el_name="Active checkbox")
            if active == '0':
                sa.handle(func=self.__element_should_not_be_selected, locator=printereditorpage.ACTIVE(
                    index=idx), el_name="Active checkbox")

            if name is not None:
                sa.assert_equal(actual=self.web.get_value(locator=printereditorpage.NAME(
                    index=idx)), exp=name, desc=f"Name.")

            if mask is not None:
                sa.assert_equal(actual=self.web.get_value(
                    locator=printereditorpage.MASK(index=idx)), exp=mask, desc="Mask.")

            if mask_rule is not None:
                if '_' in mask_rule:
                    words = mask_rule.split('_')
                    words = [i.capitalize() for i in words]
                    mask_rule = ' '.join(words)
                sa.assert_equal(actual=self.web.get_text(locator=printereditorpage.SELECTED_MASK_RULE(
                    index=idx)), exp=mask_rule, desc="Mask rule.")

            if order_receipt_tpl is not None:
                sa.assert_equal(actual=self.web.get_text(locator=printereditorpage.SELECTED_ORDER_RECEIPT(
                    index=idx)), exp=order_receipt_tpl, desc="Order receipt template.")

            if cx_info_txt_font_size is not None:
                if self.web.is_enabled(locator=printereditorpage.CUST_INFO_FONT_SIZE_SELECT(index=idx), timeout=timedelta(seconds=0.1)):
                    sa.assert_equal(actual=self.web.get_first_selected_option(locator=printereditorpage.CUST_INFO_FONT_SIZE_SELECT(
                        index=idx)), exp=cx_info_txt_font_size, desc="Customer info text font size.")

            if cn_txt_font_size is not None:
                if self.web.is_enabled(locator=printereditorpage.CHINESE_TEXT_FONT_SIZE_SELECT(index=idx), timeout=timedelta(seconds=0.1)):
                    font_size = self.web.get_selected_select_option_text(
                        locator=printereditorpage.CHINESE_TEXT_FONT_SIZE_SELECT(index=idx))
                    sa.assert_that_list_has_item(lst=font_size, content=str(
                        cn_txt_font_size), desc="Chinese text font size.")

            if en_txt_font_size is not None:
                if self.web.is_enabled(locator=printereditorpage.ENGLISH_TEXT_FONT_SIZE_SELECT(index=idx), timeout=timedelta(seconds=0.1)):
                    font_size = self.web.get_selected_select_option_text(
                        locator=printereditorpage.ENGLISH_TEXT_FONT_SIZE_SELECT(index=idx))
                    sa.assert_that_list_has_item(
                        lst=font_size, content=str(en_txt_font_size), desc="English text font size.")

            if spacing is not None:
                if self.web.is_enabled(locator=printereditorpage.SPACING_SELECT(index=idx), timeout=timedelta(seconds=0.1)):
                    selected_spacing = self.web.get_selected_select_option_text(
                        locator=printereditorpage.SPACING_SELECT(index=idx))
                    sa.assert_that_list_has_item(
                        lst=selected_spacing, content=spacing, desc="Spacing.")

            if line is not None:
                if self.web.is_enabled(locator=printereditorpage.LINE_SELECT(index=idx), timeout=timedelta(seconds=0.1)):
                    sa.assert_equal(actual=self.web.get_first_selected_option(
                        locator=printereditorpage.LINE_SELECT(index=idx)), exp=line, desc="Line.")
                else:
                    self.logger.warn(
                        f"Cannot validate the value of line for printer with pid: {pid} because the line field is disabled.")

            if cc_template is not None:
                sa.assert_equal(actual=self.web.get_text(locator=printereditorpage.SELECTED_CC_TEMPLATE(
                    index=idx)), exp=cc_template, desc="CC Template.")

            if last_updated is not None:
                sa.assert_equal(actual=self.web.get_text(locator=printereditorpage.LAST_UPDATED(
                    index=idx)), exp=last_updated, desc="Last updated.")

            if last_updated_by is not None:
                sa.assert_equal(actual=self.web.get_text(locator=printereditorpage.LAST_UPDATED_BY(
                    index=idx)), exp=last_updated_by, desc="Last updated by.")
            sa.assert_all()
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def nucless_details_should_be(self, pid: str, host: str = None, model: str = None, printer_port: str = None, status_port: str = None):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            sa = SoftAssert()
            if host is not None:
                sa.assert_equal(actual=self.web.get_value(
                    locator=printereditorpage.NUCLESS_HOST(index=idx)), exp=host, desc="Host.")
            if model is not None:
                sa.assert_equal(actual=self.web.get_text(
                    locator=printereditorpage.SELECTED_MODEL(index=idx)), exp=model, desc="Model.")
            if printer_port is not None:
                sa.assert_equal(actual=self.web.get_value(locator=printereditorpage.NUCLESS_PRINTER_PORT(
                    index=idx)), exp=printer_port, desc="Printer port.")
            if status_port is not None:
                sa.assert_equal(actual=self.web.get_value(locator=printereditorpage.NUCLESS_STATUS_PORT(
                    index=idx)), exp=status_port, desc="Status port.")
            sa.assert_all()
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def customer_info_text_checkbox_should_be_disabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_disabled(locator=printereditorpage.CUST_INFO_CHECKBOX(
                index=idx), el_name="Customer info text checkbox.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def customer_info_text_checkbox_should_be_enabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_enabled(locator=printereditorpage.CUST_INFO_CHECKBOX(
                index=idx), el_name="Customer info text check box.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def customer_info_text_font_size_should_be_enabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_enabled(locator=printereditorpage.CUST_INFO_FONT_SIZE_SELECT(
                index=idx), el_name="Customer info font size.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def customer_info_text_font_size_should_be_disabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_disabled(locator=printereditorpage.CUST_INFO_FONT_SIZE_SELECT(
                index=idx), el_name="Customer info font size.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def chinese_text_font_size_should_be_enabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_enabled(locator=printereditorpage.CHINESE_TEXT_FONT_SIZE_SELECT(
                index=idx), el_name="Chinese text font size.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def chinese_text_font_size_should_be_disabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_disabled(locator=printereditorpage.CHINESE_TEXT_FONT_SIZE_SELECT(
                index=idx), el_name="Chinese text font size.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def chinese_text_checkbox_should_be_enabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_enabled(locator=printereditorpage.CHINESE_TEXT_CHECKBOX(
                index=idx), el_name="Chinese text checkbox.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def chinese_text_checkbox_should_be_disabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_disabled(locator=printereditorpage.CHINESE_TEXT_CHECKBOX(
                index=idx), el_name="Chinese text checkbox.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def chinese_text_toggle_should_be_enabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_enabled(locator=printereditorpage.CHINESE_TEXT_BOLD_TOGGLE(
                index=idx), el_name="Chinese bold toggle.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def chinese_text_toggle_should_be_selected(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_selected(locator=printereditorpage.CHINESE_TEXT_BOLD_TOGGLE(
                index=idx), el_name="Chinese bold toggle.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def chinese_text_toggle_should_not_be_selected(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_not_be_selected(locator=printereditorpage.CHINESE_TEXT_BOLD_TOGGLE(
                index=idx), el_name="Chinese bold toggle.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def chinese_text_toggle_should_be_disabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_disabled(locator=printereditorpage.CHINESE_TEXT_BOLD_TOGGLE(
                index=idx), el_name="Chinese bold toggle.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def english_text_font_size_should_be_enabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_enabled(locator=printereditorpage.ENGLISH_TEXT_FONT_SIZE_SELECT(
                index=idx), el_name="English text font size.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def english_text_font_size_should_be_disabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_disabled(locator=printereditorpage.ENGLISH_TEXT_FONT_SIZE_SELECT(
                index=idx), el_name="English text font size.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def english_text_checkbox_should_be_enabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_enabled(locator=printereditorpage.ENGLISH_TEXT_CHECKBOX(
                index=idx), el_name="English text checkbox.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def english_text_checkbox_should_be_disabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_disabled(locator=printereditorpage.ENGLISH_TEXT_CHECKBOX(
                index=idx), el_name="English text checkbox.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def english_text_toggle_should_be_enabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_enabled(locator=printereditorpage.ENGLISH_TEXT_BOLD_TOGGLE(
                index=idx), el_name="English bold toggle.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def english_text_toggle_should_be_disabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_disabled(locator=printereditorpage.ENGLISH_TEXT_BOLD_TOGGLE(
                index=idx), el_name="English bold toggle.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def english_text_toggle_should_be_selected(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_selected(locator=printereditorpage.ENGLISH_TEXT_BOLD_TOGGLE(
                index=idx), el_name="English bold toggle.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def english_text_toggle_should_not_be_selected(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_not_be_selected(locator=printereditorpage.ENGLISH_TEXT_BOLD_TOGGLE(
                index=idx), el_name="English bold toggle.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def spacing_should_be_enabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_enabled(
                locator=printereditorpage.SPACING_SELECT(index=idx), el_name="Spacing.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def spacing_should_be_disabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_disabled(
                locator=printereditorpage.SPACING_SELECT(index=idx), el_name="Spacing.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def always_print_qty_should_be_enabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_enabled(locator=printereditorpage.ALWAYS_PRINT_QTY_CHECKBOX(
                index=idx), el_name="Always print qty.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def always_print_qty_should_be_disabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_disabled(locator=printereditorpage.ALWAYS_PRINT_QTY_CHECKBOX(
                index=idx), el_name="Always print qty.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def modified_dishes_only_should_be_enabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_enabled(locator=printereditorpage.MODIFIED_DISH_ONLY(
                index=idx), el_name="Modified Dishes Only.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def modified_dishes_only_should_be_disabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_disabled(locator=printereditorpage.MODIFIED_DISH_ONLY(
                index=idx), el_name="Modified Dishes Only.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def line_should_be_enabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_enabled(
                locator=printereditorpage.LINE_SELECT(index=idx), el_name="Line.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def line_should_be_disabled(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_disabled(
                locator=printereditorpage.LINE_SELECT(index=idx), el_name="Line.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    def __element_should_be_enabled(self, locator: str, el_name: str):
        is_enabled = self.web.is_enabled(
            locator=locator, timeout=self.__timeout)
        assert_true(expr=is_enabled, desc=f"{el_name} should be enabled.")

    def __element_should_be_disabled(self, locator: str, el_name: str):
        is_enabled = self.web.is_enabled(
            locator=locator, timeout=self.__timeout)
        assert_false(expr=is_enabled, desc=f"{el_name} should be disabled.")

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def customer_info_text_checkbox_should_be_selected(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_selected(locator=printereditorpage.CUST_INFO_CHECKBOX(
                index=idx), el_name="Customer info text checkbox.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def customer_info_text_checkbox_should_not_be_selected(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_not_be_selected(locator=printereditorpage.CUST_INFO_CHECKBOX(
                index=idx), el_name="Customer info text checkbox.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def chinese_text_checkbox_should_be_selected(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_selected(locator=printereditorpage.CHINESE_TEXT_CHECKBOX(
                index=idx), el_name="Chinese text checkbox.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def chinese_text_checkbox_should_not_be_selected(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_not_be_selected(locator=printereditorpage.CHINESE_TEXT_CHECKBOX(
                index=idx), el_name="Chinese text checkbox.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def english_text_checkbox_should_be_selected(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_selected(locator=printereditorpage.ENGLISH_TEXT_CHECKBOX(
                index=idx), el_name="English text checkbox.")
        except Exception as e:
            raise e
        self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def english_text_checkbox_should_not_be_selected(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_not_be_selected(locator=printereditorpage.ENGLISH_TEXT_CHECKBOX(
                index=idx), el_name="English text checkbox.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def always_print_qty_checkbox_should_be_selected(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_selected(locator=printereditorpage.ALWAYS_PRINT_QTY_CHECKBOX(
                index=idx), el_name="Always print qty checkbox.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def always_print_qty_checkbox_should_not_be_selected(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_not_be_selected(locator=printereditorpage.ALWAYS_PRINT_QTY_CHECKBOX(
                index=idx), el_name="Always print qty checkbox.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def modified_dishes_only_checkbox_should_be_selected(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_selected(locator=printereditorpage.MODIFIED_DISH_ONLY(
                index=idx), el_name="Modified dishes only checkbox.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def modified_dishes_only_checkbox_should_not_be_selected(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_not_be_selected(locator=printereditorpage.MODIFIED_DISH_ONLY(
                index=idx), el_name="Modified dishes only checkbox.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def cc_void_receipt_checkbox_should_be_selected(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_be_selected(locator=printereditorpage.CC_VOID_RECEIPT_CHECKBOX(
                index=idx), el_name="CC Void receipt checkbox.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def cc_void_receipt_checkbox_should_not_be_selected(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__element_should_not_be_selected(locator=printereditorpage.CC_VOID_RECEIPT_CHECKBOX(
                index=idx), el_name="CC Void receipt checkbox.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    def __element_should_be_selected(self, locator: str, el_name: str):
        is_selected = self.web.is_selected(locator=locator)
        assert_true(expr=is_selected,
                    desc=f"{el_name} should be selected.")

    def __element_should_not_be_selected(self, locator: str, el_name: str):
        is_selected = self.web.is_selected(locator=locator)
        assert_false(expr=is_selected,
                     desc=f"{el_name} should NOT be selected.")

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def printer_editor_error_messages_should_be(self, pid: str, pid_err_msg: str = None, name_err_msg: str = None, mask_err_msg: str = None,
                                                mask_rule_err_msg: str = None, order_receipt_tpl_err: str = None,
                                                host_err_msg: str = None, model_err_msg: str = None, printer_port_err_msg: str = None,
                                                status_port_err_msg: str = None):

        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            sa = SoftAssert()

            if pid_err_msg is not None:
                sa.assert_equal(actual=self.web.get_text(locator=printereditorpage.PID_ERR_MSG(
                    index=idx), normalize=True), exp=pid_err_msg, desc="PID error msg.")

            if name_err_msg is not None:
                sa.assert_equal(actual=self.web.get_text(locator=printereditorpage.NAME_ERR_MSG(
                    index=idx), normalize=True), exp=name_err_msg, desc="Name error message.")

            if mask_err_msg is not None:
                sa.assert_equal(actual=self.web.get_text(locator=printereditorpage.MASK_ERR_MSG(
                    index=idx), normalize=True), exp=mask_err_msg, desc="Mask error message.")

            if mask_rule_err_msg is not None:
                sa.assert_equal(actual=self.web.get_text(locator=printereditorpage.MASK_RULE_ERR_MSG(
                    index=idx), normalize=True), exp=mask_rule_err_msg, desc="Mask rule error message.")

            if order_receipt_tpl_err is not None:
                sa.assert_equal(actual=self.web.get_text(locator=printereditorpage.ORDER_RECEIPT_ERR_MSG(
                    index=idx), normalize=True), exp=order_receipt_tpl_err, desc="Order receipt error message.")

            if self.web.is_selected(locator=printereditorpage.NUCLESS_TOGGLE):
                self.web.scroll_into_view(
                    locator=printereditorpage.NUCLESS_HOST(index=idx))
                self.web.scroll_into_view(
                    locator=printereditorpage.PID(index=idx))

                if host_err_msg is not None:
                    sa.assert_equal(actual=self.web.get_text(locator=printereditorpage.NUCLESS_HOST_ERR_MSG(
                        index=idx), normalize=True), exp=host_err_msg, desc="Host error message.")

                if model_err_msg is not None:
                    sa.assert_equal(actual=self.web.get_text(locator=printereditorpage.MODEL_ERR_MSG(
                        index=idx), normalize=True), exp=model_err_msg, desc="Model error message.")

                if printer_port_err_msg is not None:
                    sa.assert_equal(actual=self.web.get_text(locator=printereditorpage.NUCLESS_PRINTER_PORT_ERR_MSG(
                        index=idx), normalize=True), exp=printer_port_err_msg, desc="Printer port error message.")

                if status_port_err_msg is not None:
                    sa.assert_equal(actual=self.web.get_text(locator=printereditorpage.NUCLESS_STATUS_PORT_ERR_MSG(
                        index=idx), normalize=True), exp=status_port_err_msg, desc="Status port error message.")

            else:
                self.logger.warn(
                    "Cannot verify nucless details error message because nucless is not enabled.")

            sa.assert_all()
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def printer_editor_page_column_names_should_include(self, *args):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            actual_headers = self.web.get_texts(
                locator=printereditorpage.COLUMN_NAMES, normalize=True)
            assert_that_list_contains_all(
                lst=actual_headers, contents=list(args), desc="Column names.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def printer_editor_page_column_count_should_be(self, count: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            act_count = self.web.count(
                locator=printereditorpage.COLUMN_NAMES)
            assert_equal(actual=str(act_count),
                         exp=count, desc="Column Count.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def nucless_details_column_names_should_include(self, *args):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            count = self.web.count(
                locator=printereditorpage.ALL_DISPLAYED_PIDS)
            sa = SoftAssert()
            for i in range(1, count + 1):
                actual_headers = self.web.get_texts(
                    locator=printereditorpage.NUCLESS_DETAILS_LABELS(index=i), normalize=True)
                assert_that_list_contains_all(
                    lst=actual_headers, contents=list(args), desc="Column names.")

            sa.assert_all()
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def nucless_details_column_count_should_be(self, count: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            count_of_printers = self.web.count(
                locator=printereditorpage.ALL_DISPLAYED_PIDS)
            sa = SoftAssert()
            for i in range(1, count_of_printers + 1):
                self.logger.debug(
                    f"Nucless columns: {self.web.get_texts(locator=printereditorpage.NUCLESS_DETAILS_LABELS(index=i))}")
                act_count = self.web.count(
                    locator=printereditorpage.NUCLESS_DETAILS_LABELS(index=i))
                sa.assert_equal(actual=str(act_count), exp=count,
                                desc="Nucless details Column Count.")
            sa.assert_all()
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords", "For DB Mapping Test Only"))
    def template_settings_should_be_correct(self, pid: str,  db_template_setting: str):
        self.logger.debug(f"Template settings: {db_template_setting}")
        sa = SoftAssert()
        # Verify that template settings are disabled if in the UI if template setting in DB is None
        if db_template_setting is None or db_template_setting == 'None':
            sa.handle(
                func=self.customer_info_text_checkbox_should_be_disabled, pid=pid)
            sa.handle(
                func=self.customer_info_text_font_size_should_be_disabled, pid=pid)
            sa.handle(func=self.chinese_text_checkbox_should_be_disabled, pid=pid)
            sa.handle(
                func=self.chinese_text_font_size_should_be_disabled, pid=pid)
            sa.handle(func=self.chinese_text_toggle_should_be_disabled, pid=pid)
            sa.handle(func=self.english_text_checkbox_should_be_disabled, pid=pid)
            sa.handle(
                func=self.english_text_font_size_should_be_disabled, pid=pid)
            sa.handle(func=self.english_text_toggle_should_be_disabled, pid=pid)
            sa.handle(func=self.spacing_should_be_disabled, pid=pid)
            sa.handle(func=self.always_print_qty_should_be_disabled, pid=pid)
            sa.handle(func=self.modified_dishes_only_should_be_disabled, pid=pid)
            sa.handle(func=self.line_should_be_disabled, pid=pid)
        else:
            # Verify that template settings in UI reflect the template setting in the DB
            db_template_setting: dict = json.loads(db_template_setting)
            # Verify Modified dishes only checkbox
            if self.__is_key_in_dict(data=db_template_setting, key='modifiedDishesOnly'):
                sa.handle(
                    func=self.modified_dishes_only_should_be_enabled, pid=pid)
                if db_template_setting['modifiedDishesOnly']:
                    sa.handle(
                        func=self.modified_dishes_only_checkbox_should_be_selected, pid=pid)
                else:
                    sa.handle(
                        func=self.modified_dishes_only_checkbox_should_not_be_selected, pid=pid)
            else:
                sa.handle(
                    func=self.modified_dishes_only_should_be_disabled, pid=pid)

            # Verify customer info text
            if self.__is_key_in_dict(data=db_template_setting, key='custInfoActive'):
                if db_template_setting['custInfoActive']:
                    sa.handle(
                        func=self.customer_info_text_checkbox_should_be_enabled, pid=pid)
                    sa.handle(
                        func=self.customer_info_text_checkbox_should_be_selected, pid=pid)
                    sa.handle(
                        func=self.customer_info_text_font_size_should_be_enabled, pid=pid)
                    sa.handle(func=self.printer_details_should_be, pid=pid,
                              cx_info_txt_font_size=str(db_template_setting['fontSizeCustInfo']))
                else:
                    sa.handle(
                        func=self.customer_info_text_checkbox_should_not_be_selected, pid=pid)
                    sa.handle(
                        func=self.customer_info_text_font_size_should_be_disabled, pid=pid)
            else:
                sa.handle(
                    func=self.customer_info_text_checkbox_should_be_disabled, pid=pid)
                sa.handle(
                    func=self.customer_info_text_font_size_should_be_disabled, pid=pid)

            # Verify spacing
            sa.handle(
                func=self.spacing_should_be_enabled, pid=pid)
            sa.handle(func=self.printer_details_should_be, pid=pid,
                      spacing=str(db_template_setting['spacingSize']))

            # Verify line
            sa.handle(
                func=self.line_should_be_enabled, pid=pid)
            sa.handle(func=self.printer_details_should_be, pid=pid,
                      line=str(db_template_setting['line']))

            # Verify always print quantity
            sa.handle(
                func=self.always_print_qty_should_be_enabled, pid=pid)
            if db_template_setting['alwaysPrintQty']:
                sa.handle(
                    func=self.always_print_qty_checkbox_should_be_selected, pid=pid)
            else:
                sa.handle(
                    func=self.always_print_qty_checkbox_should_not_be_selected, pid=pid)

            # Verify english text
            sa.handle(
                func=self.english_text_checkbox_should_be_enabled, pid=pid)
            if 'EN' in db_template_setting['languageSetting'].split(','):
                sa.handle(
                    func=self.english_text_checkbox_should_be_selected, pid=pid)
                sa.handle(
                    func=self.english_text_font_size_should_be_enabled, pid=pid)
                sa.handle(
                    func=self.english_text_toggle_should_be_enabled, pid=pid)
                sa.handle(func=self.printer_details_should_be, pid=pid,
                          en_txt_font_size=db_template_setting['fontSizeEn'])

                if db_template_setting['boldEn']:
                    sa.handle(
                        func=self.english_text_toggle_should_be_selected, pid=pid)
                else:
                    sa.handle(
                        func=self.english_text_toggle_should_not_be_selected, pid=pid)
            # Commenting out due to inconsistencies in the application behavior
            # else:
            #     sa.handle(
            #         func=self.english_text_checkbox_should_not_be_selected, pid=pid)
            #     sa.handle(
            #         func=self.english_text_font_size_should_be_disabled, pid=pid)
            #     sa.handle(
            #         func=self.english_text_toggle_should_be_disabled, pid=pid)

            # Verify chinese text
            sa.handle(
                func=self.english_text_checkbox_should_be_enabled, pid=pid)
            if 'CN' in db_template_setting['languageSetting'].split(','):
                sa.handle(
                    func=self.chinese_text_checkbox_should_be_selected, pid=pid)
                sa.handle(
                    func=self.chinese_text_font_size_should_be_enabled, pid=pid)
                sa.handle(
                    func=self.chinese_text_toggle_should_be_enabled, pid=pid)
                sa.handle(func=self.printer_details_should_be, pid=pid,
                          cn_txt_font_size=db_template_setting['fontSizeCn'])

                if db_template_setting['boldCn']:
                    sa.handle(
                        func=self.chinese_text_toggle_should_be_selected, pid=pid)
                else:
                    sa.handle(
                        func=self.chinese_text_toggle_should_not_be_selected, pid=pid)
            else:
                # NOTE: Behavior is different between english and chinese text when checkbox is checked or unchecked
                sa.handle(
                    func=self.chinese_text_checkbox_should_not_be_selected, pid=pid)
                sa.handle(
                    func=self.chinese_text_toggle_should_be_enabled, pid=pid)
                sa.handle(func=self.printer_details_should_be, pid=pid,
                          cn_txt_font_size=db_template_setting['fontSizeCn'])
                sa.handle(
                    func=self.chinese_text_toggle_should_be_enabled, pid=pid)
        sa.assert_all()

    def __is_key_in_dict(self, data: dict, key: str):
        return key in data.keys()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def add_printer_button_should_be_visible(self, enabled: bool = None):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        sa = SoftAssert()
        try:
            sa.assert_true(self.web.is_visible(
                locator=printereditorpage.ADD_PRINTER, timeout=timedelta(seconds=0.1)))

            if enabled is not None:
                if enabled:
                    sa.assert_true(self.web.is_enabled(
                        locator=printereditorpage.ADD_PRINTER, timeout=timedelta(seconds=0.1)))
                else:
                    sa.assert_false(self.web.is_enabled(
                        locator=printereditorpage.ADD_PRINTER, timeout=timedelta(seconds=0.1)))
            sa.assert_all()
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def save_printer_button_should_be_visible(self, enabled: bool = None):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            sa = SoftAssert()
            sa.assert_true(self.web.is_visible(
                locator=printereditorpage.SAVE_BTN, timeout=timedelta(seconds=0.1)))

            if enabled is not None:
                if enabled:
                    sa.assert_true(self.web.is_enabled(
                        locator=printereditorpage.SAVE_BTN, timeout=timedelta(seconds=0.1)))
                else:
                    sa.assert_false(self.web.is_enabled(
                        locator=printereditorpage.SAVE_BTN, timeout=timedelta(seconds=0.1)))
            sa.assert_all()
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def nucless_details_should_not_be_visible(self):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            sa = SoftAssert()
            sa.handle(func=self.__element_should_not_be_selected,
                      locator=printereditorpage.NUCLESS_TOGGLE, el_name="Nucless Toggle")
            sa.assert_equal(actual=self.web.count(locator=printereditorpage.NUCLESS_DETAILS_LABEL),
                            exp=0, desc="Nucless details should not be visible.")
            sa.assert_all()
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ValidationKeywords"))
    def last_updated_time_should_be_visible(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            sa = SoftAssert()
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            date = self.web.get_text(
                locator=printereditorpage.LAST_UPDATED(index=idx))
            sa.assert_that_text_is_not_empty(
                txt=date, desc="Last updated time.")
            sa.assert_that_date_format_is(
                date=date, exp_format="%b %d, %Y %I:%M %p")
            sa.assert_all()
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
