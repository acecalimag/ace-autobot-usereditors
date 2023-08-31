from requests import Response
from robot.api.deco import keyword
from autocore.bases import APILibraryComponent
from autocore.coreutils import remove_none_values_from_dict, to_bool


class Restaurant(APILibraryComponent):


    @keyword(tags=("RestaurantKeywords","GetRequest"))
    def request_to_get_restaurant_details(self, jwt: str, rid: str) -> Response:
        return self.api.get(
            url=f"{self.base_url}/contentconfigserver/api/restaurant/{rid}",
            headers={
                'Authorization': f'Bearer {jwt}'
            }
        )

    @keyword(tags=("RestaurantKeywords","PutRequest"))
    def request_to_update_restaurant_details(self, jwt: str, rid: str, address1: str = None, address2: str = None, call_ctr_rank: str = None,
                                             city: str = None, contact_phone1: str = None, contact_phone2: str = None, contact_phone3: str = None,
                                             convenience_fee: str = None, convenience_tax: str = None, deliver_tax: str = None, delivery_closing_remark: str = None,
                                             delivery_fee: str = None, display_mask: str = None, en_name: str = None, et_zone_offset: str = None, ex_name: str = None,
                                             forwarded_phone: str = None, has_cancel_order: str = None, has_delivery: str | bool = None, has_sms_enabled: str | bool = None,
                                             hour_text: str = None, language_mask: str = None, match_min_delivery: str | bool = None, min_delivery: str = None, mistake_threshold: str = None,
                                             notes: str = None, pickup_closing_remark: str = None, separate_order: str | bool = None, separate_order_fee: str = None,
                                             state: str = None, status: str = None, travel_mode: str = None, website: str = None, zipcode: str = None, dish_tax: str = None,
                                             separate_order_fee_type: str = None, exlude_none_values_from_body: bool = True
                                             ) -> Response:
        body = {
            "rid": rid,
            "address1": address1,
            "address2": address2,
            "callCtrRank": int(call_ctr_rank) if call_ctr_rank is not None else None,
            "city": city,
            "contactPhone1": contact_phone1,
            "contactPhone2": contact_phone2,
            "contactPhone3": contact_phone3,
            "convenienceFee": float(convenience_fee) if convenience_fee is not None else None,
            "convenienceTax": float(convenience_tax) if convenience_tax is not None else None,
            "deliverTax": float(deliver_tax) if deliver_tax is not None else None,
            "deliveryClosingRemark": delivery_closing_remark,
            "deliveryFee": float(delivery_fee) if delivery_fee is not None else None,
            "dishTax": float(dish_tax) if dish_tax is not None else None,
            "displayMask": int(display_mask) if display_mask is not None else None,
            "enName": en_name,
            "etZoneOffSet": int(et_zone_offset) if et_zone_offset is not None else None,
            "exName": ex_name,
            "forwardedPhone": forwarded_phone,
            "hasCancelOrder": int(has_cancel_order) if has_cancel_order is not None else None,
            "hasDelivery": to_bool(has_delivery) if has_delivery is not None else None,
            "hasSmsEnabled": to_bool(has_sms_enabled) if has_sms_enabled is not None else None,
            "hourText": hour_text,
            "languageMask": int(language_mask) if language_mask is not None else None,
            "matchMinimumDelivery": to_bool(match_min_delivery) if match_min_delivery is not None else None,
            "minimumDelivery": float(min_delivery) if min_delivery is not None else None,
            "mistakeRateThreshold": int(mistake_threshold) if mistake_threshold is not None else None,
            "notes": notes,
            "pickupClosingRemark": pickup_closing_remark,
            "separateOrder": to_bool(separate_order) if separate_order is not None else None,
            "separateOrderFeeAmount": float(separate_order_fee) if separate_order_fee is not None else None,
            "separateOrderFeeType": separate_order_fee_type,
            "state": state,
            "status": status,
            "travelMode": travel_mode,
            "website": website,
            "zipcode": zipcode
        }

        if exlude_none_values_from_body:
            body = remove_none_values_from_dict(dictionary=body)
            
        return self.api.put(
            url=f"{self.base_url}/contentconfigserver/admin/restaurant",
            headers={
                'Authorization':f'Bearer {jwt}'
            },
            json=body
        )
