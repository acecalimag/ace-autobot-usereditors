from autocore.reservedvariables import CREDS_DIR, PABOT, TEST_ENV
from robot.api import logger
from autocore.robothelper import get_variable_value

try:
    import properties
    properties_mod = properties
except Exception:
    properties_mod = None
    
class Globals:
    
    def __init__(self) -> None:
        self.__env = self.__get_env()
        self.__log_level = self.__get_log_level_from_properties()
        self.__creds_dir = self.__get_creds_dir()
        self.__is_pabot_lib_used = self.__get_is_pabotlib_used()
        self.__headless = self.__get_is_headless()
        self.__incognito = self.__get_is_incognito()
        self.__ss_after_keyword = self.__get_ss_after_keyword_from_properties()
        self.__ss_start_keyword = self.__get_ss_start_keyword_from_properties()
        
        
    @property
    def env(self) -> str:
        logger.debug(f"[GLOBALS]: ENV: {self.__env}")
        return self.__env
    
    @property
    def log_level(self) -> str:
        return self.__log_level
    
    @property
    def creds_dir(self) -> str:
        return self.__creds_dir
    
    @property
    def is_pabot_lib_used(self) -> bool:
        return self.__is_pabot_lib_used
    
    @property
    def headless(self) -> bool:
        return self.__headless
    
    @property
    def incognito(self) -> bool:
        return self.__incognito
    
    @property
    def ss_after_keyword(self) -> bool:
        return self.__ss_after_keyword
    
    @property 
    def ss_start_keyword(self) -> bool:
        return self.__ss_start_keyword
    
    def __get_env(self) -> str:
        env: str = get_variable_value(name=TEST_ENV)
        if env is None and properties_mod is not None:
            env = properties_mod.TEST_ENVIRONMENT
    
        if env is None:
            raise Exception(f"No environment was set. Env: {env}")
        
        return env
        
    def __get_log_level_from_properties(self) -> str:
        if properties_mod is not None:
            level = properties_mod.LOG_LEVEL
            if level is not None and len(level) > 0:
                return level
        else:
            logger.info(f"Properties file not found. Log level not set from properties.")  
            return None
        
        
    def __get_creds_dir(self) -> str:
        return get_variable_value(name=CREDS_DIR)

    def __get_is_pabotlib_used(self) -> bool:
        is_pabotlib_used = get_variable_value(name=PABOT)
        if is_pabotlib_used is None:
            is_pabotlib_used = False
        else:
            if is_pabotlib_used.lower().strip() == "true":
                is_pabotlib_used = True
            else:
                is_pabotlib_used = False
        return is_pabotlib_used
    
    def __get_is_headless(self) -> bool:
        if properties_mod is not None:
            return properties_mod.HEADLESS
        else:
            return True   # Default is headless
        
    def __get_is_incognito(self) -> bool: 
        if properties_mod is not None:
            return properties_mod.INCOGNITO
        else:
            return True

    def __get_ss_start_keyword_from_properties(self) -> bool:
        if properties_mod is not None:
            return properties_mod.SS_START_KEYWORD
        else:
            return False
        
    def __get_ss_after_keyword_from_properties(self) -> bool:
        if properties_mod is not None:
            return properties_mod.SS_AFTER_KEYWORD
        else:
            return False
        
