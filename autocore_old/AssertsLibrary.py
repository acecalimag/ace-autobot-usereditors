"""
Provides Hard and Soft Assertion capability. Wraps robot.api.logger
"""
from datetime import datetime

from robot.api import logger
from robot.utils import asserts
from robot.api.deco import keyword

ROBOT_AUTO_KEYWORDS = False

def __get_messages(default_success_msg: str, default_error_msg: str, desc: str = None, e_msg: str = None,
                   s_msg: str = None):
    if s_msg is not None:
        success = s_msg
    else:
        success = default_success_msg

    if e_msg is not None:
        error = e_msg
    else:
        error = default_error_msg

    if desc is not None:
        success = f"{desc} {success}"
        error = f"{desc} {error}"

    return success, error


def __process_text(text: str, ignore_case: bool, ignore_space: bool):
    logger.debug(f"Processing text: [ {text} ]. Ignore Case: [ {ignore_case} ]. Ignore Space: [ {ignore_space} ].")
    if ignore_case:
        text = text.lower()
        logger.debug(f"Ignored Cases. Processed Text: [ {text} ]")

    if ignore_space:
        text = text.replace("\xa0", "")
        text = text.replace("\n", "").strip()
        text = text.replace(" ", "").strip()
        logger.debug(f"Ignored Spaces and Line breaks. Processed Text: [ {text} ]")
    return text

@keyword
def assert_that_date_format_is(date: str, exp_format: str, e_msg: str = None, s_msg: str = None, desc: str = None):
    """Fail the test if the ``date`` provided does not match the ``exp_format``."""
    def_err_msg = f"Expecting format of {date} to match format {exp_format} but it did not."
    def_scs_msg = f"Verified that date string {date} match the format {exp_format}."

    success, error = __get_messages(default_success_msg=def_scs_msg, default_error_msg=def_err_msg, e_msg=e_msg,
                                    s_msg=s_msg, desc=desc)
    try:
        datetime.strptime(date, exp_format)
        logger.info(msg=success, also_console=True)
    except Exception:
        raise AssertionError(error)

@keyword
def assert_equal(actual, exp, e_msg: str = None, s_msg: str = None, desc: str = None):
    """Fail if ``actual`` and ``exp`` are unequal as determined by the '==' operator.

    If ``msg`` was provided, this will be the error message in case this keyword failed.

    Examples:
        assert_equal(1,2) -> fail \n
        assert_equal("one","two") -> fail \n
        assert_equal(1,2, "one is not equal to two") -> fail \n
        assert_equal(1,1) -> pass \n
        assert_equal("one","one", "error message if this keyword fails") -> pass
    """
    def_err_msg = f"{actual} is not equal to {exp}."
    def_scs_msg = f"Verified that: {actual} is equal to {exp}."

    success, error = __get_messages(default_success_msg=def_scs_msg, default_error_msg=def_err_msg, e_msg=e_msg,
                                    s_msg=s_msg, desc=desc)

    try:
        asserts.assert_equal(actual, exp)
        logger.info(msg=success, also_console=True)
    except AssertionError:
        raise AssertionError(error)

@keyword
def assert_that_strings_are_equal(actual: str, exp: str, e_msg: str = None, s_msg: str = None, desc: str = None,
                                  ignore_space: bool = False, ignore_case: bool = False):
    def_err_msg = f"{actual} is not equal to {exp}."
    def_scs_msg = f"Verified that: {actual} is equal to {exp}. ignore_space: {ignore_space}, ignore_case: {ignore_case}"

    success, error = __get_messages(default_success_msg=def_scs_msg, default_error_msg=def_err_msg, e_msg=e_msg,
                                    s_msg=s_msg, desc=desc)

    actual = __process_text(text=actual, ignore_case=ignore_case, ignore_space=ignore_space)
    exp = __process_text(text=exp, ignore_case=ignore_case, ignore_space=ignore_space)

    try:
        asserts.assert_equal(actual, exp)
        logger.info(msg=success, also_console=True)
    except AssertionError:
        raise AssertionError(error)

@keyword
def fail(e_msg=None):
    """Fail test immediately with the given message.

    If ``msg`` was provided, this will be the error message.

    Examples:
        fail() -> fail \n
        fail("error message to be displayed") -> fail
    """
    if e_msg is None:
        e_msg = "Fail Test."

    asserts.fail(e_msg)

