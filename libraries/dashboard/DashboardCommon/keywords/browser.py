from libraries.dashboard.config import DASHBOARD_LOGIN_PAGE_URL
from autocore.bases import WebLibraryComponent
from autocore.web.browserconfig import chrome_options
from robot.api.deco import keyword

def _get_url(env: str):
    env = env.lower().strip()
    url = DASHBOARD_LOGIN_PAGE_URL.get(env)
    if url is None:
        raise Exception(f'No URL configured for [ {env} ] environment yet.')
    return url
class BrowserKeywords(WebLibraryComponent):

    @keyword(tags=("BrowserKeywords",))
    def open_dashboard_in_browser(self):
        """Open Dashboard login page in browser."""
        self.web.open_browser(
            url=_get_url(env=self.globals.env),
            browser='chrome',
            options=chrome_options(is_headless=self.globals.headless, is_incognito=self.globals.incognito),
            alias=None
        )

    @keyword(tags=("BrowserKeywords",))
    def close_dashboard(self):
        """Closes the browser hence closing Dashboard."""
        self.web.close_browser()

    @keyword(tags=("BrowserKeywords",))
    def reload_dashboard(self):
        """Reload the browser. Mimic clicking the reload button of the browser."""
        self.web.reload_browser()