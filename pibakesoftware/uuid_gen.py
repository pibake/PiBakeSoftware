# UUID generation tool v2.1 beta Special Edition
# Written by Wyatt J. Miller, 2019
#
# TODO: Needs documentation

import os
import os.path as path
import json
import uuid
import datetime

class Uuid:
    '''
    Synopsis:
    Unqiue Universal Identifier generator class
    
    Details:
    A class to solely generate a unique unniversal identifier.
    Generates a new UUID, deploy date, and a file if one has not been created
    once this object is instantiated.
    '''

    def __init__(self, file="uuid.txt"):
        '''
        Synopsis:
        Constructor

        Details:
        Instatiates a new UUID, deploy date and file attributes
        '''

        self.uuid = uuid.uuid4().hex
        self.deploy_date = self.generate_deploy_date() # Deprecated

        self.file = file

    def generate_uuid(self):
        '''
        Synopsis:
        UUID generation method

        Details:
        Method that generates a UUID in hexadecimal
        '''

        return uuid.uuid4().hex

    def generate_deploy_date(self):
        '''
        Synopsis:
        Deploy date/time generation method

        NOTE: DEPRECATED

        Details:
        Method that generates the deploy date and deploy time 
        based on today's date and time
        
        NOTE: DEPRECATED
        '''

        return str(datetime.date.today())

    def read_uuid_file(self):
        '''
        Synopsis:
        Text file reading method
        
        Details:

        '''

        with open(self.file, "r") as file:
            result = file.read()
            file.close()

        return result

    def write_uuid_file(self):
        '''
        Text file writing method
        '''

        with open(self.file, "w") as file:
            file.write(self.uuid)
            file.close()

    def read_uuid_file_json(self):
        '''
        JSON file reading method
        '''

        with open(self.file, "r+") as data:
            result = json.loads(data)
            return result

    def write_uuid_file_json(self):
        '''
        JSON file writing method
        '''

        with open(self.file, "w+") as data:
            json.dump(self.uuid.__dict__, data)

    def create_file(self):
        '''
        Create file method
        '''

        os.mknod(self.file)

    def does_file_exist(self):
        '''
        Method to check if the file exists
        '''

        result = path.isfile(self.file)

        if result == False:
            self.create_file()
            self.write_uuid_file()
        else:
            pass