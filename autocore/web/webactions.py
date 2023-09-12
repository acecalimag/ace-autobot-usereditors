import random
import time
import traceback
from datetime import timedelta

from robot.libraries.BuiltIn import RobotNotRunningError
from selenium.common import (ElementClickInterceptedException,
                             ElementNotInteractableException,
                             StaleElementReferenceException, TimeoutException)
from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from SeleniumLibrary import SeleniumLibrary
from SeleniumLibrary.errors import ElementNotFound

from autocore.coreutils import normalize_string
from autocore.logger import Logger


logger = Logger()

def sleep(seconds: float = 0):
    """Pause execution in seconds."""
    logger.debug(f"SLEEP for {seconds}")
    if seconds < 0:
        seconds = 0

    end_time = time.time() + seconds
    while True:
        remaining = end_time - time.time()
        if remaining <= 0:
            break
        time.sleep(min(remaining, 0.01))


def _transform(text: str, remove_case: bool = False, remove_spaces: bool = False, strip: bool = False) -> str:
    """Transform the text by converting to lowercase and/or removing spaces."""
    if remove_case:
        text = text.lower()
    if remove_spaces:
        text = text.replace(" ", "").strip()
    if strip:
        text = text.strip()
    return text


def _get_retry_count(timeout: timedelta) -> int:
    """Return the retry count based on the timeout provided."""
    if timeout is None:
        raise Exception("Timeout can not be None.")

    timeout = timeout.total_seconds()
    if timeout < 1:
        return 1
    elif 1 <= timeout < 5:
        return 5
    elif 5 <= timeout < 10:
        return 10
    elif 10 <= timeout < 20:
        return 20
    elif 20 <= timeout < 30:
        return 30
    elif 30 <= timeout < 60:
        return 60
    elif 60 <= timeout < 120:
        return 120
    elif 120 <= timeout < 240:
        return 240
    elif 240 <= timeout < 480:
        return 480
    else:
        return 600


def _click_number(el: WebElement, number: str):
    """Type the number to the element via keys. Period (.) is in accepted for decimal points."""
    if number == "0":
        el.send_keys(Keys.NUMPAD0)
    elif number == "1":
        el.send_keys(Keys.NUMPAD1)
    elif number == "2":
        el.send_keys(Keys.NUMPAD2)
    elif number == "3":
        el.send_keys(Keys.NUMPAD3)
    elif number == "4":
        el.send_keys(Keys.NUMPAD4)
    elif number == "5":
        el.send_keys(Keys.NUMPAD5)
    elif number == "6":
        el.send_keys(Keys.NUMPAD6)
    elif number == "7":
        el.send_keys(Keys.NUMPAD7)
    elif number == "8":
        el.send_keys(Keys.NUMPAD8)
    elif number == "9":
        el.send_keys(Keys.NUMPAD9)
    elif number == ".":
        el.send_keys(Keys.DECIMAL)


def _random_item(lst, except_for=None):
    if except_for is None:
        return random.choice(lst)
    else:
        rule = random.choice(lst)
        if rule.strip().lower() == except_for.strip().lower():
            i = lst.index(rule)

            if i != 0:
                rule = lst[0]
            elif i != len(lst) - 1:
                rule = lst[-1]

        return rule


