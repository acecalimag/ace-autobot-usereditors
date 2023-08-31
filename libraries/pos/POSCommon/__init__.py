from autocore.bases import WebLibraryBase
from libraries.pos.POSCommon.keywords.browser import BrowserKeywords
from libraries.pos.POSCommon.keywords.homepage import HomepageKeywords
from libraries.pos.POSCommon.keywords.loginpage import LoginKeywords
from libraries.pos.config import POS_GLOBAL_TIMEOUT, POS_HOMEPAGE_TIMEOUT


class POSCommon(WebLibraryBase):
    
    def __init__(self):
        super().__init__()
        components = [
            BrowserKeywords(library=self),
            LoginKeywords(library=self, timeout=POS_GLOBAL_TIMEOUT),
            HomepageKeywords(library=self, timeout=POS_HOMEPAGE_TIMEOUT)
        ]
        
        self.add_library_components(library_components=components)