@keyword
def assert_true(expr, e_msg=None, s_msg: str = None, desc: str = None):
    """Fail the test unless the provided ``expr`` is True.

    If ``msg`` was provided, this will be the error message in case this keyword failed.

    Examples:
        assert_true(1 != 1) -> fail \n
        assert_true([]) -> fail since empty lists are falsy \n
        assert_true("string" == "String", "Custom error message") -> fail \n
        assert_true(1,1) -> pass \n
        assert_true([1,2,3], "Custom error message") -> pass since list with contents are truth
    """
    def_err_msg = "The expression passed as 'expr' is not True."
    def_scs_msg = "Verified that expression passed as 'expr' is True."

    success, error = __get_messages(default_success_msg=def_scs_msg, default_error_msg=def_err_msg, e_msg=e_msg,
                                    s_msg=s_msg, desc=desc)
    try:
        asserts.assert_true(expr)
        logger.info(msg=success, also_console=True)
    except AssertionError:
        raise AssertionError(error)

@keyword
def assert_false(expr, e_msg=None, s_msg: str = None, desc: str = None):
    """Fail the test unless the provided ``expr`` is False.

    If ``msg`` was provided, this will be the error message in case this keyword failed.

    Examples:
        assert_false(1 == 1) -> fail since 1 the expression is True and the method expects False \n
        assert_false(5 > 1, "Customer error message") -> fail \n
        assert_false(False) -> pass
    """
    def_err_msg = "The expression passed as 'expr' is not False."
    def_scs_msg = "Verified that the expression passed as 'expr' is False."

    success, error = __get_messages(default_success_msg=def_scs_msg, default_error_msg=def_err_msg, e_msg=e_msg,
                                    s_msg=s_msg, desc=desc)
    try:
        asserts.assert_false(expr)
        logger.info(msg=success, also_console=True)
    except AssertionError:
        raise AssertionError(error)

@keyword
def assert_that_text_is_not_empty(txt: str, e_msg: str = None, s_msg: str = None, desc: str = None):
    """Fail the test if the given ``txt`` is empty. len(txt) == 0 .

    If ``msg`` was provided, this will be the error message in case this keyword failed.

    Examples:
        assert_that_text_is_not_empty("")  -> fail  \n
        assert_that_text_is_not_empty(" ")  -> pass since string has space  \n
        assert_that_text_is_not_empty("text")  -> pass \n
    """
    def_err_msg = "Provided text is empty."
    def_scs_msg = f"Verified that provided text: {txt} is not empty."

    success, error = __get_messages(default_success_msg=def_scs_msg, default_error_msg=def_err_msg, e_msg=e_msg,
                                    s_msg=s_msg, desc=desc)

    if (txt is None) or len(txt) == 0:
        fail(error)
    else:
        logger.info(msg=success, also_console=True)

@keyword
def assert_that_text_starts_with(txt: str, start: str, e_msg=None, s_msg: str = None, desc: str = None):
    """Fail the test if the given ``txt`` does not start with ``start``. This is case-sensitive.

    If ``msg`` was provided, this will be the error message in case this keyword failed.

    Examples:
        assert_that_text_starts_with("String", "ing") -> fail   \n
        assert_that_text_starts_with("String", "ing", "Custom error message.") -> fail  \n
        assert_that_text_starts_with("String", "str") -> fail since this is case-sensitive  \n
        assert_that_text_starts_with("String", "Str") -> pass
    """
    def_err_msg = f"{txt} does not start with {start}"
    def_scs_msg = f"Verified that: {txt} starts with {start}."

    success, error = __get_messages(default_success_msg=def_scs_msg, default_error_msg=def_err_msg, e_msg=e_msg,
                                    s_msg=s_msg, desc=desc)

    if not txt.startswith(start):
        fail(error)
    else:
        logger.info(msg=success, also_console=True)

@keyword
def assert_that_text_ends_with(txt: str, end: str, e_msg=None, s_msg: str = None, desc: str = None):
    """Fail the test if the given ``txt`` does not end with ``end``. This is case-sensitive.

    If ``msg`` was provided, this will be the error message in case this keyword failed.

    Examples:
        assert_that_text_ends_with("String","rin") -> fail \n
        assert_that_text_ends_with("String","ING","Custom error message") -> fail \n
        assert_that_text_ends_with("String","ing") -> pass
    """
    def_err_msg = f"{txt} does not end with {end}."
    def_scs_msg = f"Verified that: {txt} ends with {end}."

    success, error = __get_messages(default_success_msg=def_scs_msg, default_error_msg=def_err_msg, e_msg=e_msg,
                                    s_msg=s_msg, desc=desc)
    if not txt.endswith(error):
        fail(e_msg)
    else:
        logger.info(msg=success, also_console=True)

