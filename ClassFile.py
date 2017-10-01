#Simple python Class file.
# Author: Satyadev - 01/10/17
class Character:

    # constructor: called when new object is instantiated
    def __init__(self):
        self.char_name = None
        self.char_description = None

    # Set and Get methods to define members of class
    def set_name(self, char_name):
        self.char_name = char_name

    def get_name(self):
        return self.char_name

    def set_description(self, char_description):
        self.char_description = char_description

    def get_description(self):
        return self.char_description

    # method to get details of members
    def describe(self):
        print("Name: " + self.char_name)
        print("Detail: " + self.char_description)
