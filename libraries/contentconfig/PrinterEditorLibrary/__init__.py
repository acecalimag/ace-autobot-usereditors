from robot.api.deco import library

from libraries.contentconfig.ContentConfigCommon import ContentConfigCommon
from libraries.contentconfig.ContentConfigCommon.config import CONTENT_CONFIG_GLOBAL_TIMEOUT, PRINTER_EDITOR_LANDING_TIMEOUT
from libraries.contentconfig.ContentConfigCommon.keywords.landingpage import LandingPageKeywords
from libraries.contentconfig.PrinterEditorLibrary.keywords.actions import ActionKeywords
from libraries.contentconfig.PrinterEditorLibrary.keywords.getdetails import GetDetailsKeywords
from libraries.contentconfig.PrinterEditorLibrary.keywords.validation import ValidationKeywords


@library(scope='GLOBAL')
class PrinterEditorLibrary(ContentConfigCommon):

    def __init__(self):
        ContentConfigCommon.__init__(self)
        library_components = [
            LandingPageKeywords(library=self, timeout=PRINTER_EDITOR_LANDING_TIMEOUT),
            GetDetailsKeywords(library=self,timeout=CONTENT_CONFIG_GLOBAL_TIMEOUT),
            ActionKeywords(library=self, timeout=CONTENT_CONFIG_GLOBAL_TIMEOUT),
            ValidationKeywords(library=self, timeout=CONTENT_CONFIG_GLOBAL_TIMEOUT)
        ]
        self.add_library_components(library_components=library_components)
        
