import time

from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn

import json

@library
class RestaurantEditor:

    #   This will store the original data
    temp_dict = dict()

    #   This will hold the actual value fetched from the site
    actual_value = list()

    # This is the constructor that will help you to use the keywords available in robot framework
    def __init__(self):
        self.selLib = BuiltIn().get_library_instance("SeleniumLibrary")

    # This function will store the default data of a restaurant
    # and compare the fetched data to the stored default value of a restaurant
    @keyword
    def store_restaurant_data(self, **kwargs):

        i = 0  # this will be your counter on looping the values on your list

        #   Loop through on your dictionary (parameter)
        for key, value in kwargs.items():

            #   This will append the key value pair on your temp_dict dictionary
            if key == "status" and value == "open":
                self.temp_dict.update({key: "Active"})
            else:
                self.temp_dict.update({key: value})

            #   Getting the actual value of an element
            element_value = self.selLib.get_value(key)

            #   Replace the return value of a locator based on the list of values displayed on the UI
            def switch(value):
                if value == "open":
                    self.actual_value.append("Active")
                elif value == "reject":
                    self.actual_value.append("Inactive")
                elif value == "closed":
                    self.actual_value.append("Offboarding")
                elif value == "new":
                    self.actual_value.append("Onboarding")
                elif value == "template":
                    self.actual_value.append("Template")
                elif value == "test":
                    self.actual_value.append("Test")
                elif value == "0":
                    self.actual_value.append("Eastern Time")
                elif value == "-1":
                    self.actual_value.append("Central Time")
                elif value == "-2":
                    self.actual_value.append("Mountain Time")
                elif value == "-3":
                    self.actual_value.append("Pacific Time")
                else:
                    self.actual_value.append(element_value.lstrip())

            # Call the function switch value and pass the argument which is derived from the actual value of an element
            switch(element_value)

            #   To compare the actual and stored data
            if self.temp_dict[key] == self.actual_value[i]:
                print("The default data is {}, and the actual is {}".format(self.temp_dict[key], self.actual_value[i]))
            i += 1

    @keyword
    def store_address_data(self, **kwargs):

        self.selLib.wait_until_element_is_visible("link:Address")

        self.selLib.click_link("Address")

        #   Loop through on your dictionary (parameter)
        for key, value in kwargs.items():

            #   This will append the key value pair on your temp_dict dictionary
            self.temp_dict.update({key: value})

            #   Getting the actual value of an element
            element_value = self.selLib.get_value(key)

            def switch(value):
                if value == "AL":
                    self.actual_value.append("Alabama")
                elif value == "AK":
                    self.actual_value.append("Alaska")
                elif value == "AZ":
                    self.actual_value.append("Arizona")
                elif value == "AR":
                    self.actual_value.append("Arkansas")
                elif value == "CA":
                    self.actual_value.append("California")
                elif value == "CO":
                    self.actual_value.append("Colorado")
                elif value == "CT":
                    self.actual_value.append("Connecticut")
                elif value == "DE":
                    self.actual_value.append("Delaware")
                elif value == "DC":
                    self.actual_value.append("District Of Columbia")
                elif value == "FL":
                    self.actual_value.append("Florida")
                elif value == "GA":
                    self.actual_value.append("Georgia")
                elif value == "HI":
                    self.actual_value.append("Hawaii")
                elif value == "ID":
                    self.actual_value.append("Idaho")
                elif value == "IL":
                    self.actual_value.append("Illinois")
                elif value == "IN":
                    self.actual_value.append("Indiana")
                elif value == "IA":
                    self.actual_value.append("Iowa")
                elif value == "KS":
                    self.actual_value.append("Kansas")
                elif value == "KY":
                    self.actual_value.append("Kentucky")
                elif value == "LA":
                    self.actual_value.append("Louisiana")
                elif value == "ME":
                    self.actual_value.append("Maine")
                elif value == "MD":
                    self.actual_value.append("Maryland")
                elif value == "MA":
                    self.actual_value.append("Massachusetts")
                elif value == "MI":
                    self.actual_value.append("Michigan")
                elif value == "MN":
                    self.actual_value.append("Minnesota")
                elif value == "MS":
                    self.actual_value.append("Mississippi")
                elif value == "MO":
                    self.actual_value.append("Missouri")
                elif value == "MT":
                    self.actual_value.append("Montana")
                elif value == "NE":
                    self.actual_value.append("Nebraska")
                elif value == "NV":
                    self.actual_value.append("Nevada")
                elif value == "NH":
                    self.actual_value.append("New Hampshire")
                elif value == "NJ":
                    self.actual_value.append("New Jersey")
                elif value == "NM":
                    self.actual_value.append("New Mexico")
                elif value == "NY":
                    self.actual_value.append("New York")
                elif value == "NC":
                    self.actual_value.append("North Carolina")
                elif value == "ND":
                    self.actual_value.append("North Dakota")
                elif value == "OH":
                    self.actual_value.append("Ohio")
                elif value == "OK":
                    self.actual_value.append("Oklahoma")
                elif value == "OR":
                    self.actual_value.append("Oregon")
                elif value == "PA":
                    self.actual_value.append("Pennsylvania")
                elif value == "RI":
                    self.actual_value.append("Rhode Island")
                elif value == "SC":
                    self.actual_value.append("South Carolina")
                elif value == "SD":
                    self.actual_value.append("South Dakota")
                elif value == "TN":
                    self.actual_value.append("Tennessee")
                elif value == "TX":
                    self.actual_value.append("Texas")
                elif value == "UT":
                    self.actual_value.append("Utah")
                elif value == "VT":
                    self.actual_value.append("Vermont")
                elif value == "VA":
                    self.actual_value.append("Virginia")
                elif value == "WA":
                    self.actual_value.append("Washington")
                elif value == "WV":
                    self.actual_value.append("West Virginia")
                elif value == "WI":
                    self.actual_value.append("Wisconsin")
                elif value == "WY":
                    self.actual_value.append("Wyoming")
                else:
                    self.actual_value.append(element_value.lstrip())

            #   Calling the switch() method
            switch(element_value)

        j = 0   # This is a counter to iterate the values to print for checking
        for key, value in self.temp_dict.items():
            if value == self.actual_value[j]:
                print("Item in {} is matched to {}".format(value, self.actual_value[j]))
            else:
                print("Item in {} is not matched to {}".format(value, self.actual_value[j]))
            j += 1

    @keyword
    def store_contact_data(self, **kwargs):

        self.selLib.wait_until_element_is_visible("link:Contact")

        self.selLib.click_link("Contact")

        #   Loop through on your dictionary (parameter)
        for key, value in kwargs.items():

            #   This will append the key value pair on your temp_dict dictionary
            self.temp_dict.update({key: value})

            #   Getting the actual value of an element
            element_value = self.selLib.get_value(key)

            self.actual_value.append(element_value.lstrip())

        j = 0   # This is a counter to iterate the values to print for checking
        for key, value in self.temp_dict.items():
            if value == self.actual_value[j]:
                print("Item in {} is matched to {}".format(value, self.actual_value[j]))
            else:
                print("Item in {} is not matched to {}".format(value, self.actual_value[j]))
            j += 1

    @keyword
    def store_order_data(self, **kwargs):

        self.selLib.wait_until_element_is_visible("link:Order")

        self.selLib.click_link("Order")

        #   Loop through on your dictionary (parameter)
        for key, value in kwargs.items():
            #   This will append the key value pair on your temp_dict dictionary
            self.temp_dict.update({key: value})

            #   Getting the actual value of an element
            element_value = self.selLib.get_value(key)

            def switch(value):
                if value == "dividedAmount":
                    self.actual_value.append("Split Evenly")
                elif value == "dividedAmountWithMinimum":
                    self.actual_value.append("Split Evenly with Minimum")
                elif value == "fixedAmount":
                    self.actual_value.append("Fixed Amount")
                elif value == "sameAmount":
                    self.actual_value.append("Treat as Different Address")
                else:
                    self.actual_value.append(element_value.lstrip())

            if element_value == 'on':
                self.actual_value.append("Selected")
            else:
                switch(element_value)

        j = 0  # This is a counter to iterate the values to print for checking
        for key, value in self.temp_dict.items():
            if value == self.actual_value[j]:
                print("Item in {} is matched to {}".format(value, self.actual_value[j]))
            else:
                print("Item in {} is not matched to {}".format(value, self.actual_value[j]))
            j += 1

    @keyword
    def store_delivery_data(self, **kwargs):

        self.selLib.wait_until_element_is_visible("link:Delivery")

        self.selLib.click_link("Delivery")

        #   Loop through on your dictionary (parameter)
        for key, value in kwargs.items():
            #   This will append the key value pair on your temp_dict dictionary
            self.temp_dict.update({key: value})

            #   Getting the actual value of an element
            element_value = self.selLib.get_value(key)

            def switch(value):
                if value == "walking":
                    self.actual_value.append("Walking")
                elif value == "driving":
                    self.actual_value.append("Driving")
                elif value == "bicycling":
                    self.actual_value.append("Bicycling")
                else:
                    self.actual_value.append(element_value.lstrip())

            if element_value == 'on':
                self.actual_value.append("Selected")
            else:
                switch(element_value)

        j = 0  # This is a counter to iterate the values to print for checking
        for key, value in self.temp_dict.items():
            if value == self.actual_value[j]:
                print("{} location value is {} == {}".format(key, value, self.actual_value[j]))
            else:
                print("{} location value is {} != {}".format(key, value, self.actual_value[j]))
            j += 1

        self.store_data_json(self.temp_dict)

        print("*********************")
        print("This is the actual value: " + str(self.actual_value))
        print("\n")
        print("This is the default value before update: " + str(self.temp_dict))
        print("*********************")

    @keyword
    def store_data_json(self, dictionary):
        with open("09RestaurantEditor\\Resources\\Data\\data.json", "a") as outfile:
            json.dump(dictionary, outfile)

    @keyword
    def checkbox_is_checked(self, locator):
        if self.selLib.checkbox_should_be_selected(locator) is True:
            return True
        else:
            return False

    @keyword
    def strip_left(self, string):
        return string.lstrip()

    '''**********************************
    This is a reusable keyword when modifying a field in the editor.
    element_to_change = key in section_dict that intended to change the value
    text_input = str
    locator = link element
    section_dict =  dict()
    **********************************'''
    @keyword
    def modify_element_data(self, element_to_change, text_input, locator, section_dict):

        if locator == "null":
            pass
        else:
            self.selLib.wait_until_element_is_visible(locator)

            self.selLib.click_element(locator)

        time.sleep(3)

        section_stored_data = dict()
        list_section_data = list()

        for key, value in section_dict.items():  # Iterate to all items in the argument passed to add_data_in_section keyword
            section_stored_data.update({key: value})  # This will append the key value pair on your temp_data dictionary
            element_value = self.selLib.get_value(key.lstrip())
            list_section_data.append(element_value)

        print("This is the default value before the update: " + str(section_stored_data))

        for key, value in section_stored_data.items():
            if key == element_to_change:
                # self.selLib.clear_element_text(key)  # This will clear the field first

                self.selLib.input_text(key, text_input, "clear=True")  # Enter text to the field

                self.selLib.click_element("triggerSave")

                self.selLib.wait_until_element_contains("toasts", "Changes saved successfully!")

            section_stored_data.update({key: self.selLib.get_value(key.lstrip())})

        if "Contact" in locator:
            text_input = self.format_tel(text_input)
            self.catching_change_value(section_stored_data[element_to_change], text_input)
        else:
            self.catching_change_value(section_stored_data[element_to_change], text_input)

        print("This is the default value after the update: " + str(section_stored_data))

        time.sleep(3)

    def catching_change_value(self, expect_text, actual_data):

        if expect_text == actual_data:
            print("True")
        else:
            raise Exception("Value is {} instead of {}".format(expect_text, actual_data))

    def format_tel(self, phone):

        if len(phone) != 10:
            raise Exception("Phone number should only 10 digits")
            quit()

        assert (len(phone) == 10)
        format_phone = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"

        return format_phone