from requests import Response

from autocore.bases import APILibraryBase


class ContentConfigApiLibrary(APILibraryBase):
    
    def __init__(self):...
    
    # The method signatures below are from libraries.api.ContentConfigApiLibrary.keywords.restaurant.py
    def request_to_get_restaurant_details(self, jwt: str, rid: str) -> Response:...
    def request_to_update_restaurant_details(self, jwt: str, rid: str, address1: str = None, address2: str = None, call_ctr_rank: str = None,
                                            city: str = None, contact_phone1: str = None, contact_phone2: str = None, contact_phone3: str = None,
                                            convenience_fee: str = None, convenience_tax: str = None, deliver_tax: str = None, delivery_closing_remark: str = None,
                                            delivery_fee: str = None, display_mask: str = None, en_name: str = None, et_zone_offset: str = None, ex_name: str = None,
                                            forwarded_phone: str = None, has_cancel_order: str = None, has_delivery: str | bool = None, has_sms_enabled: str | bool = None,
                                            hour_text: str = None, language_mask: str = None, match_min_delivery: str | bool = None, min_delivery: str = None, mistake_threshold: str = None,
                                            notes: str = None, pickup_closing_remark: str = None, separate_order: str | bool = None, separate_order_fee: str = None,
                                            state: str = None, status: str = None, travel_mode: str = None, website: str = None, zipcode: str = None, dish_tax: str = None,
                                            separate_order_fee_type: str = None
                                            ) -> Response:...
    
    # The method signatures below are from libraries.api.ContentConfigApiLibrary.keywords.contentconfigtoken.py
    def request_for_a_token(self, username: str, password: str) -> Response:...
    def request_for_a_token_and_extract_jwt(self, username: str, password: str) -> str:...