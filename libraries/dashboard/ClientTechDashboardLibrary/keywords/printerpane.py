from datetime import timedelta
from robot.api.deco import keyword
from autocore.AssertsLibrary import SoftAssert, assert_false
from libraries.dashboard.ClientTechDashboardLibrary.locators import frame, printerpane
from autocore.bases import WebLibraryComponent

class PrinterPaneKeywords(WebLibraryComponent):

    @keyword(tags=("ClientTechDashBoardKeywords", "PrinterPaneKeywords"))
    def main_printer_details_should_be(self, printer_name: str, exp_status: str = None, exp_description: str = None):
        self.web.select_frame(locator=frame.CLIENT_TECH_FRAME)
        try:
            sa = SoftAssert()
            self.web.wait_until_visible(
                locator=printerpane.MAIN_PRINTER_TPL(printer=printer_name))
            act_printer = self.web.get_text(
                locator=printerpane.MAIN_PRINTER_TPL(printer=printer_name))
            sa.assert_equal(actual=act_printer,
                            exp=printer_name, desc="Printer.")
            if exp_status is not None:
                act_status = self.web.get_text(
                    locator=printerpane.MAIN_PRINTER_STATUS_TPL(printer=printer_name))
                sa.assert_equal(actual=act_status,
                                exp=exp_status, desc="Printer status.")
            if exp_description is not None:
                self.web.wait_until_text_is_not_empty(
                    locator=printerpane.MAIN_PRINTER_DESCRIPTION_TPL(printer=printer_name))
                self.web.wait_until_text_is(locator=printerpane.MAIN_PRINTER_DESCRIPTION_TPL(
                    printer=printer_name), exp_text=exp_description)
                act_desc = self.web.get_text(
                    locator=printerpane.MAIN_PRINTER_DESCRIPTION_TPL(printer=printer_name))
                sa.assert_equal(actual=act_desc, exp=exp_description,
                                desc="Printer description.")

            act_last_up_time = self.web.get_text(
                locator=printerpane.MAIN_PRINTER_LAST_UP_TIME_TPL(printer=printer_name))
            sa.assert_that_text_is_not_empty(
                txt=act_last_up_time, desc="Last up time.")
            sa.assert_that_date_format_is(
                date=act_last_up_time, exp_format="%Y-%m-%d %H:%M:%S", desc="Last up time.")
            sa.assert_all()
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("ClientTechDashBoardKeywords", "PrinterPaneKeywords"))
    def printer_should_not_be_visible_in_the_main_printer_section(self, printer_name: str):
        self.web.select_frame(locator=frame.CLIENT_TECH_FRAME)
        try:
            self.web.wait_until_not_visible(
                locator=printerpane.MAIN_PRINTER_TPL(printer=printer_name))
            is_visible = self.web.is_visible(locator=printerpane.MAIN_PRINTER_TPL(
                printer=printer_name), timeout=timedelta(seconds=0.1))
            assert_false(
                is_visible, desc=f"Printer {printer_name} should not be visible.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("ClientTechDashBoardKeywords", "PrinterPaneKeywords"))
    def ack_printer_details_should_be(self, printer_name: str, exp_status: str = None, exp_description: str = None):
        self.web.select_frame(locator=frame.CLIENT_TECH_FRAME)
        try:
            sa = SoftAssert()
            self.web.wait_until_visible(
                locator=printerpane.ACK_PRINTER_TPL(printer=printer_name))
            act_printer = self.web.get_text(
                locator=printerpane.ACK_PRINTER_TPL(printer=printer_name))
            sa.assert_equal(actual=act_printer,
                            exp=printer_name, desc="Printer.")
            if exp_status is not None:
                act_status = self.web.get_text(
                    locator=printerpane.ACK_PRINTER_STATUS_TPL(printer=printer_name))
                sa.assert_equal(actual=act_status,
                                exp=exp_status, desc="Printer status.")
            if exp_description is not None:
                act_desc = self.web.get_text(
                    locator=printerpane.ACK_PRINTER_DESCRIPTION_TPL(printer=printer_name))
                sa.assert_equal(actual=act_desc, exp=exp_description,
                                desc="Printer description.")

            act_last_up_time = self.web.get_text(
                locator=printerpane.ACK_PRINTER_LAST_UP_TIME_TPL(printer=printer_name))
            sa.assert_that_text_is_not_empty(
                txt=act_last_up_time, desc="Last up time.")
            sa.assert_that_date_format_is(
                date=act_last_up_time, exp_format="%Y-%m-%d %H:%M:%S", desc="Last up time.")
            sa.assert_all()
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("ClientTechDashBoardKeywords", "PrinterPaneKeywords"))
    def printer_should_not_be_visible_in_the_ack_printer_section(self, printer_name: str):
        self.web.select_frame(locator=frame.CLIENT_TECH_FRAME)
        try:
            self.web.wait_until_not_visible(
                locator=printerpane.ACK_PRINTER_TPL(printer=printer_name))
            is_visible = self.web.is_visible(
                locator=printerpane.ACK_PRINTER_TPL(printer=printer_name), timeout=timedelta(seconds=0.1))
            assert_false(
                is_visible, desc=f"Printer {printer_name} should not be visible.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    @keyword(tags=("ClientTechDashBoardKeywords", "PrinterPaneKeywords"))
    def click_printer_close_btn(self, printer_name: str):
        self.web.select_frame(locator=frame.CLIENT_TECH_FRAME)
        try:
            self.web.wait_until_visible(
                locator=printerpane.MAIN_PRINTER_TPL(printer=printer_name))
            self.web.click(
                locator=printerpane.MAIN_PRINTER_CLOSE_BTN_TPL(printer=printer_name))
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
