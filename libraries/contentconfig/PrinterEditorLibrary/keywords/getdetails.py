from datetime import timedelta
from autocore.bases import WebLibraryBase, WebLibraryComponent
from robot.api.deco import keyword
from libraries.contentconfig.PrinterEditorLibrary.dto.printerdetails import PrinterDetails
from libraries.contentconfig.PrinterEditorLibrary.helpers.printerindexfinder import get_index_of_printer
from libraries.contentconfig.PrinterEditorLibrary.locators import iframe, printereditorpage


class GetDetailsKeywords(WebLibraryComponent):
    
    def __init__(self, library: WebLibraryBase, timeout: timedelta = ...):
        super().__init__(library=library, timeout=timeout)
        self.__timeout= timedelta(seconds=0.1)

    @keyword(tags=("PrinterEditorKeywords",))
    def get_printer_details(self, pid: str, incl_dd_options: bool = False, incl_nucless_details: bool = False,
                            incl_err_msgs: bool = False, _: PrinterDetails = None) -> PrinterDetails:
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        self.logger.info(f"***** GETTING DETAILS OF PRINTER WITH PID: {pid} *****")
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)

            details = PrinterDetails(
                is_active_cb_checked=self.web.is_selected(
                    locator=printereditorpage.ACTIVE(index=idx)),
                pid=self.web.get_value(
                    locator=printereditorpage.PID(index=idx)),
                name=self.web.get_value(
                    locator=printereditorpage.NAME(index=idx)),
                mask=self.web.get_value(
                    locator=printereditorpage.MASK(index=idx)),
                selected_mask_rule=self.web.get_text(
                    locator=printereditorpage.SELECTED_MASK_RULE(index=idx)),
                selected_order_receipt_tpl=self.web.get_text(
                    locator=printereditorpage.SELECTED_ORDER_RECEIPT(index=idx)),
                cc_template=self.web.get_text(
                    locator=printereditorpage.SELECTED_CC_TEMPLATE(index=idx)),
                is_cc_void_receipt_cb_checked=self.web.is_selected(
                    locator=printereditorpage.CC_VOID_RECEIPT_CHECKBOX(index=idx)),
                last_updated=self.web.get_text(
                    locator=printereditorpage.LAST_UPDATED(index=idx)),
                last_updated_by=self.web.get_text(
                    locator=printereditorpage.LAST_UPDATED_BY(index=idx))
            )

            details = self.__get_customer_info_text_details(
                details=details, idx=idx)
            details = self.__get_chinese_text_details(details=details, idx=idx)
            details = self.__get_english_text_details(details=details, idx=idx)

            details["is_spacing_enabled"] = self.web.is_enabled(
                locator=printereditorpage.SPACING_SELECT(index=idx), timeout=self.__timeout)
            if details["is_spacing_enabled"]:
                details["spacing"] = self.web.get_first_selected_option(
                    locator=printereditorpage.SPACING_SELECT(index=idx))
            else:
                details["spacing"] = None

            details["is_always_print_qty_cb_enabled"] = self.web.is_enabled(
                locator=printereditorpage.ALWAYS_PRINT_QTY_CHECKBOX(index=idx), timeout=self.__timeout)
            if details["is_always_print_qty_cb_enabled"]:
                details["is_always_print_qty_cb_checked"] = self.web.is_selected(
                    locator=printereditorpage.ALWAYS_PRINT_QTY_CHECKBOX(index=idx))
            else:
                details["is_always_print_qty_cb_checked"] = None

            details["is_modified_dishes_only_cb_enabled"] = self.web.is_enabled(
                locator=printereditorpage.MODIFIED_DISH_ONLY(index=idx), timeout=self.__timeout)
            if details["is_modified_dishes_only_cb_enabled"]:
                details["is_modified_dishes_only_cb_checked"] = self.web.is_selected(
                    locator=printereditorpage.MODIFIED_DISH_ONLY(index=idx))
            else:
                details["is_modified_dishes_only_cb_checked"] = None

            details["is_line_enabled"] = self.web.is_enabled(
                locator=printereditorpage.LINE_SELECT(index=idx), timeout=self.__timeout)
            if details["is_line_enabled"]:
                details["line"] = self.web.get_first_selected_option(
                    locator=printereditorpage.LINE_SELECT(index=idx))
            else:
                details["line"] = None

            if incl_dd_options:
                self.logger.info(f"***** GETTING DROPDOWN OPTIONS OF PRINTER WITH PID: {pid} *****")
                details = self.__get_dropdown_options(details=details, idx=idx)
                
            if incl_nucless_details:
                self.logger.info(f"***** GETTING NUCLESS CONFIG DETAILS OF PRINTER WITH PID: {pid} *****")
                details = self.__get_nucless_details(details=details, idx=idx)
                
            if incl_err_msgs:
                self.logger.info(f"***** GETTING ERROR MESSAGES OF PRINTER WITH PID: {pid} *****")
                details = self.__get_err_msg(details=details, idx=idx)

            self.self.logger.debug_json(data=details)
            self.logger.info(f"***** DONE GETTING DETAILS OF PRINTER WITH PID: {pid} *****")
            return details
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
            
    def __get_err_msg(self, details: PrinterDetails, idx: str) -> PrinterDetails:
        if self.web.is_visible(locator=printereditorpage.PID_ERR_MSG(index=idx), timeout=self.__timeout):
            details["pid_err_msg"] = self.web.get_text(locator=printereditorpage.PID_ERR_MSG(index=idx), normalize=True)
        else:
            details["pid_err_msg"] = None
        
        if self.web.is_visible(locator=printereditorpage.NAME_ERR_MSG(index=idx), timeout=self.__timeout):
            details["name_err_msg"] = self.web.get_text(locator=printereditorpage.NAME_ERR_MSG(index=idx), normalize=True)
        else:
            details["name_err_msg"] = None
            
        if self.web.is_visible(locator=printereditorpage.MASK_ERR_MSG(index=idx), timeout=self.__timeout):
            details["mask_err_msg"] = self.web.get_text(locator=printereditorpage.MASK_ERR_MSG(index=idx), normalize=True)
        else:
            details["mask_err_msg"] = None
            
        if self.web.is_visible(locator=printereditorpage.MASK_RULE_ERR_MSG(index=idx), timeout=self.__timeout):
            details["mask_rule_err_msg"] = self.web.get_text(locator=printereditorpage.MASK_RULE_ERR_MSG(index=idx), normalize=True)
        else:
            details["mask_rule_err_msg"] = None
            
        if self.web.is_visible(locator=printereditorpage.ORDER_RECEIPT_ERR_MSG(index=idx), timeout=self.__timeout):
            details["order_receipt_err_msg"] = self.web.get_text(locator=printereditorpage.ORDER_RECEIPT_ERR_MSG(index=idx), normalize=True)
        else:
            details["order_receipt_err_msg"] = None
            
        if self.web.is_selected(locator=printereditorpage.NUCLESS_TOGGLE):
            self.web.scroll_into_view(locator=printereditorpage.NUCLESS_HOST(index=idx))
            self.web.scroll_into_view(locator=printereditorpage.PID(index=idx))
            if self.web.is_visible(locator=printereditorpage.NUCLESS_HOST_ERR_MSG(index=idx), timeout=self.__timeout):
                details["host_err_msg"] = self.web.get_text(locator=printereditorpage.NUCLESS_HOST_ERR_MSG(index=idx), normalize=True)
            else:
                details["host_err_msg"] = None
 
            if self.web.is_visible(locator=printereditorpage.MODEL_ERR_MSG(index=idx), timeout=self.__timeout):
                details["model_err_msg"] = self.web.get_text(locator=printereditorpage.MODEL_ERR_MSG(index=idx), normalize=True)
            else:
                details["model_err_msg"] = None       

            if self.web.is_visible(locator=printereditorpage.NUCLESS_PRINTER_PORT_ERR_MSG(index=idx), timeout=self.__timeout):
                details["printer_port_err_msg"] = self.web.get_text(locator=printereditorpage.NUCLESS_PRINTER_PORT_ERR_MSG(index=idx), normalize=True)
            else:
                details["printer_port_err_msg"] = None  
                
            if self.web.is_visible(locator=printereditorpage.NUCLESS_STATUS_PORT_ERR_MSG(index=idx), timeout=self.__timeout):
                details["status_port"] = self.web.get_text(locator=printereditorpage.NUCLESS_STATUS_PORT_ERR_MSG(index=idx), normalize=True)
            else:
                details["status_port"] = None
        return details
               
    def __get_nucless_details(self, details: PrinterDetails, idx: str) -> PrinterDetails:
        if self.web.is_selected(locator=printereditorpage.NUCLESS_TOGGLE):
            self.web.scroll_into_view(locator=printereditorpage.NUCLESS_HOST(index=idx))
            self.web.scroll_into_view(locator=printereditorpage.PID(index=idx))
            details["host"] = self.web.get_value(locator=printereditorpage.NUCLESS_HOST(index=idx))
            
            if self.web.is_visible(locator=printereditorpage.SELECTED_MODEL(index=idx), timeout=self.__timeout):
                details["model"] = self.web.get_text(locator=printereditorpage.SELECTED_MODEL(index=idx))
            else:
                details["model"] = self.web.get_text(locator=printereditorpage.MODEL_DROPDOWN(index=idx))
            
            self.web.click(locator=printereditorpage.MODEL_DROPDOWN(index=idx))
            details["model_options"] = self.web.get_texts(locator=printereditorpage.MODEL_OPTIONS(index=idx))
            self.web.click(locator=printereditorpage.MODEL_DROPDOWN(index=idx))
            
            details["printer_port"] = self.web.get_value(locator=printereditorpage.NUCLESS_PRINTER_PORT(index=idx))
            details["status_port"] = self.web.get_value(locator=printereditorpage.NUCLESS_STATUS_PORT(index=idx))
        else:
            self.logger.info("Nucless is not enabled. Cannot get details.")
            
        return details
        
    def __get_dropdown_options(self, details: PrinterDetails, idx: str) -> PrinterDetails:
        self.web.click_js(
            locator=printereditorpage.MASK_RULE_DROPDOWN(index=idx))
        details["mask_rule_options"] = self.web.get_texts(
            locator=printereditorpage.MASK_RULE_OPTIONS(index=idx))
        self.web.click_js(
            locator=printereditorpage.MASK_RULE_DROPDOWN(index=idx))

        self.web.click_js(
            locator=printereditorpage.ORDER_RECEIPT_DROPDOWN(index=idx))
        details["order_receipt_tpl_options"] = self.web.get_texts(
            locator=printereditorpage.ORDER_RECEIPT_OPTIONS(index=idx))
        self.web.click_js(
            locator=printereditorpage.ORDER_RECEIPT_DROPDOWN(index=idx))

        if details["is_line_enabled"]:
            self.web.click_js(
                locator=printereditorpage.LINE_SELECT(index=idx))
            details["line_options"] = self.web.get_all_select_options_values(
                locator=printereditorpage.LINE_SELECT(index=idx))
            self.web.click_js(
                locator=printereditorpage.LINE_SELECT(index=idx))
        else:
            details["line_options"] = []

        self.web.click_js(
            locator=printereditorpage.CC_TEMPLATE_DROPDOWN(index=idx))
        details["cc_template_options"] = self.web.get_texts(
            locator=printereditorpage.CC_TEMPLATE_OPTIONS(index=idx))
        self.web.click_js(
            locator=printereditorpage.CC_TEMPLATE_DROPDOWN(index=idx))
        
        return details



    def __get_customer_info_text_details(self, details: PrinterDetails, idx: str) -> PrinterDetails:
        details["is_cust_info_txt_cb_enabled"] = self.web.is_enabled(
            locator=printereditorpage.CUST_INFO_CHECKBOX(index=idx), timeout=self.__timeout)
        details["is_cust_info_txt_font_size_enabled"] = self.web.is_enabled(
            locator=printereditorpage.CUST_INFO_FONT_SIZE_SELECT(index=idx), timeout=self.__timeout)

        if details["is_cust_info_txt_cb_enabled"]:
            details["is_cust_info_txt_cb_checked"] = self.web.is_selected(
                locator=printereditorpage.CUST_INFO_CHECKBOX(index=idx))
        else:
            details["is_cust_info_txt_cb_checked"] = None

        if details["is_cust_info_txt_font_size_enabled"] and details["is_cust_info_txt_cb_checked"]:
            details["cust_info_txt_font_size"] = self.web.get_first_selected_option(
                locator=printereditorpage.CUST_INFO_FONT_SIZE_SELECT(index=idx))
        else:
            details["cust_info_txt_font_size"] = None
        return details

    def __get_chinese_text_details(self, details: PrinterDetails, idx: str) -> PrinterDetails:
        details["is_cn_txt_cb_enabled"] = self.web.is_enabled(
            locator=printereditorpage.CHINESE_TEXT_CHECKBOX(index=idx), timeout=self.__timeout)
        details["is_cn_txt_font_size_enabled"] = self.web.is_enabled(
            locator=printereditorpage.CUST_INFO_FONT_SIZE_SELECT(index=idx), timeout=self.__timeout)
        details["is_cn_txt_toggle_enabled"] = self.web.is_enabled(
            locator=printereditorpage.CHINESE_TEXT_BOLD_TOGGLE(index=idx), timeout=self.__timeout)

        # NOTE: Minor incosistency between chinese text details and english text details.
        #       If Chinese text checkbox is not checked, font size is still displayed while when English text checkbox is not checked
        #       the english font size is hidden.
        if details["is_cn_txt_cb_enabled"]:
            details["is_cn_txt_cb_checked"] = self.web.is_selected(
                locator=printereditorpage.CHINESE_TEXT_CHECKBOX(index=idx))
            details["is_cn_txt_toggle_on"] = self.web.is_selected(
                locator=printereditorpage.CHINESE_TEXT_BOLD_TOGGLE(index=idx))
            details["cn_txt_font_size"] = self.web.get_first_selected_option(
                locator=printereditorpage.CHINESE_TEXT_FONT_SIZE_SELECT(index=idx))
        else:
            details["is_cn_txt_cb_checked"] = None
            details["is_cn_txt_toggle_on"] = None
            details["cn_txt_font_size"] = None

        return details

    def __get_english_text_details(self, details: PrinterDetails, idx: str) -> PrinterDetails:
        details["is_en_txt_cb_enabled"] = self.web.is_enabled(
            locator=printereditorpage.ENGLISH_TEXT_CHECKBOX(index=idx), timeout=self.__timeout)
        details["is_en_txt_font_size_enabled"] = self.web.is_enabled(
            locator=printereditorpage.ENGLISH_TEXT_FONT_SIZE_SELECT(index=idx), timeout=self.__timeout)
        details["is_en_txt_toggle_enabled"] = self.web.is_enabled(
            locator=printereditorpage.ENGLISH_TEXT_BOLD_TOGGLE(index=idx), timeout=self.__timeout)

        if details["is_en_txt_cb_enabled"]:
            details["is_en_txt_cb_checked"] = self.web.is_selected(
                locator=printereditorpage.ENGLISH_TEXT_CHECKBOX(index=idx))
        else:
            details["is_en_txt_cb_checked"] = None

        if details["is_en_txt_font_size_enabled"]:
            details["en_txt_font_size"] = self.web.get_first_selected_option(
                locator=printereditorpage.ENGLISH_TEXT_FONT_SIZE_SELECT(index=idx))
        else:
            details["en_txt_font_size"] = None

        if details["is_en_txt_toggle_enabled"]:
            details["is_en_txt_toggle_on"] = self.web.is_selected(
                locator=printereditorpage.ENGLISH_TEXT_BOLD_TOGGLE(index=idx))
        else:
            details["is_en_txt_toggle_on"] = None

        return details
