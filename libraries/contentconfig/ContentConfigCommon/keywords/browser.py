
from autocore.bases import WebLibraryComponent
from robot.api.deco import keyword

from autocore.web.browserconfig import chrome_options
from libraries.contentconfig.ContentConfigCommon.config import CONTENT_CONFIG_LOGIN_PAGE_URL


def _get_url(env: str):
    env = env.lower().strip()
    url = CONTENT_CONFIG_LOGIN_PAGE_URL.get(env)
    if url is None:
        raise Exception(f'No URL configured for [ {env} ] environment yet.')
    return url


class BrowserKeywords(WebLibraryComponent):

    @keyword(tags=("BrowserKeywords","ContentConfigCommonKeywords"))
    def open_content_config_in_browser(self):
        """Open Content config login page in browser."""
        self.web.open_browser(
            url=_get_url(env=self.globals.env),
            browser='chrome',
            options=chrome_options(is_headless=self.globals.headless, is_incognito=self.globals.incognito),
            alias=None
        )
    
    @keyword(tags=("BrowserKeywords","ContentConfigCommonKeywords"))
    def close_content_config(self):
        """Closes the browser hence closing Content Config."""
        self.web.close_browser()

    @keyword(tags=("BrowserKeywords","ContentConfigCommonKeywords"))
    def reload_content_config(self):
        """Reload the browser. Mimic clicking the reload button of the browser."""
        self.web.reload_browser()