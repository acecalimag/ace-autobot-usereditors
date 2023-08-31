from robot.api.deco import keyword
from autocore.bases import WebLibraryComponent
from libraries.ros.config import ROS_LOGIN_PAGE_URL

def _get_url(env: str):
    env = env.lower().strip()
    url = ROS_LOGIN_PAGE_URL.get(env)
    if url is None:
        raise Exception(f'No URL configured for [ {env} ] environment yet.')
    return url

class BrowserKeywords(WebLibraryComponent):

    @keyword(tags=("BrowserKeywords",))
    def open_ros_in_browser(self):
        """Open ROS login page in browser."""
        self.web.open_browser(
            url=_get_url(env=self.globals.env),
            browser='chrome',
            options=self.chrome_options,
            alias=None
        )

    @keyword(tags=("BrowserKeywords",))
    def close_ros(self):
        """Closes the browser hence closing ROS."""
        self.web.close_browser()

    @keyword(tags=("BrowserKeywords",))
    def reload_ros(self):
        """Reload the browser. Mimic clicking the reload button of the browser."""
        self.web.reload_browser()