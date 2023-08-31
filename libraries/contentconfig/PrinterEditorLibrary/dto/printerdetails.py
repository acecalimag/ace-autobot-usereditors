from typing import TypedDict


class PrinterDetails(TypedDict, total=False):
    is_active_cb_checked: bool | None
    pid: str | None
    pid_err_msg: str | None
    name: str | None
    name_err_msg: str | None
    mask: str | None
    mask_err_msg: str | None
    selected_mask_rule: str | None
    mask_rule_options: list[str] | None
    mask_rule_err_msg: str | None
    selected_order_receipt_tpl: str | None
    order_receipt_err_msg: str | None
    order_receipt_tpl_options: list[str] | None
    
    is_cust_info_txt_cb_enabled: bool | None
    is_cust_info_txt_cb_checked: bool | None
    is_cust_info_txt_font_size_enabled: bool | None
    cust_info_txt_font_size: str | None
    
    is_cn_txt_cb_enabled: bool | None
    is_cn_txt_cb_checked: bool | None
    is_cn_txt_font_size_enabled: bool | None
    cn_txt_font_size: str | None
    is_cn_txt_toggle_enabled: bool | None
    is_cn_txt_toggle_on: bool | None
    
    is_en_txt_cb_enabled: bool | None
    is_en_txt_cb_checked: bool | None
    is_en_txt_font_size_enabled: bool | None
    en_txt_font_size: str | None
    is_en_txt_toggle_enabled: bool | None
    is_en_txt_toggle_on: bool | None
    
    is_spacing_enabled: bool | None
    spacing: str | None
    
    is_always_print_qty_cb_enabled: bool | None
    is_always_print_qty_cb_checked: bool | None
    
    is_modified_dishes_only_cb_enabled: bool | None
    is_modified_dishes_only_cb_checked: bool | None
    
    is_line_enabled: bool | None
    line: str | None
    line_options: list[str] | None
    
    cc_template: str | None
    cc_template_options: list[str] | None
    is_cc_void_receipt_cb_checked: bool | None
    last_updated: str | None
    last_updated_by: str | None
    
    host: str | None
    host_err_msg: str | None
    model: str | None
    model_err_msg: str | None
    model_options: list[str] | None
    printer_port: str | None
    printer_port_err_msg: str | None
    status_port: str | None
    status_port_err_msg: str | None
    
    
    
    
    
    