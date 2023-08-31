from typing import Any

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError


def set_test_variable(name, value):
    try:
        BuiltIn().set_test_variable(name, value)
    except RobotNotRunningError as e:
        logger.warn(f"Variable: {name} with value {value} not set as test variable due to {str(e)}.")


def set_suite_variable(name, value):
    try:
        BuiltIn().set_suite_variable(name, value)
    except RobotNotRunningError as e:
        logger.warn(f"Variable: {name} with value {value} not set as test variable due to {str(e)}.")


def get_variable_value(name, default: Any = None):
    try:
        value = BuiltIn().get_variable_value(name=name, default=default)

        return value
    except RobotNotRunningError as e:
        logger.warn(f"Can't get variable with name {name} due to {str(e)}.")
        return default


def set_global_variable(name, value):
    try:
        BuiltIn().set_global_variable(name, value)
    except RobotNotRunningError as e:
        logger.warn(f"Variable: {name} with value {value} not set as test variable due to {str(e)}.")


def skip_test(msg: str = None):
    try:
        if msg is not None:
            BuiltIn().skip(msg=msg)
        else:
            BuiltIn().skip()
    except RobotNotRunningError as e:
        logger.warn(f"Encountered a RobotNotRunningError.")


def set_log_level(level: str):
    try:
        BuiltIn().set_log_level(level=level)
    except RobotNotRunningError as e:
        logger.warn(f"Cannot set log level due to {str(e)}")

def get_library_instance(name: str, all: bool = False):
    try:
        BuiltIn().get_library_instance(name=name, all=all)
    except RobotNotRunningError as e:
        logger.warn(f"Cannot get library instance of {name} due to {str(e)}")