import os
import sys
import paramiko

class Connect:
    def __init__(self, file, host, port, username, password, local_path, remote_path):
        self.file = file
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.local_path = local_path
        self.remote_path = remote_path

    def connect_to_server(self):
        try:
            transport = paramiko.Transport((self.host, self.password))
            transport.connect(username="pibake", password="f4rh54dfg$r")
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.put(self.local_path, self.remote_path)
            sftp.close()
            transport.close()
            return True
        except Exception as e:
            print("Exception occurred: ".format(e)) # pylint: disable=too-many-format-args