class WebActions:

    def __init__(self, ctx: SeleniumLibrary, timeout: timedelta = timedelta(seconds=5)):
        self.__ctx = ctx
        self.__timeout = timeout

    @property
    def se_lib(self):
        return self.__ctx

    def attribute_ends_with(self, locator: str, attribute: str, exp_value: str) -> bool:
        """Returns True if attribute of the element ends with the exp value, otherwise false."""
        return self.get_attribute(locator=locator, attribute=attribute).endswith(exp_value)

    def attribute_contains(self, locator: str, attribute: str, exp_value: str) -> bool:
        """Returns True if attribute of the element contains the exp value, otherwise false."""
        return exp_value in self.get_attribute(locator=locator, attribute=attribute)

    def capture_page_screenshot(self):
        """Capture page screenshot and embed it to the logs."""
        self.__ctx.capture_page_screenshot(filename="EMBED")

    def click_js(self, locator: str):
        self.__force_click_element_via_js_executor(locator=locator)

    def click(self, locator: str, use_js_if_failed: bool = True):
        """Click the element."""
        try:
            self.__exception_handler(func=self.__ctx.click_element, locator=locator)
        except ElementClickInterceptedException as e:
            if  use_js_if_failed:
                self.__force_click_element_via_js_executor(locator=locator)
            else:
                raise e
        except Exception as e:
            if  use_js_if_failed:
                self.__force_click_element_via_js_executor(locator=locator)
            else:
                raise e
                
    def close_browser(self):
        """Close browser."""
        self.__ctx.close_browser()

    def close_all_browsers(self):
        """Close all browsers."""
        self.__ctx.close_all_browsers()

    def count(self, locator: str) -> int:
        """Returns the count of the elements."""
        count = len(self.__exception_handler(func=self.__ctx.find_elements, locator=locator))
        logger.info(f"Count of element located by: {locator} is {count}.")
        return count

    def delete_text_via_keys(self, locator: str):
        """Delete texts using Ctrl + A  Delete ."""
        logger.info(f"Deleting text of element located by '{locator}' via keys")
        element: WebElement = self.__exception_handler(func=self.__ctx.find_element, locator=locator)
        element.send_keys(Keys.CONTROL + "A")
        element.send_keys(Keys.DELETE)

    def deselect_all(self, locator: str):
        """Deselect all selected <select> options."""
        logger.info(f"Unselecting all options on the <select> element located by '{locator}'")
        self.__get_select_element(locator=locator).deselect_all()

    def deselect_by_value(self, locator: str, value: str):
        """Deselect selected <select> option by value."""
        logger.info(f"Unselecting option with value: {value} on the <select> element located by '{locator}'")
        self.__get_select_element(locator=locator).deselect_by_value(value=value)

    def deselect_by_index(self, locator: str, index: str):
        """Deselect selected <select> option by index."""
        logger.info(f"Unselecting option with index: {index} on the <select> element located by '{locator}'")
        self.__get_select_element(locator=locator).deselect_by_index(index=index)

    def double_click(self, locator: str):
        self.__exception_handler(func=self.__ctx.double_click_element, locator=locator)

    def find_elements(self, locator: str):
        return self.__ctx.find_elements(locator)

    def deselect_by_label(self, locator: str, label: str):
        """Deselect selected <select> option by label/visible text."""
        logger.info(f"Unselecting option with label: {label} on the <select> element located by '{locator}'")
        self.__get_select_element(locator=locator).deselect_by_visible_text(text=label)

    def execute_javascript(self, *code: str):
        self.__ctx.execute_javascript(*code)

    def get_attribute(self, locator: str, attribute: str) -> str:
        """Returns the attribute value of the element."""
        return self.__exception_handler(func=self.__ctx.get_element_attribute, locator=locator, attribute=attribute)

    def get_first_selected_option(self, locator: str) -> str:
        """Returns the first selected options of a <select> element."""
        return self.__get_select_element(locator=locator).first_selected_option.get_attribute("value")

    def get_text(self, locator: str, normalize: bool = False) -> str:
        """Returns the text of the element. When using this, make sure that the locator is unique."""
        self.scroll_into_view(locator=locator)
        text = self.__exception_handler(func=self.__ctx.get_text, locator=locator)
        if normalize:
            text = normalize_string(txt=text)
        return text

    def get_texts(self, locator: str, normalize: bool = False) -> list[str]:
        """Returns a list of texts of the element/s."""
        elements = self.__ctx.find_elements(locator=locator)
        if normalize:
            return [normalize_string(self.__exception_handler(func=self.__ctx.get_text, locator=element)) for element in
                    elements]
        else:
            return [self.__exception_handler(func=self.__ctx.get_text, locator=element) for element in elements]

    def get_value(self, locator: str, normalize: bool = False) -> str:
        """Returns the value of the element. When using this, make sure that the locator is unique."""
        value = self.__exception_handler(func=self.__ctx.get_value, locator=locator)
        if normalize:
            value = normalize_string(value)
        return value

    def get_values(self, locator: str, normalize: bool = False) -> list[str]:
        """Returns a list of values of the element/s."""
        elements = self.__ctx.find_elements(locator=locator)
        if normalize:
            return [normalize_string(self.__exception_handler(func=self.__ctx.get_value, locator=element)) for element
                    in elements]
        else:
            return [self.__exception_handler(func=self.__ctx.get_value, locator=element) for element in elements]

    def go_to(self, url: str):
        """Open the url on the current browser window."""
        self.__ctx.go_to(url=url)

    def input_text(self, locator: str, text: str, click: bool = True, press_enter: bool = False, clear: bool = True):
        """Input text to the element."""
        if click:
            self.click(locator=locator)

        self.__exception_handler(func=self.__ctx.input_text, locator=locator, text=text, clear=clear)

        if press_enter:
            self.press_enter(locator=locator)

    def input_password(self, locator: str, password: str, click: bool = True, press_enter: bool = False,
                       clear: bool = True):
        """Input password to the element."""
        if click:
            self.click(locator=locator)

        try:
            self.__exception_handler(func=self.__ctx.input_password, locator=locator, password=password, clear=clear)
        except RobotNotRunningError:
            self.__exception_handler(func=self.__ctx.input_text, locator=locator, text=password, clear=clear)
        if press_enter:
            self.press_enter(locator=locator)

    def is_text(self, locator: str, exp_text: str, ignore_case: bool = False, ignore_space: bool = False,
                timeout: timedelta = None) -> bool:
        """Returns True if the element text matches the exp text, otherwise False."""
        if timeout:
            try:
                self.wait_until_text_is(locator=locator, exp_text=exp_text)
            except TimeoutException:
                pass

        act_text = self.get_text(locator=locator)
        exp_text_transformed = _transform(exp_text, ignore_case, ignore_space)
        act_text_transformed = _transform(act_text, ignore_case, ignore_space)
        return exp_text_transformed == act_text_transformed

    def is_text_a_valid_select_option(self, locator: str, text: str) -> bool:
        """Returns True if text is a valid <select> option, otherwise False."""
        return text in self.__get_all_select_options_text(locator=locator)

    def is_value_a_valid_select_option(self, locator: str, value: str) -> bool:
        """Returns True if value is a valid <select> option, otherwise False."""
        return value in self.get_all_select_options_values(locator=locator)

    def is_value(self, locator: str, exp_value: str, ignore_case: bool = False, ignore_space: bool = False) -> bool:
        """Returns True if the element value matches the exp value, otherwise False."""
        act_value = self.get_value(locator=locator)
        exp_value_transformed = _transform(exp_value, ignore_case, ignore_space)
        act_value_transformed = _transform(act_value, ignore_case, ignore_space)
        return exp_value_transformed == act_value_transformed

    def is_visible(self, locator: str, timeout: timedelta = None) -> bool:
        """Returns True if the element is visible, otherwise False."""
        if timeout is None:
            timeout = self.__timeout
        try:
            self.wait_until_visible(locator=locator, timeout=timeout)
            return True
        except Exception:
            return False

    def is_enabled(self, locator: str, timeout: timedelta = None) -> bool:
        """Returns True if the element is enabled, otherwise False."""
        if timeout is None:
            timeout = self.__timeout
        try:
            self.wait_until_enabled(locator=locator, timeout=timeout)
            return True
        except Exception:
            return False

    def is_selected(self, locator: str):
        """Returns True if the element is selected, otherwise False."""
        return self.__exception_handler(func=self.__ctx.find_element, locator=locator).is_selected()   

    def wait_until_element_is_selected(self, locator: str, timeout: timedelta = None):
        if timeout is None:
            timeout = self.__timeout

        retries = _get_retry_count(timeout=timeout)
        delay = timeout.total_seconds() / retries

        while retries > 0:
            if not self.is_selected(locator=locator):
                sleep(delay)
            else:
                break
            retries -= 1

    def wait_until_element_is_not_selected(self, locator: str, timeout: timedelta = None):
        if timeout is None:
            timeout = self.__timeout

        retries = _get_retry_count(timeout=timeout)
        delay = timeout.total_seconds() / retries

        while retries > 0:
            if self.is_selected(locator=locator):
                sleep(delay)
            else:
                break
            retries -= 1


    def open_browser(self, url, browser, options, alias):
        """Creates a new web driver and then open the url on the specified browser."""
        self.__ctx.open_browser(url=url, browser=browser, options=options, alias=alias)

    def press_enter(self, locator: str):
        """Press enter."""
        logger.info(f"Press enter on element located by '{locator}'.")
        element: WebElement = self.__exception_handler(func=self.__ctx.find_element, locator=locator)
        element.send_keys(Keys.ENTER)

    def reload_browser(self):
        """Reload the browser."""
        self.__ctx.reload_page()

    def scroll_into_view(self, locator):
        """Scroll the element into view."""
        logger.info(f"Scroll element located by '{locator}' into view.")
        # self.__exception_handler(func=self.__ctx.scroll_element_into_view, locator=locator)
        try:
            self.__ctx.execute_javascript("arguments[0].scrollIntoView(true);", "ARGUMENTS",
                                          self.__ctx.find_element(locator=locator))
        except StaleElementReferenceException:
            self.__wait_until_element_is_not_stale(locator=locator)
            self.__ctx.execute_javascript("arguments[0].scrollIntoView(true);", "ARGUMENTS",
                                          self.__ctx.find_element(locator=locator))
        except TimeoutException:
            logger.debug(f"Selenium Timeout: {self.__ctx.get_selenium_timeout()}")
            logger.debug(traceback.format_exc())

    def select_frame(self, locator: str):
        """Select the frame/iFrame."""
        self.__exception_handler(func=self.__ctx.select_frame, locator=locator)

    def select_by_label(self, locator: str, label: str):
        """Select <select> element option by label/visible text."""
        logger.info(f"Selecting option with label: {label} on the <select> element located by '{locator}'")
        self.__get_select_element(locator=locator).select_by_visible_text(text=label)

    def select_by_random_value(self, locator: str):
        """Select random <select> element option by value except for the currently selected option. Returns the value of the selected option."""
        current = self.get_first_selected_option(locator=locator)
        options_by_value = self.get_all_select_options_values(locator=locator)
        new = _random_item(options_by_value, except_for=current)
        self.select_by_value(locator=locator, value=new)
        return new

    def select_by_value(self, locator: str, value: str):
        """Select <select> element option by value."""
        logger.info(f"Selecting option with value: {value} on the <select> element located by '{locator}'")
        self.__get_select_element(locator=locator).select_by_value(value=value)

    def select_by_index(self, locator: str, index: str):
        """Select <select> element option by index."""
        logger.info(f"Selecting option with index: {index} on the <select> element located by '{locator}'")
        self.__get_select_element(locator=locator).select_by_index(index=index)

    def type_number(self, locator: str, number: str):
        """Type the number to the element via keys. Period (.) is in accepted for decimal points."""
        logger.info(f"Type number: {number} into element located by '{locator}'")
        element: WebElement = self.__exception_handler(func=self.__ctx.find_element, locator=locator)
        for char in number:
            self.__exception_handler(func=_click_number, el=element, number=char)

    def unselect_frame(self):
        """Unselect the current selected frame/iFrame."""
        logger.info("Unselecting Frame")
        self.__ctx.unselect_frame()

    def wait_until_attribute_value_contains(self, locator: str, attribute: str, exp_value: str,
                                            timeout: timedelta = None) -> str:
        """Wait until the element attribute contains the exp attribute.
        Return the actual value if present,raises TimeoutException otherwise.
        """
        logger.info(
            f"Wait until value of {attribute} attribute of element located by '{locator}' to contain {exp_value}.")
        if timeout is None:
            timeout = self.__timeout

        retries = _get_retry_count(timeout=timeout)
        delay = timeout.total_seconds() / retries
        act_value = self.get_attribute(locator=locator, attribute=attribute)
        present = False

        while not present:
            if retries == 0:
                break
            if exp_value in act_value:
                present = True
                break
            sleep(seconds=delay)
            act_value = self.get_attribute(locator=locator, attribute=attribute)
            retries -= 1

        if not present:
            raise TimeoutException(
                f"Cannot wait until '{attribute}' attribute of element located by '{locator}' to contain {exp_value}. Actual attribute: {act_value}.")

        return act_value

    def wait_until_text_contains(self, locator: str, exp_value: str, timeout: timedelta = None, normalize: bool = False,
                                 ignore_case: bool = False, ignore_space: bool = False) -> str:
        """Wait until the element contains the exp text.
        Return the actual value if present,raises TimeoutException otherwise.
        """
        logger.info(
            f"Wait until element located by '{locator}' to contain {exp_value}.")
        if timeout is None:
            timeout = self.__timeout

        retries = _get_retry_count(timeout=timeout)
        delay = timeout.total_seconds() / retries
        act_text = self.get_text(locator=locator, normalize=normalize)
        present = False

        exp_value_transformed = _transform(exp_value, ignore_case, ignore_space)
        act_value_transformed = _transform(act_text, ignore_case, ignore_space)

        while not present:
            if retries == 0:
                break
            if exp_value_transformed in act_value_transformed:
                present = True
                break
            sleep(seconds=delay)
            act_text = self.get_text(locator=locator, normalize=normalize)
            act_value_transformed = _transform(act_text, ignore_case, ignore_space)
            retries -= 1

        if not present:
            logger.debug(f"TRANSFORMED Expected value: {exp_value_transformed}")
            logger.debug(f"TRANSFORMED Actual value: {exp_value_transformed}")
            raise TimeoutException(
                f"Cannot wait until element located by '{locator}' to contain {exp_value}. Actual text: {act_text}.")

        return act_text

    def wait_until_count_is_greater_than(self, locator: str, count: int, timeout: timedelta = None) -> int:
        """Wait until the element count is greater than the exp count.
         Return the actual count if greater than the exp count,raises TimeoutException otherwise.
         """
        logger.info(f"Wait until count of elements located by '{locator}' to be greater than {count}.")
        if timeout is None:
            timeout = self.__timeout

        retries = _get_retry_count(timeout=timeout)
        logger.debug(f"Timeout: {timeout}")
        logger.debug(f"Retry count: {retries}")
        delay = timeout.total_seconds() / retries
        logger.debug(f"Delay: {delay}")
        act_count = self.count(locator=locator)
        while act_count <= count:
            if retries == 0:
                break

            sleep(seconds=delay)
            act_count = self.count(locator=locator)
            retries -= 1

        if act_count <= count:
            raise TimeoutException(
                f"Cannot wait until count of element located by '{locator}' to be greater than {count}. Actual count: {act_count}.")

        return act_count

    def wait_until_text_is(self, locator: str, exp_text: str, ignore_case: bool = False, ignore_space: bool = False,
                           timeout: timedelta = None) -> str:
        """Wait until the element text is the exp text.
         Return the actual text if present,raises TimeoutException otherwise.
         """
        logger.info(f"Wait until text of element located by '{locator}' to be {exp_text}.")
        if timeout is None:
            timeout = self.__timeout

        retries = _get_retry_count(timeout=timeout)
        delay = timeout.total_seconds() / retries

        exp_text_transformed = _transform(exp_text, ignore_case, ignore_space)

        act_text = self.get_text(locator=locator)
        act_text_transformed = _transform(act_text, ignore_case, ignore_space)

        while exp_text_transformed != act_text_transformed:
            if retries == 0:
                break
            sleep(seconds=delay)
            act_text = self.get_text(locator=locator)
            act_text_transformed = _transform(act_text, ignore_case, ignore_space)
            retries -= 1

        if exp_text_transformed != act_text_transformed:
            raise TimeoutException(
                f"Cannot for the text of element located by '{locator}' to be {exp_text}. Actual text: {act_text}")

        return act_text

    def wait_until_text_is_not_empty(self, locator: str, timeout: timedelta = None) -> str:
        """Wait until the element text is not empty.
         Return the actual text if present,raises TimeoutException otherwise.
         """
        logger.info(f"Wait until text of element located by '{locator}' is not empty.")
        if timeout is None:
            timeout = self.__timeout

        retries = _get_retry_count(timeout=timeout)
        delay = timeout.total_seconds() / retries
        text = self.get_text(locator=locator)

        while (text is None) or (len(text) == 0):
            if retries == 0:
                break
            sleep(delay)
            text = self.get_text(locator=locator)
            retries -= 1

        if (text is None) or (len(text) == 0):
            raise Exception(f"Can't wait for the text of element located by '{locator}' to appear.")

        return text

    def wait_until_found(self, locator: str, timeout: timedelta = None):
        """Wait until element is found."""
        self.__wait_until_element_is_found(locator=locator, timeout=timeout)

    def wait_until_value_is_not_empty(self, locator: str, timeout: timedelta = None) -> str:
        """Wait until the element value is not empty.
           Return the actual value if present,raises TimeoutException otherwise.
           """
        logger.info(f"Wait until value of element located by '{locator}' is not empty.")
        if timeout is None:
            timeout = self.__timeout

        retries = _get_retry_count(timeout=timeout)
        delay = timeout.total_seconds() / retries
        value = self.get_value(locator=locator)
        while (value is None) or (len(value) == 0):
            if retries == 0:
                break
            sleep(delay)
            value = self.get_value(locator=locator)
            retries -= 1

        if (value is None) or (len(value) == 0):
            raise Exception(f"Can't for the value of element located by '{locator}' to appear.")

        return value

    def wait_until_value_is(self, locator: str, exp_value: str, ignore_case: bool = False, ignore_space: bool = False,
                            timeout: timedelta = None) -> str:
        """Wait until the element value is the exp value.
            Return the actual value if present,raises TimeoutException otherwise.
            """
        logger.info(f"Wait until value of element located by '{locator}' is {exp_value}.")
        if timeout is None:
            timeout = self.__timeout

        retries = _get_retry_count(timeout=timeout)
        delay = timeout.total_seconds() / retries

        exp_value_transformed = _transform(exp_value, ignore_case, ignore_space)

        act_value = self.get_value(locator=locator)
        act_value_transformed = _transform(act_value, ignore_case, ignore_space)

        while exp_value_transformed != act_value_transformed:
            if retries == 0:
                break
            sleep(seconds=delay)
            act_value = self.get_value(locator=locator)
            act_value_transformed = _transform(act_value, ignore_case, ignore_space)
            retries -= 1

        if exp_value_transformed != act_value_transformed:
            raise TimeoutException(
                f"Cannot wait for the value of element located by '{locator}' to be {exp_value}. Actual value: {act_value}.")

        return act_value

    def wait_until_visible(self, locator: str, timeout: timedelta = None):
        """Waits until element is visible."""
        logger.info(f"Wait until element located by '{locator}' is visible.")
        if timeout is None:
            timeout = self.__timeout
        self.__exception_handler(func=self.__ctx.wait_until_element_is_visible, locator=locator, timeout=timeout)

    def wait_until_interactible(self, locator: str, timeout: timedelta = None):
        """Wait until element is interactible."""
        logger.info(f"Wait until element located by '{locator}' is interactible.")
        if timeout is None:
            timeout = self.__timeout
        self.__exception_handler(func=self.__wait_until_element_is_interactible, locator=locator, timeout=timeout)

    def wait_until_not_visible(self, locator: str, timeout: timedelta = None):
        """Wait until element is not visible."""
        logger.info(f"Wait until element located by '{locator}' is not visible.")
        if timeout is None:
            timeout = self.__timeout
        self.__exception_handler(func=self.__ctx.wait_until_element_is_not_visible, locator=locator, timeout=timeout)
        # self.__wait_until_element_is_not_visible(locator=locator, timeout=timeout)

    def wait_until_enabled(self, locator: str, timeout: timedelta = None):
        """Waits until element is enabled."""
        logger.info(f"Wait until element located by '{locator}' is enabled.")
        if timeout is None:
            timeout = self.__timeout
        self.__exception_handler(func=self.__ctx.wait_until_element_is_enabled, locator=locator, timeout=timeout)

    def switch_to_default_content(self):
        """Switch to default content."""
        self.__ctx.driver.switch_to.default_content()

    def __get_select_element(self, locator: str) -> Select:
        element = self.__exception_handler(func=self.__ctx.find_element, locator=locator)
        return Select(webelement=element)

    def __exception_handler(self, func, *args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ElementNotFound as e:
            logger.info(f"Exception encountered: {str(e)}")
            self.__wait_until_element_is_found(locator=kwargs.get("locator"), timeout=kwargs.get("timeout"))
            return func(*args, **kwargs)
        except ElementNotInteractableException as e:
            logger.info(f"Exception encountered: {str(e)}")
            self.__wait_until_element_is_interactible(locator=kwargs.get("locator"), timeout=kwargs.get("timeout"))
            return func(*args, **kwargs)
        except StaleElementReferenceException as e:
            logger.info(f"Exception encountered: {str(e)}")
            self.__wait_until_element_is_not_stale(locator=kwargs.get("locator"), timeout=kwargs.get("timeout"))
            return func(*args, **kwargs)

    def __wait_until_element_is_found(self, locator: str, timeout: timedelta = None):
        if timeout is None:
            timeout = self.__timeout

        retries = _get_retry_count(timeout=timeout)
        delay = timeout.total_seconds() / retries
        elements = self.__ctx.find_elements(locator=locator)

        while len(elements) == 0:
            sleep(delay)
            elements = self.__ctx.find_elements(locator=locator)

            if retries == 0:
                break
            retries -= 1

        if len(elements) == 0:
            raise ElementNotFound(f"Element with locator '{locator}' not found.")
        
    def __wait_until_element_is_interactible(self, locator: str, timeout: timedelta = None):
        if timeout is None:
            timeout = self.__timeout

        retries = _get_retry_count(timeout=timeout)
        delay = timeout.total_seconds() / retries
        interactible = False

        while retries > 0:
            try:
                self.__ctx.get_text(locator=locator)
                self.__ctx.get_value(locator=locator)
                interactible = True
                break
            except ElementNotInteractableException:
                sleep(delay)
            except ElementClickInterceptedException:
                sleep(delay)
            retries -= 1

        if not interactible:
            raise ElementNotInteractableException(f"Element located by '{locator}' is not interactible.")

    def __wait_until_element_is_not_stale(self, locator: str, timeout: timedelta = None):
        if timeout is None:
            timeout = self.__timeout

        retries = _get_retry_count(timeout=timeout)
        delay = timeout.total_seconds() / retries
        stale = True

        while retries > 0:
            try:
                self.__ctx.get_text(locator)
                self.__ctx.get_value(locator)
                stale = False
                break
            except StaleElementReferenceException:
                sleep(delay)
            retries -= 1

        if stale:
            raise StaleElementReferenceException(f"Element located by '{locator}' is stale.")
        
    def __wait_until_element_is_not_visible(self, locator: str, timeout: timedelta = None):
        if timeout is None:
            timeout = self.__timeout

        logger.info(f"Timeout: {timeout.total_seconds()}")
        retries = _get_retry_count(timeout=timeout)
        logger.info(f"Retries: {retries}")
        delay = timeout.total_seconds() / retries
        logger.info(f"Delay: {delay}")
        visible = True

        while retries > 0:
            logger.info(f"Remaining retry: {retries}")
            try:
                self.__ctx.wait_until_element_is_not_visible(locator=locator, timeout=delay)
                visible = False
                break
            except Exception:
                pass
            retries -= 1

        if visible:
            raise Exception(f"Element located by '{locator}' is still visible after {timeout} seconds.")

    def __force_click_element_via_js_executor(self, locator: str):
        try:
            self.__ctx.execute_javascript("arguments[0].click()", "ARGUMENTS", self.__ctx.find_element(locator=locator))
        except TimeoutException:
            logger.debug(f"Selenium Timeout: {self.__ctx.get_selenium_timeout()}")
            logger.debug(traceback.format_exc())

    def __get_all_select_options_text(self, locator: str) -> list[str]:
        """Returns a list of the options visible text."""
        return [el.text for el in self.__get_select_element(locator=locator).options]

    def get_selected_select_option_text(self, locator: str) -> list[str]:
        return [el.text for el in self.__get_select_element(locator=locator).all_selected_options]

    def get_all_select_options_values(self, locator: str) -> list[str]:
        """Returns a list of the options values."""
        return [el.get_attribute("value") for el in self.__get_select_element(locator=locator).options]

    def __get_selected_select_option_value(self, locator: str) -> list[str]:
        return [el.get_attribute("value") for el in self.__get_select_element(locator=locator).all_selected_options]
