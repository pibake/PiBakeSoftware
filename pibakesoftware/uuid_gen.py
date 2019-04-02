# UUID generation tool v2.1 beta Special Edition
# Written by Wyatt J. Miller, 2019

import os
import os.path as path
import json
import uuid
import datetime


class Uuid:
    def __init__(self, file="uuid.txt"):
        self.uuid = uuid.uuid4().hex
        self.deploy_date = self.generate_deploy_date()

        self.file = file

    def generate_uuid(self):
        return uuid.uuid4().hex

    def generate_deploy_date(self):
        return str(datetime.date.today())

    def read_uuid_file(self):
        with open(self.file, "r") as file:
            result = file.read()
            file.close()

        return result

    def write_uuid_file(self):
        with open(self.file, "w") as file:
            file.write(self.uuid)
            file.close()

    def read_uuid_file_json(self):
        with open(self.file, "r+") as data:
            result = json.loads(data)
            return result

    def write_uuid_file_json(self):
        with open(self.file, "w+") as data:
            json.dump(self.uuid.__dict__, data)

    def create_file(self):
        os.mknod(self.file)

    def does_file_exist(self):
        result = path.isfile(self.file)

        if result == False:
            self.create_file()
            self.write_uuid_file()
        else:
            self.write_uuid_file()