import sys
from robot.libraries.BuiltIn import BuiltIn
from autocore.bases import WebLibraryBase
from libraries.ros.ROSCommonLibrary import ROSCommonLibrary


class ROSSubLibraryBase(WebLibraryBase):

    def __init__(self, roscommon: ROSCommonLibrary = None):
        super().__init__()
        try:
            ros_common_library: ROSCommonLibrary = BuiltIn().get_library_instance(
                name="libraries.ros.ROSCommonLibrary")
        except Exception:
            if roscommon is not None:
                ros_common_library = roscommon
            else:
                if sys.argv[0].endswith('libdoc'):
                    # Adding this so libdoc won't raise an exception when generating library documentations
                    ros_common_library = ROSCommonLibrary() 
                else:
                    raise Exception(
                    "Cannot instantiate ROSSubLibraryBase. When using a ROSSubLibrary (Library that extends ROSSubLibraryBase) in robot files, be sure to import libraries.ros.ROSCommonLibrary first. If using it in python code, be sure to pass an object of ROSCommonLibrary when instantiating the ROSSubLibrary.")
        self.override_selenium_library(
            new_se_lib=ros_common_library.create_web_action().se_lib)
