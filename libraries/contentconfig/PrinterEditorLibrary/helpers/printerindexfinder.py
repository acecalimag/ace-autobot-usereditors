from libraries.contentconfig.PrinterEditorLibrary.locators import printereditorpage
from autocore.web.webactions import WebActions
from robot.api import logger


def get_index_of_printer(web_action: WebActions, pid: str) -> str:
    web_action.wait_until_count_is_greater_than(locator=printereditorpage.ALL_DISPLAYED_PIDS, count=0)
    pids = web_action.get_values(printereditorpage.ALL_DISPLAYED_PIDS)

    for index, value in enumerate(pids):
        if value == pid:
            logger.info(
                f"Printer with pid: {pid} found with index of {index + 1}")
            return str(index + 1)

    raise Exception(f"No printer found with pid: {pid}")
