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
    Unqiue Universal Identifier generator class
    '''

    def __init__(self, file="uuid.txt"):
        '''
        Constructor
        '''
        self.uuid = uuid.uuid4().hex
        self.deploy_date = self.generate_deploy_date()

        self.file = file

    def generate_uuid(self):
        '''
        UUID generation method
        '''
        return uuid.uuid4().hex

    def generate_deploy_date(self):
        '''
        Deploy date generation method
        '''
        return str(datetime.date.today())

    def read_uuid_file(self):
        '''
        Text file reading method
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