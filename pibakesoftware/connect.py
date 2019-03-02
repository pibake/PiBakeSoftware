import os
import sys
import paramiko

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
            transport = paramiko.Transport((self.host, self.port))
            transport.connect(username=self.username, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.put(self.file, self.remote_path)
            sftp.close()
            transport.close()
            return True
        except Exception as e:
            print("Exception occurred: ".format(e)) # pylint: disable=too-many-format-args

