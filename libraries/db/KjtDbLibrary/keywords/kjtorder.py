from libraries.db.KjtDbLibrary.dto.kjtorderdetails import KjtOrderDetails
from autocore.bases import DBLibraryComponent
from robot.api.deco import keyword

class KjtOrder(DBLibraryComponent):

    @keyword(tags=("kjt", "kjtorder"))
    def query_order_details_from_kjt_order_table(self, oid: str, _: KjtOrderDetails = None) -> KjtOrderDetails:
        query = "SELECT x.* FROM kjt.kjtorder x WHERE oid = %s"

        results = self.db.execute(query, (oid,))
        if len(results) == 0:
            raise Exception(
                f"No order found with oid: {oid} in kjtorder table.")

        result = results[0]

        details = KjtOrderDetails(
            oid=result['oid'],
            createTime=result['createTime']
        )
        self.logger.pretty_debug(data=details)
        return details