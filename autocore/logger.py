import json
from pprint import pformat
from robot.api import logger


class Logger:

    def info(self, msg, html=False, also_console=False):
        logger.info(msg=msg, html=html, also_console=also_console)

    def warn(self, msg, html=False):
        logger.warn(msg=msg, html=html)

    def debug(self, msg, html=False):
        logger.debug(msg=msg, html=html)

    def error(self, msg, html=False):
        logger.error(msg=msg, html=html)
        
    def debug_json(self, data, msg: str = None):
        """Convert the data as json then log it with debug log level."""
        if msg is None:   
            logger.debug("[DEBUG DETAILS]")
        else:
            logger.debug(msg=msg)
        logger.debug(json.dumps(data))
        
    def pretty_debug(self, data, msg: str = None):
        if msg is None:   
            logger.debug("[DEBUG DETAILS]")
        else:
            logger.debug(msg=msg)
        logger.debug(pformat(data))
        
