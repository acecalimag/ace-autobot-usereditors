
from autocore.bases import WebLibraryBase
from libraries.contentconfig.ContentConfigCommon.config import CONTENT_CONFIG_GLOBAL_TIMEOUT
from libraries.contentconfig.ContentConfigCommon.keywords.browser import BrowserKeywords
from libraries.contentconfig.ContentConfigCommon.keywords.landingpage import LandingPageKeywords
from libraries.contentconfig.ContentConfigCommon.keywords.loginpage import LoginKeywords


class ContentConfigCommon(WebLibraryBase):

    def __init__(self):
        WebLibraryBase.__init__(self)
        library_components = [
            BrowserKeywords(library=self),
            LoginKeywords(library=self, timeout=CONTENT_CONFIG_GLOBAL_TIMEOUT),
            LandingPageKeywords(ctx=self.ctx)
        ]
        self.add_library_components(library_components=library_components)
