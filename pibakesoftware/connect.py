import os
import sys

from paramiko import Transport, SFTPClient, SSHException

class Connect(object):
    def __init__(self, file, host, port, username, password, 
                local_path, remote_path):
        self.file = file
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.local_path = local_path
        self.remote_path = remote_path

        self.transport = Transport((self.host, self.port))

    def initalize_transaction(self):
        try:
            return self.transport.connect(username=self.username, password=self.password)
        except SSHException:
            print("Couldn't connect via SSH! Is everything set correctly?")
        except Exception as e:
            print(f"Exception occurred: {e}")

    def connect_to_server(self):
        try:
            result = self.initalize_transaction()
            sftp = SFTPClient.from_transport(result)
            sftp.put(self.local_path, self.remote_path)
            sftp.close()
            self.transport.close()
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")

