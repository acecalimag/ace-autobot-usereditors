from libraries.db.KjtDbLibrary.dto.printerdetails import PrinterDetails
from autocore.bases import DBLibraryComponent
from robot.api.deco import keyword
class Printer(DBLibraryComponent):
    
        
    @keyword(tags=("kjt", "printer"))
    def query_printer_details_of_restaurant_from_printer_table(self, rid: str, _:PrinterDetails = None) -> list[PrinterDetails]:
        """Get the details of the printers that belong to ``rid`` as `PrinterDetails`.
        """
        query = "SELECT x.* FROM kjt.printer x WHERE x.rid = %s;"
        results = self.db.execute(query, (rid,))
        details = [self.__map_result_to_printer_details(i) for i in results]
        self.logger.pretty_debug(data=details)
        return details

    @keyword(tags=("kjt", "printer"))
    def query_details_of_printer_from_printer_table(self, pid: str, _:PrinterDetails = None) -> PrinterDetails:
        """Get the details of the printer with the provided ``pid`` as `PrinterDetails`.
        """
        query = "SELECT x.* FROM kjt.printer x WHERE x.pid = %s;"
        result = self.db.execute(query,(pid,))[0]
        details = self.__map_result_to_printer_details(result=result)
        self.logger.pretty_debug(data=details)
        return details
    
    def __map_result_to_printer_details(self, result) -> PrinterDetails:
        return PrinterDetails(
                pid=result['pid'],
                rid=result['rid'],
                name=result['name'],
                active=result['active'],
                nucless=result['nucless'],
                mask = result['mask'],
                maskRule=result['maskRule'],
                template=result['template'],
                templateSettings=result['templateSettings'],
                ccTemplate=result['ccTemplate'],
                creditCardVoid=result['creditCardVoid'],
                printInternalMeta=result['printInternalMeta'],
                printExternalMeta=result['printExternalMeta'],
                status=result['status'],
                lastNormalTime=result['lastNormalTime'],
                lastContactTime=result['lastContactTime'],
                statusReport=result['statusReport'],
                lastUpdatedBy=result['lastUpdatedBy'],
                createTime=result['createTime'],
                updateTime=result['updateTime']
            )
