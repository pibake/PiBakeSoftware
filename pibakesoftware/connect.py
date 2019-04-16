# 'Connecting to the server' logic 
# Written by Wyatt J. Miller

import os
import sys
import pysftp
from paramiko import SSHClient, AutoAddPolicy

class Connect:
    '''
    Class for connect to server logic
    '''

    def __init__(self, file, host, port, username, password, local_path):
        '''
        Constructor
        '''
        self.file = file
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.local_path = local_path

    def connect_to_server(self):
        '''
        Method to connect via SFTP
        '''

        attempts = 0

        try:
            ssh = SSHClient()
            ssh.set_missing_host_key_policy(AutoAddPolicy())
            ssh.load_system_host_keys()

            cnopts = pysftp.CnOpts()
            cnopts.hostkeys = None
            
            sftp = pysftp.Connection(self.host, username=self.username, password=self.password, cnopts=cnopts)
            sftp.put(self.file)

            ssh.connect(self.host, port=self.port, username=self.username, password=self.password)
            ssh.exec_command("php import.php")
            
            ssh.close()
            sftp.close()

            return True

        except Exception as e:
            print("Exception occurred: ".format(e)) # pylint: disable=too-many-format-args

