from datetime import timedelta
from autocore.AssertsLibrary import SoftAssert, assert_false
from libraries.dashboard.ClientTechDashboardLibrary.locators import frame, portpane
from robot.api.deco import keyword
from autocore.bases import WebLibraryComponent

class PortPaneKeywords(WebLibraryComponent):
    
    @keyword(tags=("ClientTechDashBoardKeywords", "PortPaneKeywords"))
    def main_port_details_should_be(self, en_name: str, ex_name: str, exp_gateway: str, exp_status: str = None, exp_description: str = None):
        self.web.select_frame(locator=frame.CLIENT_TECH_FRAME)
        try:
            sa = SoftAssert()
            self.web.wait_until_visible(
                locator=portpane.MAIN_RESTAURANT_TPL(en_name=en_name, ex_name=ex_name))
            act_restaurant = self.web.get_text(
                locator=portpane.MAIN_RESTAURANT_TPL(en_name=en_name, ex_name=ex_name))
            sa.assert_equal(actual=act_restaurant,
                            exp=f"{en_name} ({ex_name})", desc="Restaurant.")
            
            if exp_gateway is not None:
                act_gateway = self.web.get_text(locator=portpane.MAIN_GATEWAY_TPL(en_name=en_name, ex_name=ex_name))
                sa.assert_equal(actual=act_gateway, exp=exp_gateway, desc="Gateway.")
                
            if exp_status is not None:
                act_status = self.web.get_text(
                    locator=portpane.MAIN_STATUS_TPL(en_name=en_name, ex_name=ex_name))
                sa.assert_equal(actual=act_status,
                                exp=exp_status, desc="Status.")
                
            if exp_description is not None:
                self.web.wait_until_text_is_not_empty(
                    locator=portpane.MAIN_DESCRIPTION_TPL(en_name=en_name, ex_name=ex_name))
                self.web.wait_until_text_is(locator=portpane.MAIN_DESCRIPTION_TPL(en_name=en_name, ex_name=ex_name), exp_text=exp_description)
                act_desc = self.web.get_text(
                    locator=portpane.MAIN_DESCRIPTION_TPL(en_name=en_name, ex_name=ex_name))
                sa.assert_equal(actual=act_desc, exp=exp_description,
                                desc="Description.")

            act_last_up_time = self.web.get_text(locator=portpane.MAIN_LAST_UP_TIME_TPL(en_name=en_name, ex_name=ex_name))
            sa.assert_that_text_is_not_empty(
                txt=act_last_up_time, desc="Last up time.")
            sa.assert_that_date_format_is(
                date=act_last_up_time, exp_format="%Y-%m-%d %H:%M:%S", desc="Last up time.")
            sa.assert_all()
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
    
    @keyword(tags=("ClientTechDashBoardKeywords", "PortPaneKeywords"))
    def restaurant_should_not_be_visible_in_the_main_port_section(self, en_name: str, ex_name: str):
        self.web.select_frame(locator=frame.CLIENT_TECH_FRAME)
        try:
            self.web.wait_until_not_visible(
                locator=portpane.MAIN_RESTAURANT_TPL(en_name=en_name, ex_name=ex_name))
            is_visible = self.web.is_visible(locator=portpane.MAIN_RESTAURANT_TPL(en_name=en_name, ex_name=ex_name), timeout=timedelta(seconds=0.1))
            assert_false(is_visible, desc=f"Restaurant {en_name} ({ex_name}) should not be visible.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
            
    @keyword(tags=("ClientTechDashBoardKeywords", "PortPaneKeywords"))
    def ack_port_details_should_be(self, en_name: str, ex_name: str, exp_gateway: str, exp_status: str = None, exp_description: str = None):
        self.web.select_frame(locator=frame.CLIENT_TECH_FRAME)
        try:
            sa = SoftAssert()
            self.web.wait_until_visible(
                locator=portpane.ACK_RESTAURANT_TPL(en_name=en_name, ex_name=ex_name))
            act_restaurant = self.web.get_text(
                locator=portpane.ACK_RESTAURANT_TPL(en_name=en_name, ex_name=ex_name))
            sa.assert_equal(actual=act_restaurant,
                            exp=f"{en_name} ({ex_name})", desc="Restaurant.")
            
            if exp_gateway is not None:
                act_gateway = self.web.get_text(locator=portpane.ACK_GATEWAY_TPL(en_name=en_name, ex_name=ex_name))
                sa.assert_equal(actual=act_gateway, exp=exp_gateway, desc="Gateway.")
                
            if exp_status is not None:
                act_status = self.web.get_text(
                    locator=portpane.ACK_STATUS_TPL(en_name=en_name, ex_name=ex_name))
                sa.assert_equal(actual=act_status,
                                exp=exp_status, desc="Status.")
                
            if exp_description is not None:
                self.web.wait_until_text_is_not_empty(
                    locator=portpane.ACK_DESCRIPTION_TPL(en_name=en_name, ex_name=ex_name))
                self.web.wait_until_text_is(locator=portpane.ACK_DESCRIPTION_TPL(en_name=en_name, ex_name=ex_name), exp_text=exp_description)
                act_desc = self.web.get_text(
                    locator=portpane.ACK_DESCRIPTION_TPL(en_name=en_name, ex_name=ex_name))
                sa.assert_equal(actual=act_desc, exp=exp_description,
                                desc="Description.")

            act_last_up_time = self.web.get_text(locator=portpane.ACK_LAST_UP_TIME_TPL(en_name=en_name, ex_name=ex_name))
            sa.assert_that_text_is_not_empty(
                txt=act_last_up_time, desc="Last up time.")
            sa.assert_that_date_format_is(
                date=act_last_up_time, exp_format="%Y-%m-%d %H:%M:%S", desc="Last up time.")
            sa.assert_all()
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
            
    @keyword(tags=("ClientTechDashBoardKeywords", "PortPaneKeywords"))
    def restaurant_should_not_be_visible_in_the_ack_port_section(self, en_name: str, ex_name: str):
        self.web.select_frame(locator=frame.CLIENT_TECH_FRAME)
        try:
            self.web.wait_until_not_visible(
                locator=portpane.ACK_RESTAURANT_TPL(en_name=en_name, ex_name=ex_name))
            is_visible = self.web.is_visible(locator=portpane.ACK_RESTAURANT_TPL(en_name=en_name, ex_name=ex_name), timeout=timedelta(seconds=0.1))
            assert_false(is_visible, desc=f"Restaurant {en_name} ({ex_name}) should not be visible.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()
            
    @keyword(tags=("ClientTechDashBoardKeywords", "PortPaneKeywords"))
    def click_restaurant_close_btn(self, en_name: str, ex_name: str):
        self.web.select_frame(locator=frame.CLIENT_TECH_FRAME)
        try:
            self.web.wait_until_visible(
                locator=portpane.MAIN_RESTAURANT_TPL(en_name=en_name, ex_name=ex_name))
            self.web.click(
                locator=portpane.MAIN_CLOSE_BTN_TPL(en_name=en_name, ex_name=ex_name))
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()