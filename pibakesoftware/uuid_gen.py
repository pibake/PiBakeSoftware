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
        It's a method that returns a read text file stream
        '''

        with open(self.file, "r") as file:
            result = file.read()
            file.close()

        return result

    def write_uuid_file(self):
        '''
        Synopsis:
        Text file writing method

        Details:
        It's a method that writes to already created text file. If
        something is already in text file, this method will overwrite it as well
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
        Synopsis:
        Create file method

        Details:
        It's a method that takes the file attribute of this
        class and makes a node (a.k.a a file) of that attribute in
        the current directory
        '''

        os.mknod(self.file)

    def does_file_exist(self):
        '''
        Synopsis:
        Method to check if the file exists

        Details:
        It's a method that checks if a file is found using the
        file attribute and takes the result of that and does
        the appropriate actions.
        '''

        result = path.isfile(self.file)

        if result == False:
            self.create_file()
            self.write_uuid_file()
        else:
            pass
