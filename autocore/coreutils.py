from datetime import datetime
import random
import pytz

def normalize_string(txt: str) -> str:
    if "\n" in txt:
        txt = txt.replace("\n", " ")
    if "\xa0" in txt:
        txt = txt.replace("\xa0", " ")

    txt_split = txt.split(" ")
    txt = " ".join([i.replace(" ", "") for i in txt_split if len(i) > 0])
    return txt


def format_phone_number(phone_number: str):
    phone_number = phone_number.replace(" ", "")
    phone_number = "".join([i for i in phone_number if i.isdigit()])
    return f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"


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

def remove_characters(text: str, *args):
    copy = text
    for i in args:
        if i in copy:
            copy = copy.replace(i, "")
    return copy.strip()
    
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
    
def get_est_timestamp_as_list() :
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

def to_bool(var):
    if isinstance(var, bool):
        return var
    if isinstance(var, str):
        var = var.lower().replace(" ","")
        if var == "false" or var == "0":
            return False
        if var == "true" or var == "1":
            return True      

def remove_none_values_from_dict(dictionary):
    return {key: value for key, value in dictionary.items() if value is not None}
