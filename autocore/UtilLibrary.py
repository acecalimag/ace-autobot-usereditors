from datetime import datetime
import random
import re
import time
import pytz
from robot.api.deco import keyword, not_keyword
from robot.api import logger
ROBOT_AUTO_KEYWORDS = False

@keyword
def convert_est_time_to_a_different_timezone(est_time_str: str, et_zone_offset: str,
                                        est_time_format: str = '%Y-%m-%d %H:%M:%S', target_format: str = '%Y-%m-%d %H:%M:%S') -> str:
    """Convert the time ``est_time`` to a different timezone based on the value of ``et_zone_offset``
    - ``est_time_str`` = The est time to be converted
    - ``et_zone_offset``  = The offset value. 
    Accepted values and their corresponding timezones are:
    ``0`` = America/New_York timezone
    ``-1`` = America/Chicago
    ``-2`` = America/Denver
    ``-3`` = America/Los_Angeles
    - ``est_time_format`` = The date format of the ``est_time_str``
    - ``target_format`` = The date format of the returned time
    """

    timezones = ["America/New_York", "America/Chicago",
                "America/Denver", "America/Los_Angeles"]
    idx = int(et_zone_offset) * -1
    
    est_time = datetime.strptime(est_time_str, est_time_format)

    target_timezone = pytz.timezone(timezones[idx])
    target_time = est_time.astimezone(target_timezone)

    return datetime.strftime(target_time, target_format)

@not_keyword
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
        
@keyword
def convert_datetime_object(datetime_obj: datetime, target_format: str = '%Y-%m-%d %H:%M:%S') -> str:
    return datetime.strftime(datetime_obj, target_format)

@keyword
def convert_datetime_string(input_date_string: str, input_format: str, target_format: str = '%Y-%m-%d %H:%M:%S') -> str:
    # Parse the input date string
    input_datetime = datetime.strptime(input_date_string, input_format)

    # Convert to a new format
    return datetime.strftime(input_datetime, target_format)

@keyword
def get_est_timestamp_as_list():
    est_timezone = pytz.timezone('EST')
    timestamp = datetime.now(est_timezone)
    timestamp_list = [
        timestamp.year,
        timestamp.month,
        timestamp.day,
        timestamp.hour,
        timestamp.minute,
        timestamp.second,
        timestamp.microsecond
    ]
    
    return timestamp_list

@not_keyword
def random_item(lst, except_for=None):
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
    
@keyword
def get_random_whole_number(lower_limit: str = "1", upper_limit: str = "100", as_str: bool = True) -> str | int:
    """Generate a random whole number based on the provided ``lower_limit`` and ``upper_limit``. Upper limit is not included
    in the selection of random number. Decimal values are excluded from the provided ``lower_limit`` and ``upper_limit``.
    """
    if not __is_valid_number(upper_limit) or not __is_valid_number(lower_limit):
        raise Exception(
            "Provided upper_limit or lower_limit is not a valid number.")

    lower_limit = int(__get_whole_number(lower_limit))

    upper_limit = int(__get_whole_number(upper_limit)) - 1

    if lower_limit > upper_limit:
        raise Exception(
            "Upper lower limit must not be greater than the upper limit.")

    number = random.randint(int(lower_limit), int(upper_limit))
    if as_str:
        number = str(number)
    return number

@keyword
def get_random_float_number(lower_limit: str = "0.01", upper_limit: str = "100.00", as_str: bool = True, decimal_count: str = "2") -> str | float:
    """Generate a random float number based on the provided ``lower_limit`` and ``upper_limit``. Upper limit is not included
    in the selection of random number.
    """
    decimal_count = int(decimal_count)
    number = round(random.uniform(float(lower_limit), float(upper_limit)),decimal_count)
    if as_str:
        number = str(number)
    return number

def __is_valid_number(string):
    pattern = r'^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$'
    return bool(re.match(pattern, string))

def __get_whole_number(num_str: str) -> str:
    if "." in num_str:
        num_str = num_str.split(".")[0]
        if len(num_str) == 0:
            num_str = "0"
    return num_str

@not_keyword
def custom_round(value, decimal=2):
    value_str = str(value)
    if "." in value_str:
        whole = value_str.split(".")[0]
        deci_value = value_str.split(".")[1]

        if len(deci_value) < decimal + 1:
            return value
        else:
            round_base = int(deci_value[decimal])
            deci_value = int(deci_value[0:int(decimal)])
            if round_base >= 5:
                deci_value = deci_value + 1
            deci_value = deci_value / 100
            return int(whole) + deci_value

    else:
        return round(value, decimal)
    
@not_keyword
def normalize_string(txt: str) -> str:
    """Removes all leading, trailing spaces,xtra space and non-breaking spaces."""
    if "\n" in txt:
        txt = txt.replace("\n", " ")
    if "\xa0" in txt:
        txt = txt.replace("\xa0", " ")

    txt_split = txt.split(" ")
    txt = " ".join([i.replace(" ", "") for i in txt_split if len(i) > 0])
    return txt

@not_keyword
def format_phone_number(phone_number: str):
    phone_number = phone_number.replace(" ", "")
    phone_number = "".join([i for i in phone_number if i.isdigit()])
    return f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"

@not_keyword
def remove_characters(text: str, *args):
    copy = text
    for i in args:
        if i in copy:
            copy = copy.replace(i, "")
    return copy.strip()