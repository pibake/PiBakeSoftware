# Python file for writing data to config file
# Written by Wyatt J. Miller, 2019

import os
import os.path as path
import json

class Write:
    '''
    Synopsis:
    Class to serialize the temperature data

    Details:
    Class used to serialize (or write) the temperature model to a specified
    format i.e. JSON. More are soon to come later on i.e. YAML, TOML, etc.
    Please specify what kind of serialized formats you would like in
    PiBakeSoftware's Issues repository.
    '''

    def __init__(self, inputs, file="export.json", encoding="json"):
        '''
        Synopsis:
        Writing constructor

        Details:
        Instantiates the file, input (from temperature model), and encoding attributes
        '''

        self.file = file
        self.inputs = inputs
        self.encoding = encoding

    def write_to_json(self):
        '''
        Method to combine all of the following functions
        '''

        result = self.does_file_exist()

        if result == False:
            self.create_file()
        else:
            self.delete_file()
            self.create_file()

        self.to_json(self.inputs.__dict__)

        return self.file

    def does_file_exist(self):
        '''
        Synopsis:
        Method to check if the file exists

        Details:
        It's a method that checks if a file is found using the
        file attribute and takes the result of that and does
        the appropriate actions.
        '''

        return path.exists(self.file)

    def create_file(self):
        '''
        Synopsis:
        Create file method

        Details:
        It's a method that takes the file attribute of this
        class and makes a node (a.k.a a file) of that attribute in
        the current directory
        '''

        os.mknod(self.file)

    def delete_file(self):
        '''
        Method to delete the file attribute
        '''

        os.remove(self.file)

    def to_json(self, inputs):
        '''
        Method to write to JSON
        '''

        with open(self.file, "w") as data:
            json.dump(inputs, data)
