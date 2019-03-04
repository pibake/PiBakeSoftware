# Python file for writing data to config file
# Written by Wyatt J. Miller, 2019

import os
import json

'''
Class to serialize the temperature data
'''
class Write:
    '''
    Constructor
    '''
    def __init__(self, inputs, file="export.json", encoding="json"):
        self.file = file
        self.inputs = inputs
        self.encoding = encoding

    '''
    Method to combine all of the following functions
    '''    
    def write_to_json(self):
        result = self.does_file_exist()

        if result == False:
            self.create_file()
        else:
            self.delete_file()
            self.create_file()

        self.to_json(self.inputs.__dict__)

        return self.file

    '''
    Method to check if file exists
    '''
    def does_file_exist(self):
        return os.path.exists(self.file)

    '''
    Method to create the file attribute
    '''
    def create_file(self):
        os.mknod(self.file)

    '''
    Method to delete the file attribute
    '''
    def delete_file(self):
        os.remove(self.file)

    '''
    Method to write to JSON
    '''
    def to_json(self, inputs):
        with open(self.file, "w") as data:
            json.dump(inputs, data)
