from robot.api.deco import library
from libraries.pos.POSCommon import POSCommon
from libraries.pos.POSRestaurantLibrary.keywords.fooditemsarea import FoodItemsAreaKeywords
from libraries.pos.POSRestaurantLibrary.keywords.helpers.libhelper import LibraryHelperKeywords
from libraries.pos.POSRestaurantLibrary.keywords.helpers.stringhelper import StringHelperKeywords
from libraries.pos.POSRestaurantLibrary.keywords.modals.ccmodal import CreditCardModalKeywords
from libraries.pos.POSRestaurantLibrary.keywords.modals.confirmmodal import ConfirmModalKeywords
from libraries.pos.POSRestaurantLibrary.keywords.modals.dispositionmodal import DispositionModalKeywords
from libraries.pos.POSRestaurantLibrary.keywords.modals.infomodal import InfoModalKeywords
from libraries.pos.POSRestaurantLibrary.keywords.modals.rushordermodal import RushOrderModalKeywords
from libraries.pos.POSRestaurantLibrary.keywords.modals.utilmodal import UtilModalKeywords
from libraries.pos.POSRestaurantLibrary.keywords.modals.voidordermodal import VoidOrderModalKeywords
from libraries.pos.POSRestaurantLibrary.keywords.morelanding import MoreLandingKeywords
from libraries.pos.POSRestaurantLibrary.keywords.moreorderlist import OrderListKeywords
from libraries.pos.POSRestaurantLibrary.keywords.restaurantlanding import RestaurantLandingKeywords
from libraries.pos.POSRestaurantLibrary.keywords.cxorderform import CxOrderFormKeywords
from libraries.pos.POSRestaurantLibrary.keywords.modals.datanotify import DataNotifyAlertKeywords
from libraries.pos.config import POS_GLOBAL_TIMEOUT

@library(scope='GLOBAL')
class POSRestaurantLibrary(POSCommon):
    
    def __init__(self):
        super().__init__()
        components = [
            RestaurantLandingKeywords(library=self, timeout=POS_GLOBAL_TIMEOUT),
            FoodItemsAreaKeywords(library=self, timeout=POS_GLOBAL_TIMEOUT),
            DataNotifyAlertKeywords(library=self, timeout=POS_GLOBAL_TIMEOUT),
            CxOrderFormKeywords(library=self, timeout=POS_GLOBAL_TIMEOUT),
            CreditCardModalKeywords(library=self, timeout=POS_GLOBAL_TIMEOUT),
            OrderListKeywords(library=self, timeout=POS_GLOBAL_TIMEOUT),
            MoreLandingKeywords(library=self, timeout=POS_GLOBAL_TIMEOUT),
            VoidOrderModalKeywords(library=self, timeout=POS_GLOBAL_TIMEOUT),
            UtilModalKeywords(library=self, timeout=POS_GLOBAL_TIMEOUT),
            RushOrderModalKeywords(library=self, timeout=POS_GLOBAL_TIMEOUT),
            InfoModalKeywords(library=self, timeout=POS_GLOBAL_TIMEOUT),
            DispositionModalKeywords(library=self, timeout=POS_GLOBAL_TIMEOUT),
            ConfirmModalKeywords(library=self, timeout=POS_GLOBAL_TIMEOUT)
        ]
        
        helpers = [
            LibraryHelperKeywords(library=self),
            StringHelperKeywords(library=self)
        ]
        self.add_library_components(library_components=components)
        self.add_library_components(library_components=helpers)
        