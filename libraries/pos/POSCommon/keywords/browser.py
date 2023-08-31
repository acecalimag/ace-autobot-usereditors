from robot.api.deco import keyword

from autocore.bases import WebLibraryComponent
from libraries.pos.config import POS_LOGIN_PAGE_URL


def _get_url(env: str):
    env = env.lower().strip()
    url = POS_LOGIN_PAGE_URL.get(env)
    if url is None:
        raise Exception(f'No URL configured for [ {env} ] environment yet.')
    return url


class BrowserKeywords(WebLibraryComponent):


    @keyword(tags=("BrowserKeywords",))
    def open_pos_in_browser(self):
        """Open POS login page in browser."""
        self.web.open_browser(
            url=_get_url(env=self.globals.env),
            browser='chrome',
            options=self.chrome_options,
            alias=None
        )

    @keyword(tags=("BrowserKeywords",))
    def close_pos(self):
        """Closes the browser hence closing POS."""
        self.web.close_browser()

    @keyword(tags=("BrowserKeywords",))
    def reload_pos(self):
        """Reload the browser. Mimic clicking the reload button of the browser."""
        self.web.reload_browser()
