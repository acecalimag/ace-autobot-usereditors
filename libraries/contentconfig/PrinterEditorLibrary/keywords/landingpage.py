from datetime import timedelta
from libraries.contentconfig.PrinterEditorLibrary.locators import iframe, landingpage
from autocore.bases import WebLibraryComponent
from autocore.coreutils import remove_characters
from robot.api.deco import keyword


class LandingPageKeywords(WebLibraryComponent):

    @keyword(tags=("PrinterEditorKeywords", "LandingPageKeywords"))
    def open_restaurant_in_printer_editor(self, en_name: str, ex_name: str):
        ex_name = remove_characters(ex_name, "(", ")")
        restaurant_lable = f"{en_name} ({ex_name})"
        restaurant_locator = landingpage.PE_RESTAURANTS_DD_OPTION_TPL(
            restaurant_lable)

        self.web.select_frame(locator=iframe.PRINTER_EDITOR_IFRAME)
        try:
            self.web.wait_until_visible(
                locator=landingpage.PE_PAGE_TITLE)
            self.__open_dropdown()
            self.web.scroll_into_view(locator=restaurant_locator)
            self.web.click(locator=restaurant_locator)
            self.web.wait_until_text_is(
                locator=landingpage.PE_RESTAURANTS_DD_SELECTED_ITEM, exp_text=restaurant_lable,
                ignore_case=True, ignore_space=True, timeout=timedelta(seconds=10))
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

    def __open_dropdown(self):
        if not self.web.is_visible(locator=landingpage.PE_RESTAURANT_SEARCH_BOX, timeout=timedelta(seconds=2)):
            self.web.click(locator=landingpage.PE_RESTAURANTS_DD)
