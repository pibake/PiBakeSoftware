import os
import sys
import pysftp

class Connect(object):
    def __init__(self, file, host, port, username, password, 
                remote_path):
        self.file = file
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        #self.local_path = local_path
        self.remote_path = remote_path

    def connect_to_server(self):
        try:
            #result = self.initalize_transaction()
            sftp = pysftp.Connection(self.host, port=self.port, username=self.username, password=self.password)
            sftp.put(self.file)
            sftp.close()
            return True
        except Exception as e:
            print("Exception occurred: ".format(e)) # pylint: disable=too-many-format-args

