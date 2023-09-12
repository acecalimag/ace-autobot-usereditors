from datetime import timedelta

from SeleniumLibrary import SeleniumLibrary
from robot.api import logger
from robot.api.deco import keyword
from robotlibcore import DynamicCore
from autocore import UtilLibrary, dbcreds, envlabels
from autocore.apibaseurl import get_base_url

from autocore.robothelper import set_log_level
from autocore.api.apirequest import APICore
from autocore.db.database import Database
from autocore.globals import Globals
from autocore.logger import Logger
from autocore.web.browserconfig import chrome_options
from autocore.web.webactions import WebActions
import autocore.AssertsLibrary as AssertsLibrary

class LibraryBase(DynamicCore):
    def __init__(self):
        DynamicCore.__init__(self, library_components=[])
        self.__globals: Globals = Globals()
        self.__logger = Logger()
        self.__asserts = AssertsLibrary
        self.__utils = UtilLibrary
        if self.__globals.log_level is not None:
            set_log_level(level=self.__globals.log_level)

    @property
    def globals(self) -> Globals:
        return self.__globals

    @property
    def logger(self) -> Logger:
        return self.__logger

    @property
    def asserts(self) -> AssertsLibrary:
        return self.__asserts
    
    @property
    def utils(self) -> UtilLibrary:
        return self.__utils


class LibraryComponentBase:

    def __init__(self, library: LibraryBase):
        self.__library = library

    @property
    def globals(self) -> Globals:
        return self.__library.globals

    @property
    def logger(self) -> Logger:
        return self.__library.logger

    @property
    def asserts(self) -> AssertsLibrary:
        return self.__library.asserts

    @property
    def utils(self) -> UtilLibrary:
        return self.__library.utils

class WebLibraryBase(LibraryBase):
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        super().__init__()
        self.ROBOT_LIBRARY_LISTENER = self
        self.__selib = SeleniumLibrary(screenshot_root_directory='EMBED')
        self.__chrome_options = chrome_options(is_headless=self.globals.headless, is_incognito=self.globals.incognito)
        
    @property
    def chrome_options(self):
        return self.__chrome_options
    
    def override_selenium_library(self, new_se_lib: SeleniumLibrary):
        self.__selib = new_se_lib

    def create_web_action(self, timeout: timedelta = None) -> WebActions:
        if timeout is not None:
            return WebActions(ctx=self.__selib, timeout=timeout)
        else:
            return WebActions(ctx=self.__selib)

    def _end_keyword(self, name, attributes):
        if attributes['status'] == 'FAIL':
            logger.info("Keyword failed. Taking screenshot at end_keyword.")
            self.__selib.capture_page_screenshot(filename="EMBED")
        elif attributes['status'] == 'PASS':
            if self.globals.ss_after_keyword:
                logger.info("Taking screenshot at end_keyword")
                self.__selib.capture_page_screenshot(filename="EMBED")

    def _start_keyword(self, name, attributes):
        if self.globals.ss_start_keyword:
            logger.info("Taking screenshot at start_keyword")
            self.__selib.capture_page_screenshot(filename="EMBED")


class WebLibraryComponent(LibraryComponentBase):

    def __init__(self, library: WebLibraryBase, timeout: timedelta = timedelta(seconds=5)):
        super().__init__(library)
        self.__web: WebActions = library.create_web_action(timeout=timeout)
        self.__library = library

    @property
    def web(self) -> WebActions:
        return self.__web
    
    @property
    def chrome_options(self):
        return self.__library.chrome_options


class APILibraryBase(LibraryBase):

    def __init__(self):
        super().__init__()
        self.__api = APICore()
        self.__base_url = get_base_url(env=self.globals.env)

    @property
    def api(self) -> APICore:
        return self.__api
    
    @property
    def base_url(self) -> str:
        return self.__base_url


class APILibraryComponent(LibraryComponentBase):

    def __init__(self, library: APILibraryBase):
        super().__init__(library)
        self.__library = library

    @property
    def api(self) -> APICore:
        return self.__library.api
    
    @property
    def base_url(self) -> str:
        return self.__library.base_url
    
def _get_db_creds(env: str):
    if env == envlabels.QA_ENV:
        return dbcreds.QA_DB_CREDS
    elif env == envlabels.STG_ENV:
        return dbcreds.STG_DB_CREDS
    elif env == envlabels.PROD_ENV:
        return dbcreds.PROD_DB_CREDS
    else:
        raise Exception(f"No DB credentials found for [ {env} ] environment.")

class DBLibraryBase(LibraryBase):
    
    def __init__(self, db: str):
        super().__init__()
        self.__db = Database(database=db, **_get_db_creds(self.globals.env))
        
    @property
    def db(self) -> Database:
        return self.__db
    
    @keyword
    def close_database_connections(self):
        self.__db.close_connection()

class DBLibraryComponent(LibraryComponentBase):
    def __init__(self, library: DBLibraryBase):
        super().__init__(library)
        self.__library: DBLibraryBase = library
        
    @property
    def db(self) -> Database:
        return self.__library.db
    
 
    
    