@keyword
def assert_that_text_contains(txt: str, content: str, e_msg=None, s_msg: str = None, desc: str = None):
    """Fail the test if the given ``txt`` does not contain ``content``. This is case-sensitive.

    If ``msg`` was provided, this will be the error message in case this keyword failed.

    Examples:
        assert_that_text_contains("String","sng") -> fail \n
        assert_that_text_contains("String,"trg","Custom error message") -> fail \n
        assert_that_text_contains("String","Ing") -> fail since this is case-sensitive  \n
        assert_that_text_contains("String","tri") -> pass
    """
    def_err_msg = f"{txt} does not contain {content}."
    def_scs_msg = f"Verified that: {txt} contains {content}."

    success, error = __get_messages(default_success_msg=def_scs_msg, default_error_msg=def_err_msg, e_msg=e_msg,
                                    s_msg=s_msg, desc=desc)

    if not (content in txt):
        fail(error)
    else:
        logger.info(msg=success, also_console=True)

@keyword
def assert_that_list_is_empty(lst: list, e_msg=None, s_msg: str = None, desc: str = None):
    """Fail the test if the given ``lst`` is not empty. This accepts list of Any type.

    If ``msg`` was provided, this will be the error message in case this keyword failed.

    Examples:
        assert_that_list_is_empty([1,2,3]) -> fail \n
        assert_that_list_is_empty(["one","two","three"], "Custom error message") -> fails \n
        assert_that_list_is_empty([]) -> pass
    """
    def_err_msg = f"List {lst} is not empty."
    def_scs_msg = f"Verified that: list {lst} is empty."
    success, error = __get_messages(default_success_msg=def_scs_msg, default_error_msg=def_err_msg, e_msg=e_msg,
                                    s_msg=s_msg, desc=desc)
    if len(lst) > 0:
        fail(error)
    else:
        logger.info(msg=success, also_console=True)

@keyword
def assert_that_list_is_not_empty(lst: list, e_msg=None, s_msg: str = None, desc: str = None):
    """Fail the test if the given ``lst`` is empty. This accepts list of Any type.

    If ``msg`` was provided, this will be the error message in case this keyword failed.

    Examples:
        assert_that_list_is_not_empty([]) -> fail \n
        assert_that_list_is_not_empty([], "Custom error message") -> fail \n
        assert_that_list_is_not_empty([1,2,3], "Custom error message") -> pass \n
        assert_that_list_is_not_empty(["One","Two","Three"]) -> pass
    """
    def_err_msg = f"List {lst} is empty."
    def_scs_msg = f"Verified that: list {lst} is not empty."

    success, error = __get_messages(default_success_msg=def_scs_msg, default_error_msg=def_err_msg, e_msg=e_msg,
                                    s_msg=s_msg, desc=desc)

    if len(lst) == 0:
        fail(error)
    else:
        logger.info(msg=success, also_console=True)

@keyword
def assert_that_list_has_item(lst: list, content, e_msg=None, s_msg: str = None, desc: str = None):
    """Fail the test if the given ``lst`` does not contain the provided ``content``.

    If ``msg`` was provided, this will be the error message in case this keyword failed.

    Examples:
        assert_that_list_has_item([1,2,4], 3) -> fail since 3 is not in [1,2,4] \n
        assert_that_list_has_item([1,2,4], 3, "Custom Error Message") -> fail \n
        assert_that_list_has_item([1,2,4], 4) -> pass
    """
    def_err_msg = f"List {lst} does not contain {content}."
    def_scs_msg = f"Verified that: list {lst} contains {content}."

    success, error = __get_messages(default_success_msg=def_scs_msg, default_error_msg=def_err_msg, e_msg=e_msg,
                                    s_msg=s_msg, desc=desc)
    if not (content in lst):
        fail(error)
    else:
        logger.info(msg=success, also_console=True)

