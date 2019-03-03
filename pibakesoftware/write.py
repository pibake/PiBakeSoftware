# Python file for writing data to config file
# yaml and toml imports are there until we decide what configuration standard we want

import os
import json

class Write:
    def __init__(self, inputs, file="export.json", encoding="json"):
        self.file = file
        self.inputs = inputs
        self.encoding = encoding
        
    def write_to_json(self):
        result = self.does_file_exist()

        if result == False:
            self.create_file()
        else:
            self.delete_file()
            self.create_file()

        self.to_json(self.inputs.__dict__)

        return self.file

    def does_file_exist(self):
        return os.path.exists(self.file)

    def create_file(self):
        os.mknod(self.file)

    def delete_file(self):
        os.remove(self.file)

    def to_json(self, inputs):
        with open(self.file, "w") as data:
            json.dump(inputs, data)
