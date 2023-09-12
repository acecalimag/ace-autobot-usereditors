from datetime import timedelta
from robot.api.deco import keyword
from libraries.contentconfig.PrinterEditorLibrary.helpers.printerindexfinder import get_index_of_printer

from libraries.contentconfig.PrinterEditorLibrary.locators import iframe, modal, printereditorpage
from autocore.bases import WebLibraryComponent
from autocore.coreutils import random_item
from autocore.web.webactions import sleep

class ActionKeywords(WebLibraryComponent):
    
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def enable_nucless_in_printer_editor(self):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            self.web.scroll_into_view(locator=printereditorpage.NUCLESS_TOGGLE)
            try_count = 5
                
            while not self.web.is_selected(locator=printereditorpage.NUCLESS_TOGGLE):
                if try_count == 0:
                    break
                self.web.click(locator=printereditorpage.NUCLESS_TOGGLE)
                sleep(seconds=1)
                self.web.wait_until_element_is_selected(locator=printereditorpage.NUCLESS_TOGGLE, timeout=timedelta(seconds=1))
                try_count -= 1

        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame() 
    
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def disable_nucless_in_printer_editor(self):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            self.web.scroll_into_view(locator=printereditorpage.NUCLESS_TOGGLE)
            if self.web.is_selected(locator=printereditorpage.NUCLESS_TOGGLE):
                self.web.click(locator=printereditorpage.NUCLESS_TOGGLE)
                self.web.wait_until_element_is_not_selected(locator=printereditorpage.NUCLESS_TOGGLE)
            else:
                self.logger.info("Nucless is already disabled.")

        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame() 
            
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def check_active_checkbox(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__check_checkbox(pid=pid, locator=printereditorpage.ACTIVE(index=idx), cb_name="Active Check Box")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame() 
         
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def uncheck_active_checkbox(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__uncheck_checkbox(pid=pid, locator=printereditorpage.ACTIVE(index=idx), cb_name="Active Check Box")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame() 
            
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def check_customer_info_text(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__check_checkbox(pid=pid, locator=printereditorpage.CUST_INFO_CHECKBOX(index=idx), cb_name="Customer Info Text Check Box")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame() 
    
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def uncheck_customer_info_text(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__uncheck_checkbox(pid=pid, locator=printereditorpage.CUST_INFO_CHECKBOX(index=idx), cb_name="Customer Info Text Check box")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame() 
            
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def check_chinese_text(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__check_checkbox(pid=pid, locator=printereditorpage.CHINESE_TEXT_CHECKBOX(index=idx), cb_name="Chinese Text Check Box")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame() 
    
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def uncheck_chinese_text(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__uncheck_checkbox(pid=pid, locator=printereditorpage.CHINESE_TEXT_CHECKBOX(index=idx), cb_name="Chinese Text Check box")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame() 
    
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def check_english_text(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__check_checkbox(pid=pid, locator=printereditorpage.ENGLISH_TEXT_CHECKBOX(index=idx), cb_name="English Text Check Box")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame() 
    
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def uncheck_english_text(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__uncheck_checkbox(pid=pid, locator=printereditorpage.ENGLISH_TEXT_CHECKBOX(index=idx), cb_name="English Text Check box")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame() 
        
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def check_always_print_qty(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__check_checkbox(pid=pid, locator=printereditorpage.ALWAYS_PRINT_QTY_CHECKBOX(index=idx), cb_name="Always print quantity Check Box")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame() 
    
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def uncheck_alwasy_print_qty(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__uncheck_checkbox(pid=pid, locator=printereditorpage.ALWAYS_PRINT_QTY_CHECKBOX(index=idx), cb_name="Always print qty Check box")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
            
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def check_modified_dishes_only(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__check_checkbox(pid=pid, locator=printereditorpage.MODIFIED_DISH_ONLY(index=idx), cb_name="Modified dishes only Check Box")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame() 
    
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def uncheck_modified_dishes_only(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__uncheck_checkbox(pid=pid, locator=printereditorpage.MODIFIED_DISH_ONLY(index=idx), cb_name="Modified dishes only Check box")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame() 
            
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def check_cc_void_receipt(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__check_checkbox(pid=pid, locator=printereditorpage.CC_VOID_RECEIPT_CHECKBOX(index=idx), cb_name="CC Void Receipt Check Box")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame() 
    
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def uncheck_cc_void_receipt(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__uncheck_checkbox(pid=pid, locator=printereditorpage.CC_VOID_RECEIPT_CHECKBOX(index=idx), cb_name="CC void receipt Check box")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame() 

    def __check_checkbox(self, pid: str, locator: str, cb_name: str):
        if self.web.is_enabled(locator=locator, timeout=timedelta(seconds=0.1)):
            if not self.web.is_selected(locator=locator):
                self.web.click(locator=locator)
                self.web.wait_until_element_is_selected(locator=locator)
            else:
                self.logger.info(f"Printer {pid} {cb_name} is already checked.")
        else:
            raise Exception(f"Cannot check Printer {pid} {cb_name} because it is disabled.")
        
    def __uncheck_checkbox(self, pid: str, locator: str, cb_name: str):
        if self.web.is_enabled(locator=locator, timeout=timedelta(seconds=0.1)):
            if self.web.is_selected(locator=locator):
                self.web.click(locator=locator)
                self.web.wait_until_element_is_not_selected(locator=locator)
            else:
                self.logger.info(f"Printer {pid} {cb_name} is already NOT checked.")
        else:
            raise Exception(f"Cannot uncheck Printer {pid} {cb_name} because it is disabled.")
        
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def turn_on_chinese_text_bold(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__turn_on_toggle(pid=pid, locator=printereditorpage.CHINESE_TEXT_BOLD_TOGGLE(index=idx), toggle_name="Chinese text bold")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame() 
            
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def turn_off_chinese_text_bold(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__turn_off_toggle(pid=pid, locator=printereditorpage.CHINESE_TEXT_BOLD_TOGGLE(index=idx), toggle_name="Chinese text bold")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def turn_on_english_text_bold(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__turn_on_toggle(pid=pid, locator=printereditorpage.ENGLISH_TEXT_BOLD_TOGGLE(index=idx), toggle_name="English text bold")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame() 
    
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def turn_off_english_text_bold(self, pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(web_action=self.web, pid=pid)
            self.__turn_off_toggle(pid=pid, locator=printereditorpage.ENGLISH_TEXT_BOLD_TOGGLE(index=idx), toggle_name="English text bold")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
            
    def __turn_on_toggle(self, pid: str, locator: str, toggle_name: str):
        if self.web.is_enabled(locator=locator, timeout=timedelta(seconds=0.1)):
            if not self.web.is_selected(locator=locator):
                self.web.click(locator=locator)
                self.web.wait_until_element_is_selected(locator=locator)
            else:
                self.logger.info(f"Printer {pid} {toggle_name} is already ON.")
        else:
            raise Exception(f"Cannot turn on printer {pid} {toggle_name} because it is disabled.")

    def __turn_off_toggle(self, pid: str, locator: str, toggle_name: str):
        if self.web.is_enabled(locator=locator, timeout=timedelta(seconds=0.1)):
            if self.web.is_selected(locator=locator):
                self.web.click(locator=locator)
                self.web.wait_until_element_is_not_selected(locator=locator)
            else:
                self.logger.info(f"Printer {pid} {toggle_name} is already OFF.")
        else:
            raise Exception(f"Cannot turn off printer {pid} {toggle_name} because it is disabled.")
           
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def save_printer_details(self, action: str = 'SAVE'):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            self.web.click(locator=printereditorpage.SAVE_BTN)
            self.web.wait_until_visible(locator=modal.CONFIRM_MODAL)
            
            action = action.strip().upper()
            if action == 'SAVE':
                self.web.click(locator=modal.COMFIRM_MODAL_SAVE_BTN)
                self.web.wait_until_not_visible(locator=modal.CONFIRM_MODAL)
            elif action == "DISCARD":
                self.web.click(locator=modal.COMFIRM_MODAL_DISCARD_BTN)
                self.web.wait_until_not_visible(locator=modal.CONFIRM_MODAL)
            elif action == "NO_ACTION":
                pass
            else:
                raise Exception(f"Action [{action}] is not supported.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
    
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def click_add_printer(self):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            self.web.click(locator=printereditorpage.ADD_PRINTER)
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
    
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def update_pid(self, pid: str, new_pid: str):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            idx = get_index_of_printer(pid=pid, web_action=self.web)
            self.web.input_text(locator=printereditorpage.PID(index=idx), text=new_pid)
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
            
    @keyword(tags=("PrinterEditorKeywords", "ActionKeywords"))
    def fillout_other_printer_details(self, pid: str, name: str = None, mask: str = None, mask_rule: str = None,
                                      order_receipt_tpl: str = None, cx_info_txt_font_size: str = None, ch_text_font_size: str = None,
                                      en_text_font_size: str = None, spacing: str = None, line: str = None, cc_template: str = None,
                                      host: str = None, model: str = None, printer_port: str = None, status_port: str = None, new_printer: bool = False):
        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            if not new_printer:
                idx = get_index_of_printer(pid=pid, web_action=self.web)
            else:
                idx = self.web.count(locator=printereditorpage.ALL_DISPLAYED_PIDS)
                self.web.input_text(locator=printereditorpage.PID(index=idx), text=pid)
            
            if name is not None:
                self.web.input_text(locator=printereditorpage.NAME(index=idx), text=name)
            
            if mask is not None:
                self.web.input_text(locator=printereditorpage.MASK(index=idx), text=mask)
                
            if mask_rule is not None:
                if mask_rule.strip().upper() == 'RANDOM':
                    self.__select_mask_rule(idx=idx, random=True)
                else:
                    self.__select_mask_rule(idx=idx, new_mask_rule=mask_rule)
                    
            if order_receipt_tpl is not None:
                if order_receipt_tpl.strip().upper() == 'RANDOM':
                    self.__select_order_receipt_tpl(idx=idx, random=True)
                else:
                    self.__select_order_receipt_tpl(idx=idx, new_order_receipt_tpl=order_receipt_tpl)

            if cx_info_txt_font_size is not None:
                self.web.select_by_value(locator=printereditorpage.CUST_INFO_FONT_SIZE_SELECT(index=idx), value=cx_info_txt_font_size)
            
            if ch_text_font_size is not None:
                self.web.select_by_value(locator=printereditorpage.CHINESE_TEXT_FONT_SIZE_SELECT(index=idx), value=ch_text_font_size)
            
            if en_text_font_size is not None:
                self.web.select_by_value(locator=printereditorpage.ENGLISH_TEXT_FONT_SIZE_SELECT(index=idx),value=en_text_font_size)

            if spacing is not None:
                self.web.select_by_value(locator=printereditorpage.SPACING_SELECT(index=idx), value=spacing)
            
            if line is not None:
                self.web.select_by_value(locator=printereditorpage.LINE_SELECT(index=idx), value=line)
                
            if cc_template is not None:
                if cc_template == 'RANDOM':
                    self.__select_cc_tpl(idx=idx, random=True)
                else:
                    self.__select_cc_tpl(idx=idx, new_cc_tpl=cc_template)
            
            is_nucless_selected = self.web.is_selected(locator=printereditorpage.NUCLESS_TOGGLE)
            if is_nucless_selected:
                self.web.scroll_into_view(locator=printereditorpage.NUCLESS_HOST(index=idx))
            if host is not None and is_nucless_selected:
                self.web.input_text(locator=printereditorpage.NUCLESS_HOST(index=idx), text=host)
            
            if model is not None and is_nucless_selected:
                if model == 'RANDOM':
                    self.__select_model(idx=idx, random=True)
                else:
                    self.__select_model(idx=idx, new_model=model)
                
            if printer_port is not None and is_nucless_selected:
                self.web.input_text(locator=printereditorpage.NUCLESS_PRINTER_PORT(index=idx), text=printer_port)
            
            if status_port is not None and is_nucless_selected:
                self.web.input_text(locator=printereditorpage.NUCLESS_STATUS_PORT(index=idx), text=status_port)
                
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
        
    def __select_mask_rule(self, idx: str, new_mask_rule: str = None, random: bool = True):
        self.web.click(locator=printereditorpage.MASK_RULE_DROPDOWN(index=idx))
        self.web.wait_until_count_is_greater_than(locator=printereditorpage.MASK_RULE_OPTIONS(index=idx), count=0)
        if random and new_mask_rule is None:  
            current_mask_rule = self.web.get_text(locator=printereditorpage.SELECTED_MASK_RULE(index=idx))
            mask_rules = self.web.get_texts(locator=printereditorpage.MASK_RULE_OPTIONS(index=idx))
            new_mask_rule = random_item(lst=mask_rules, except_for=current_mask_rule)
        
        self.web.scroll_into_view(locator=printereditorpage.MASK_RULE_OPTION(index=idx, mask_rule=new_mask_rule))
        self.web.click(locator=printereditorpage.MASK_RULE_OPTION(index=idx, mask_rule=new_mask_rule))
        
    def __select_order_receipt_tpl(self, idx: str, new_order_receipt_tpl: str = None, random: bool = True):
        self.web.click(locator=printereditorpage.ORDER_RECEIPT_DROPDOWN(index=idx))
        self.web.wait_until_count_is_greater_than(locator=printereditorpage.ORDER_RECEIPT_OPTIONS(index=idx), count=0)
        if random and new_order_receipt_tpl is None:  
            current_order_tpl = self.web.get_text(locator=printereditorpage.SELECTED_ORDER_RECEIPT(index=idx))
            order_tpls = self.web.get_texts(locator=printereditorpage.ORDER_RECEIPT_OPTIONS(index=idx))
            new_order_receipt_tpl = random_item(lst=order_tpls, except_for=current_order_tpl)
        
        self.web.scroll_into_view(locator=printereditorpage.ORDER_RECEIPT_OPTION(index=idx, template=new_order_receipt_tpl))
        self.web.click(locator=printereditorpage.ORDER_RECEIPT_OPTION(index=idx, template=new_order_receipt_tpl))
        
    def __select_cc_tpl(self, idx: str, new_cc_tpl: str = None, random: bool = True):
        self.web.click(locator=printereditorpage.CC_TEMPLATE_DROPDOWN(index=idx))
        self.web.wait_until_count_is_greater_than(locator=printereditorpage.CC_TEMPLATE_OPTIONS(index=idx), count=0)
        if random and new_cc_tpl is None:  
            current_cc_tpl = self.web.get_text(locator=printereditorpage.SELECTED_CC_TEMPLATE(index=idx))
            cc_tpls = self.web.get_texts(locator=printereditorpage.CC_TEMPLATE_OPTIONS(index=idx))
            new_cc_tpl = random_item(lst=cc_tpls, except_for=current_cc_tpl)
        
        self.web.scroll_into_view(locator=printereditorpage.CC_TEMPLATE_OPTION(index=idx, cc_template=new_cc_tpl))
        self.web.click(locator=printereditorpage.CC_TEMPLATE_OPTION(index=idx, cc_template=new_cc_tpl))
            
    def __select_model(self, idx: str, new_model: str = None, random: bool = True):
        self.web.click(locator=printereditorpage.MODEL_DROPDOWN(index=idx))
        self.web.wait_until_count_is_greater_than(locator=printereditorpage.MODEL_OPTIONS(index=idx), count=0)
        models = self.web.get_texts(locator=printereditorpage.MODEL_OPTIONS(index=idx))
        if random and new_model is None:  
            if self.web.is_visible(locator=printereditorpage.SELECTED_MODEL(index=idx), timeout=timedelta(seconds=0.1)):
                current_model = self.web.get_text(locator=printereditorpage.SELECTED_MODEL(index=idx))
                new_model = random_item(lst=models, except_for=current_model)
            else:
                new_model = random_item(lst=models)
        
        self.web.scroll_into_view(locator=printereditorpage.MODEL_OPTION(index=idx, model=new_model))
        self.web.click(locator=printereditorpage.MODEL_OPTION(index=idx, model=new_model))