@keyword
def assert_that_list_does_not_contain(lst: list, item, e_msg=None, s_msg: str = None, desc: str = None):
    """Fail the test if the given ``lst`` contains the provided ``item``.

    If ``msg`` was provided, this will be the error message in case this keyword failed.

    Examples:
        assert_that_list_does_not_contain([1,2,3,4], 2) -> fail since 2 is in the list
        assert_that_list_does_not_contain([1,2,3,4], 10) -> pass since 10 is not in the list.
    """
    def_err_msg = f"List {lst} contains {item}."
    def_scs_msg = f"Verified that list {lst} does not contain {item}."
    success, error = __get_messages(default_success_msg=def_scs_msg, default_error_msg=def_err_msg, e_msg=e_msg,
                                    s_msg=s_msg, desc=desc)
    if item in lst:
        fail(error)
    else:
        logger.info(msg=success, also_console=True)

@keyword
def assert_that_list_contains_all(lst: list, contents: list, e_msg=None, s_msg: str = None, desc: str = None):
    """Fail the test if the given ``lst`` does not contain all ``contents``.

    If ``msg`` was provided, this will be the error message in case this keyword failed.

    Examples:
        assert_that_list_contains_all([1,2,3,4,5], [1,2,7]) -> fail since 7 is not in [1,2,3,4,5]   \n
        assert_that_list_contains_all([1,2,3,4,5],[6,7,8], "Custom error message") -> fail  \n
        assert_that_list_contains_all([1,2,3,4,5],[1,2,3]) -> pass
    """

    missing_items = []

    for i in contents:
        if not (i in lst):
            missing_items.append(i)

    def_err_msg = f"List {lst} does not contain all of {contents}. See missing item/s: {missing_items}."
    def_scs_msg = f"Verified that: list {lst} contains all of {contents}."
    success, error = __get_messages(default_success_msg=def_scs_msg, default_error_msg=def_err_msg, e_msg=e_msg,
                                    s_msg=s_msg, desc=desc)

    if len(missing_items) > 0:
        fail(error)
    else:
        logger.info(msg=success, also_console=True)


