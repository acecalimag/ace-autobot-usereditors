from robot.api.deco import library
from autocore.bases import APILibraryBase
from libraries.api.ContentConfigApiLibrary.keywords.contentconfigtoken import ContentConfigToken
from libraries.api.ContentConfigApiLibrary.keywords.restaurant import Restaurant

@library(scope='GLOBAL')
class ContentConfigApiLibrary(APILibraryBase):
    
    def __init__(self):
        APILibraryBase.__init__(self)
        components = [
            Restaurant(library=self),
            ContentConfigToken(library=self)
        ]
        self.add_library_components(library_components=components)