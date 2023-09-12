
from autocore.bases import WebLibraryComponent
from robot.api.deco import keyword
from libraries.userconfig.UserMetaCommon.config import USER_CONFIG_LOGIN_PAGE_URL


def _get_url(env: str):
    env = env.lower().strip()
    url = USER_CONFIG_LOGIN_PAGE_URL.get(env)
    if url is None:
        raise Exception(f'No URL configured for [ {env} ] environment yet.')
    return url


class BrowserKeywords(WebLibraryComponent):

    @keyword(tags=("BrowserKeywords","UserConfigCommonKeywords"))
    def open_user_config_in_browser(self):
        """Open User config login page in browser."""
        self.web.open_browser(
            url=_get_url(env=self.globals.env),
            browser='chrome',
            options=self.chrome_options,
            alias=None
        )
        self.web.se_lib.maximize_browser_window()
    

    @keyword(tags=("BrowserKeywords","UserConfigCommonKeywords"))
    def close_user_config(self):
        """Closes the browser hence closing user config."""
        self.web.close_browser()

    @keyword(tags=("BrowserKeywords","UserConfigCommonKeywords"))
    def reload_user_config(self):
        """Reload the browser. Mimic clicking the reload button of the browser."""
        self.web.reload_browser()