class SoftAssert:
    """Provide the capability to perform Soft Assertions. Fail if at least one prior assertions failed.

    NOTE: Always call assert_all() at the end, otherwise failures (if there are) will not be reported resulting
    to a passed test even if it's not.

    Example:
        sa = SoftAssert()   \n
        sa.assert_equal(1,2) -> fail but next assertion will still be executed \n
        sa.assert_equal("one","two") -> fail but next assertion will still be executed \n
        sa.assert_all()
    """

    def __init__(self):
        self.__errors: list[str] = []

    def handle(self, func, *args, **kwargs):
        """Use this to convert hard asserts to soft asserts."""
        try:
            func(*args, **kwargs)
        # except AssertionError as e:
        except Exception as e:
            self.__errors.append(str(e))

    def assert_equal(self, actual, exp, e_msg: str = None, s_msg: str = None, desc: str = None):
        """Fail if ``actual`` and ``exp`` are unequal as determined by the '==' operator.

        If ``msg`` was provided, this will be the error message in case this keyword failed.

        Example:
            sa = SoftAssert() \n
            sa.assert_equal(1,2) -> fail \n
            sa.assert_equal("one","two") -> fail \n
            sa.assert_equal(1,2, "one is not equal to two") -> fail \n
            sa.assert_equal(1,1) -> pass \n
            sa.assert_equal("one","one", "error message if this keyword fails") -> pass \n
            sa.assert_all()
        """
        try:
            assert_equal(actual, exp, e_msg=e_msg, s_msg=s_msg, desc=desc)
        except AssertionError as e:
            self.__errors.append(str(e))

    def assert_that_strings_are_equal(self, actual: str, exp: str, e_msg: str = None, s_msg: str = None,
                                      desc: str = None, ignore_space: bool = False, ignore_case: bool = False):
        try:
            assert_that_strings_are_equal(actual=actual, exp=exp, e_msg=e_msg, s_msg=s_msg, desc=desc,
                                          ignore_space=ignore_space, ignore_case=ignore_case)
        except AssertionError as e:
            self.__errors.append(str(e))

    def assert_true(self, expr, e_msg=None, s_msg: str = None, desc: str = None):
        """Fail the test unless the provided ``expr`` is True.

        If ``msg`` was provided, this will be the error message in case this keyword failed.

        Examples:
            sa = SoftAssert() \n
            sa.assert_true(1 != 1) -> fail \n
            sa.assert_true([]) -> fail since empty lists are falsy \n
            sa.assert_true("string" == "String", "Custom error message") -> fail \n
            sa.assert_true(1,1) -> pass \n
            sa.assert_true([1,2,3], "Custom error message") -> pass since list with contents are truth \n
            sa.assert_all()
        """
        try:
            assert_true(expr, e_msg=e_msg, s_msg=s_msg, desc=desc)
        except AssertionError as e:
            self.__errors.append(str(e))

    def assert_false(self, expr, e_msg=None, s_msg: str = None, desc: str = None):
        """Fail the test unless the provided ``expr`` is False.

        If ``msg`` was provided, this will be the error message in case this keyword failed.

        Examples:
            sa = SoftAssert()   \n
            sa.assert_false(1 == 1) -> fail since 1 the expression is True and the method expects False \n
            sa.assert_false(5 > 1, "Customer error message") -> fail \n
            sa.assert_false(False) -> pass \n
            sa.assert_all()
        """
        try:
            assert_false(expr, e_msg=e_msg, s_msg=s_msg, desc=desc)
        except AssertionError as e:
            self.__errors.append(str(e))

    def assert_that_text_is_not_empty(self, txt: str, e_msg: str = None, s_msg: str = None, desc: str = None):
        """Fail the test if the given ``txt`` is empty. len(txt) == 0 .

        If ``msg`` was provided, this will be the error message in case this keyword failed.

        Examples:
            sa = SoftAssert()   \n
            sa.assert_that_text_is_not_empty("")  -> fail  \n
            sa.assert_that_text_is_not_empty(" ")  -> pass since string has space  \n
            sa.assert_that_text_is_not_empty("text")  -> pass \n
            sa.assert_all()
        """
        try:
            assert_that_text_is_not_empty(txt, e_msg=e_msg, s_msg=s_msg, desc=desc)
        except AssertionError as e:
            self.__errors.append(str(e))

    def assert_that_text_starts_with(self, txt: str, start: str, e_msg=None, s_msg: str = None, desc: str = None):
        """Fail the test if the given ``txt`` does not start with ``start``. This is case-sensitive.

        If ``msg`` was provided, this will be the error message in case this keyword failed.

        Examples:
            sa = SoftAssert()   \n
            sa.assert_that_text_starts_with("String", "ing") -> fail   \n
            sa.assert_that_text_starts_with("String", "ing", "Custom error message.") -> fail  \n
            sa.assert_that_text_starts_with("String", "str") -> fail since this is case-sensitive  \n
            sa.assert_that_text_starts_with("String", "Str") -> pass   \n
            sa.assert_all()
        """
        try:
            assert_that_text_starts_with(txt=txt, start=start, e_msg=e_msg, s_msg=s_msg, desc=desc)
        except AssertionError as e:
            self.__errors.append(str(e))

    def assert_that_text_ends_with(self, txt: str, end: str, e_msg=None, s_msg: str = None, desc: str = None):
        """Fail the test if the given ``txt`` does not end with ``end``. This is case-sensitive.

        If ``msg`` was provided, this will be the error message in case this keyword failed.

        Examples:
            sa = SoftAssert()
            sa.assert_that_text_ends_with("String","rin") -> fail \n
            sa.assert_that_text_ends_with("String","ING","Custom error message") -> fail \n
            sa.assert_that_text_ends_with("String","ing") -> pass \n
            sa.assert_all()
        """
        try:
            assert_that_text_ends_with(txt=txt, end=end, e_msg=e_msg, s_msg=s_msg, desc=desc)
        except AssertionError as e:
            self.__errors.append(str(e))

    def assert_that_text_contains(self, txt: str, content: str, e_msg=None, s_msg: str = None, desc: str = None):
        """Fail the test if the given ``txt`` does not contain ``content``. This is case-sensitive.

        If ``msg`` was provided, this will be the error message in case this keyword failed.

        Examples:
            sa = SoftAssert()   \n
            sa.assert_that_text_contains("String","sng") -> fail \n
            sa.assert_that_text_contains("String,"trg","Custom error message") -> fail \n
            sa.assert_that_text_contains("String","Ing") -> fail since this is case-sensitive  \n
            sa.assert_that_text_contains("String","tri") -> pass    \n
            sa.assert_all()
        """
        try:
            assert_that_text_contains(txt=txt, content=content, e_msg=e_msg, s_msg=s_msg, desc=desc)
        except AssertionError as e:
            self.__errors.append(str(e))

    def assert_that_list_is_empty(self, lst: list, e_msg=None, s_msg: str = None, desc: str = None):
        """Fail the test if the given ``lst`` is not empty. This accepts list of Any type.

        If ``msg`` was provided, this will be the error message in case this keyword failed.

        Examples:
            sa = SoftAssert()   \n
            sa.assert_that_list_is_empty([1,2,3]) -> fail \n
            sa.assert_that_list_is_empty(["one","two","three"], "Custom error message") -> fails \n
            sa.assert_that_list_is_empty([]) -> pass    \n
            sa.assert_all()
        """
        try:
            assert_that_list_is_empty(lst=lst, e_msg=e_msg, s_msg=s_msg, desc=desc)
        except AssertionError as e:
            self.__errors.append(str(e))

    def assert_that_list_is_not_empty(self, lst: list, e_msg=None, s_msg: str = None, desc: str = None):
        """Fail the test if the given ``lst`` is empty. This accepts list of Any type.

        If ``msg`` was provided, this will be the error message in case this keyword failed.

        Examples:
            sa = SoftAssert()   \n
            sa.assert_that_list_is_not_empty([]) -> fail \n
            sa.assert_that_list_is_not_empty([], "Custom error message") -> fail \n
            sa.assert_that_list_is_not_empty([1,2,3], "Custom error message") -> pass \n
            sa.assert_that_list_is_not_empty(["One","Two","Three"]) -> pass \n
            sa.assert_all()
        """
        try:
            assert_that_list_is_not_empty(lst=lst, e_msg=e_msg, s_msg=s_msg, desc=desc)
        except AssertionError as e:
            self.__errors.append(str(e))

    def assert_that_list_has_item(self, lst: list, content, e_msg=None, s_msg: str = None, desc: str = None):
        """Fail the test if the given ``lst`` does not contain the provided ``content``.

        If ``msg`` was provided, this will be the error message in case this keyword failed.

        Examples:
            sa = SoftAssert()   \n
            sa.assert_that_list_has_item([1,2,4], 3) -> fail since 3 is not in [1,2,4] \n
            sa.assert_that_list_has_item([1,2,4], 3, "Custom Error Message") -> fail \n
            sa.assert_that_list_has_item([1,2,4], 4) -> pass    \n
            sa.assert_all()
        """
        try:
            assert_that_list_has_item(lst=lst, content=content, e_msg=e_msg, s_msg=s_msg, desc=desc)
        except AssertionError as e:
            self.__errors.append(str(e))

    def assert_that_list_does_not_contain(self, lst: list, item, e_msg=None, s_msg: str = None, desc: str = None):
        """Fail the test if the given ``lst`` contains the provided ``item``.

        If ``msg`` was provided, this will be the error message in case this keyword failed.

        Examples:
            sa = SoftAssert()   \n
            sa.assert_that_list_does_not_contain([1,2,3,4], 2) -> fail since 2 is in the list
            sa.assert_that_list_does_not_contain([1,2,3,4], 10) -> pass since 10 is not in the list.
            sa.assert_all()
        """
        try:
            assert_that_list_does_not_contain(lst=lst, item=item, e_msg=e_msg, s_msg=s_msg, desc=desc)
        except AssertionError as e:
            self.__errors.append(str(e))

    def assert_that_list_contains_all(self, lst: list, contents: list, e_msg=None, s_msg: str = None, desc: str = None):
        """Fail the test if the given ``lst`` does not contain all ``contents``.

        If ``msg`` was provided, this will be the error message in case this keyword failed.

        Examples:
            sa = SoftAssert()   \n
            sa.assert_that_list_contains_all([1,2,3,4,5], [1,2,7]) -> fail since 7 is not in [1,2,3,4,5]   \n
            sa.assert_that_list_contains_all([1,2,3,4,5],[6,7,8], "Custom error message") -> fail  \n
            sa.assert_that_list_contains_all([1,2,3,4,5],[1,2,3]) -> pass  \n
            sa.assert_all()
        """
        try:
            assert_that_list_contains_all(lst=lst, contents=contents, e_msg=e_msg, s_msg=s_msg, desc=desc)
        except AssertionError as e:
            self.__errors.append(str(e))

    def assert_that_date_format_is(self, date: str, exp_format: str, e_msg=None, s_msg: str = None, desc: str = None):
        """Fail the test if the ``date`` provided does not match the ``exp_format``."""
        try:
            assert_that_date_format_is(date=date, exp_format=exp_format, e_msg=e_msg, s_msg=s_msg, desc=desc)
        except AssertionError as e:
            self.__errors.append(str(e))

    def assert_all(self):
        """Will fail test if at least one of the prior assertions has failed."""
        if len(self.__errors) > 0:
            err_msg = "\n" + "\n".join(self.__errors)
            raise AssertionError(err_msg)
