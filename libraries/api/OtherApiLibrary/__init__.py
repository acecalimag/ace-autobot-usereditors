from robot.api.deco import library
from autocore.bases import APILibraryBase
from libraries.api.OtherApiLibrary.keywords.openvoxstatus import OpenVoxStatus

@library(scope='GLOBAL')
class OtherApiLibrary(APILibraryBase):
    
    def __init__(self):
        super().__init__()
        components = [
            OpenVoxStatus(library=self)
        ]
        self.add_library_components(library_components=components)