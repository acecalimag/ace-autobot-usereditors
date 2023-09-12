from robot.api.deco import library
from autocore.bases import APILibraryBase
from libraries.api.PshApiLibrary.keyword.printerstatus import PrinterStatus

@library(scope='GLOBAL')
class PshApiLibrary(APILibraryBase):
    
    def __init__(self):
        super().__init__()
        components = [
            PrinterStatus(library=self)
        ]
        self.add_library_components(library_components=components)