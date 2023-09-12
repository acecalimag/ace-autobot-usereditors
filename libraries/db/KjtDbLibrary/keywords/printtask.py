from robot.api.deco import keyword
from libraries.db.KjtDbLibrary.dto.printtaskdetails import PrintTaskDetails
from autocore.bases import DBLibraryComponent

class PrintTask(DBLibraryComponent):


    @keyword(tags=("kjt", "printtask"))
    def query_order_receipt_from_print_task_table(self, oid: str, version: str, order_receipt_template: str,
                                                _: PrintTaskDetails = None) -> list[PrintTaskDetails]:
        """Retrieves the records with ``printType`` of ``order`` from the ``printtask`` table with ``oid``, ``version``, and ``order_receipt_template``
        as addition filters. Returns a list of `PrintTaskDetails`.

        - ``oid``: order if
        - ``version``: order version
        - ``order_receipt_template``: the template of the order receipt

        Sample usage:
            | ${result}      |       Get Order Receipt From Print Task Table     oid=<order id>   version=<order version>   order_receipt_template=<template name>   |
            | Log            |       ${result}[0][html]  |
        """
        query = """SELECT pt.oid, pt.html, pt.version, pt.pid, p.template FROM printtask pt join printer p on pt.pid = p.pid WHERE pt.oid = %s and pt.printType = 'order' and pt.version = %s and p.template = %s;"""
        results = self.db.execute(query, (oid, version, order_receipt_template))
        data: list[PrintTaskDetails] = []

        if len(results) == 0:
            act_query = query % (oid,version,order_receipt_template)
            raise Exception(f"No record found for oid: {oid} in printtask table. Check manually by running this query on the DB \n [${act_query}]")

        for i in results:
            data.append(PrintTaskDetails(oid=i['oid'], template=i['template'], pid=i['pid'],
                                         version=i['version'], html=i['html']))
        self.logger.pretty_debug(data)
        return data

    @keyword(tags=("kjt", "printtask"))
    def query_void_receipt_from_print_task_table(self, oid: str, version: str, _: PrintTaskDetails = None) -> list[PrintTaskDetails]:
        """Retrieves the records with ``printType`` of ``void`` from the ``printtask`` table with ``oid`` and ``version``
        as addition filters. Returns a list of `PrintTaskDetails`.

        - ``oid``: order if
        - ``version``: order version

        Sample usage:
            | ${result}      |       Get Void Receipt From Print Task Table     oid=<order id>   version=<order version>    |
            | Log            |       ${result}[0][html]  |
        """
        query = """SELECT pt.oid, pt.html, pt.version, pt.pid FROM kjt.printtask pt WHERE printType = 'void' and oid = %s and pt.version = %s;"""
        results = self.db.execute(query, (oid, version))
        data: list[PrintTaskDetails] = []

        if len(results) == 0:
            self.logger.warn("The query result is empty.")

        for i in results:
            data.append(PrintTaskDetails(oid=i['oid'], pid=i['pid'], version=i['version'], html=i['html']))
        self.logger.pretty_debug(data)
        return data

    @keyword(tags=("kjt", "printtask"))
    def query_rush_receipt_from_print_task_table(self, oid: str, version: str, _: PrintTaskDetails = None) -> list[PrintTaskDetails]:
        """Retrieves the records with ``printType`` of ``rush`` from the ``printtask`` table with ``oid`` and ``version``
               as addition filters. Returns a list of `PrintTaskDetails`.

               - ``oid``: order if
               - ``version``: order version

               Sample usage:
                   | ${result}      |       Get Rush Receipt From Print Task Table     oid=<order id>   version=<order version>    |
                   | Log            |       ${result}[0][html]  |
               """
        query = """SELECT pt.oid, pt.html, pt.version, pt.pid FROM kjt.printtask pt WHERE printType = 'rush' and oid = %s and pt.version = %s;"""
        results = self.db.execute(query, (oid, version))
        data: list[PrintTaskDetails] = []

        if len(results) == 0:
            self.logger.warn("The query result is empty.")

        for i in results:
            data.append(PrintTaskDetails(oid=i['oid'], pid=i['pid'], version=i['version'], html=i['html']))
        self.logger.pretty_debug(data)
        return data
