
from autocore.bases import LibraryBase
from robot.api.deco import keyword
from autocore.html import HTML

class OrderReceiptLibraryBase(LibraryBase):
    
    @keyword
    def convert_to_html_object(self, html_str: str) -> HTML:
        return HTML(html_string=html_str)