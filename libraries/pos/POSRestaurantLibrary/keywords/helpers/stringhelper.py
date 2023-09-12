import re
from robot.api.deco import keyword

from autocore.bases import WebLibraryComponent

class StringHelperKeywords(WebLibraryComponent):
    
    
    @keyword(tags=("StringHelpers",))
    def extract_credit_card_minimum(self, credit_card_info: str) -> tuple:
        pattern_main_string = r"Min(?:imum)? \$(\d+(?:\.\d*)?)"
        patter_amount = r"\d+(?:\.\d*)?"
    
        main_str = re.search(pattern_main_string, credit_card_info, re.IGNORECASE)
        if main_str is None:
            self.logger.warn(f"No minimum found in html string \n{credit_card_info}")
            return None, None
        
        amt_str = re.search(patter_amount, main_str.group(), re.IGNORECASE)
        if amt_str is None:
            self.logger.warn(f"No minimum found in html string \n{credit_card_info}")
            return main_str.group(), None
        
        return main_str.group(), amt_str.group()