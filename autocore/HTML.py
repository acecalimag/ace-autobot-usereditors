from lxml import html

def normalize_string(txt: str) -> str:
    if "\n" in txt:
        txt = txt.replace("\n", " ")
    if "\xa0" in txt:
        txt = txt.replace("\xa0", " ")

    txt_split = txt.split(" ")
    txt = " ".join([i.replace(" ", "") for i in txt_split if len(i) > 0])
    return txt

class HTML:

    def __init__(self, html_string: str):
        self.__html_string = html_string
        self.__parsed_html = html.fromstring(html=html_string)

    @property
    def html_string(self):
        return self.__html_string

    def get_text_of_element(self, locator: str, normalize: bool = False) -> str:
        content = self.__locate_element(locator).text_content()
        if normalize:
            content = normalize_string(content)
        return content

    def get_attribute_value_of_element(self, locator: str, attribute: str) -> str:
        return self.__locate_element(locator).attrib[attribute]

    def get_count_of_element_located_by(self, locator: str) -> str:
        return str(len(self.__locate_elements(locator=locator)))

    def __locate_elements(self, locator: str) -> list:
        if locator.startswith('id:'):
            # NOTE: using get_element_by_id() returns the first element with the specified id.
            return [self.__parsed_html.get_element_by_id(locator.removeprefix('id:'))]
        elif locator.startswith('xpath:'):
            # NOTE: using xpath() returns all the elements that match the specified xpath.
            return self.__parsed_html.xpath(locator.removeprefix('xpath:'))

        else:
            raise Exception(
                f"Provided locator is not supported. Please use 'id' or 'xpath' only. Provided locator: {locator}")

    def __locate_element(self, locator: str):
        if locator.startswith('id:'):
            # NOTE: using get_element_by_id() returns the first element with the specified id.
            return self.__parsed_html.get_element_by_id(locator.removeprefix('id:'))
        elif locator.startswith('xpath:'):
            # NOTE: using xpath() returns all the elements that match the specified xpath hence we limit it to the first element found.
            elements = self.__parsed_html.xpath(locator.removeprefix('xpath:'))
            if len(elements) == 0:
                raise Exception(f"No element found using the locator: {locator}")
            if len(elements) > 1:
                raise Exception(
                    f"Please make sure that the xpath provided points to a single element only. Provided locator: {locator}")
            return elements[0]
        else:
            raise Exception(
                f"Provided locator is not supported. Please use 'id' or 'xpath' only. Provided locator: {locator}")
