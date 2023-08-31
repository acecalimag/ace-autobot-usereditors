from typing import TypedDict


class PrintTaskDetails(TypedDict, total=False):
    """
    - ``oid``: Order id
    - ``html``: order receipt html
    - ``template``: name of the order receipt template used
    - ``pid``: printer id
    - ``version``: order version
    """
    oid: str
    template: str
    pid: str
    version: int
    html: str
