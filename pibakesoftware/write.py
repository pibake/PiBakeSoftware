# Python file for writing data to config file
# Written by Wyatt J. Miller, 2019

import os
import os.path as path
import json

class Write:
    '''
    Class to serialize the temperature data
    '''

    def __init__(self, inputs, file="export.json", encoding="json"):
        '''
        Constructor
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
        Method to check if file exists
        '''
        return path.exists(self.file)

    def create_file(self):
        '''
        Method to create the file attribute
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
