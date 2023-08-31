from robot.api.deco import keyword
from libraries.db.KjtDbLibrary.dto.restaurantdetails import RestaurantDetails
from autocore.AssertsLibrary import assert_equal
from autocore.bases import DBLibraryComponent
from autocore import envlabels

class Restaurant(DBLibraryComponent):

    @keyword(tags=("kjt", "restaurant"))
    def query_restaurant_details_from_restaurant_table(self, rid: str, include_html: bool = False, _: RestaurantDetails = None) -> RestaurantDetails:
        """Query the restaurant details using the provided ``rid`` and return the details as `RestaurantDetails`.
        - ``include_html`` - if ``True``, will include the following values in the returned object: ``comment``, ``lunchDinnerAppInfo``,
        ``creditCardsInfo``, ``sizeInfo``. Default value is ``False``.
        """
        query = "SELECT x.* FROM kjt.restaurant x where rid = %s;"
        results = self.db.execute(query, (rid,))
        if len(results) == 0:
            raise Exception("The query did not return any results.")
        
        result = results[0]
        details = RestaurantDetails(
            rid=result['rid'],
            enName=result['enName'],
            cnName=result['cnName'],
            exName=result['exName'],
            status=result['status'],
            openTime=result['openTime'],
            rejectTime=result['rejectTime'],
            closeTime=result['closeTime'],
            callCtrRank=result['callCtrRank'],
            disableCallPriority=result['disableCallPriority'],
            hasDelivery=result['hasDelivery'],
            hasLunchSpecial=result['hasLunchSpecial'],
            hasDinnerSpecial=result['hasDinnerSpecial'],
            hasComboApp=result['hasComboApp'],
            hasCancelOrder=result['hasCancelOrder'],
            printMethod=result['printMethod'],
            dishTax=result['dishTax'],
            deliverTax=result['deliverTax'],
            deliveryFee=result['deliveryFee'],
            convenienceFee=result['convenienceFee'],
            convenienceTax=result['convenienceTax'],
            minimumDelivery=result['minimumDelivery'],
            matchMinimumDelivery=result['matchMinimumDelivery'],
            travelMode=result['travelMode'],
            forwardedPhone=result['forwardedPhone'],
            contactPhone1=result['contactPhone1'],
            contactPhone2=result['contactPhone2'],
            contactPhone3=result['contactPhone3'],
            smsPhone=result['smsPhone'],
            hasSmsEnabled=result['hasSmsEnabled'],
            fax=result['fax'],
            address1=result['address1'],
            address2=result['address2'],
            city=result['city'],
            state=result['state'],
            zipcode=result['zipcode'],
            hourText=result['hourText'],
            website=result['website'],
            creditCards=result['creditCards'],
            creditCardMask=result['creditCardMask'],
            displayMask=result['displayMask'],
            languageMask=result['languageMask'],
            ccZipCode=result['ccZipCode'],
            ccCvc=result['ccCvc'],
            ccSplit=result['ccSplit'],
            ccSwipeInStore=result['ccSwipeInStore'],
            preauthcarate=result['preauthcarate'],
            separateOrder=result['separateOrder'],
            separateOrderFeeType=result['separateOrderFeeType'],
            separateOrderFeeAmount=result['separateOrderFeeAmount'],
            etZoneOffset=result['etZoneOffset'],
            notes=result['notes'],
            closingRemark=result['closingRemark'],
            pickupClosingRemark=result['closingRemark'],
            deliveryClosingRemark=result['deliveryClosingRemark'],
            groupMask=result['groupMask'],
            minAssignedAgents=result['minAssignedAgents'],
            maxBenchedAgents=result['maxBenchedAgents'],
            mistakeRateThreshold=result['mistakeRateThreshold'],
            createTime=result['createTime'],
            updateTime=result['updateTime']
        )
        if include_html:
            details['comment'] = result['comment']
            details['lunchDinnerAppInfo'] = result['lunchDinnerAppInfo']
            details['creditCardsInfo'] = result['creditCardsInfo']
            details['sizeInfo'] = result['sizeInfo']

        self.logger.pretty_debug(details)
        return details
    
    @keyword(tags=("kjt", "restaurant"))
    def restaurant_type_based_on_restaurant_table_should_be(self, rid: str, exp_resto_type: str, no_check_in_prod: bool = False):
        """Verify the type of the restaurant with the provided``rid``.
        - ``exp_resto_type``: Accepted values are: ``external``, ``pos_only``, ``oo_only``, ``pos_and_oo``
        """
        if no_check_in_prod and self.globals.env == envlabels.PROD_ENV:
            self.logger.info(f"No checking of restaurant type was made.")
            return
        
        possible_exp_resto_type = ['external', 'pos_only','oo_only', 'pos_and_oo']
        exp_resto_type = exp_resto_type.lower().replace(" ","")
        
        if exp_resto_type not in possible_exp_resto_type:
            raise Exception(f"Please make sure that the value of exp_resto_type is any of {possible_exp_resto_type}")
        
        resto_details = self.query_restaurant_details_from_restaurant_table(rid=rid)
        cc_mask = resto_details['creditCardMask']
        if cc_mask is None:
            raise Exception(f"Restaurant with rid: {rid} has no credit card mask.")
        cc_mask = int(cc_mask)
        
        if cc_mask < 32:
            act_resto_type = 'external'
        elif cc_mask >= 128 and cc_mask < 160:
            act_resto_type = 'pos_only'
        elif cc_mask >= 160 and cc_mask < 192:
            act_resto_type = 'oo_only'
        elif cc_mask >= 192 and cc_mask < 224:
            act_resto_type = 'pos_and_oo'
        else:
            raise Exception(f"Cannot identify type of restaurant with rid: {rid}. Actual credit card mask: {cc_mask}")
        
        assert_equal(actual=act_resto_type, exp=exp_resto_type, desc="Restaurant type.")


    @keyword(tags=("kjt", "restaurant"))
    def restaurant_status_based_on_restaurant_table_should_be(self, rid: str, exp_status: str):
        resto_details = self.query_restaurant_details_from_restaurant_table(rid=rid)
        act_status = resto_details['status']
        assert_equal(actual=act_status, exp=exp_status, desc="Restaurant Status")

