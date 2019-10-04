# 'Connecting to the server' logic 
# Written by Wyatt J. Miller, 2019

import os
import sys
import pysftp
from paramiko import SSHClient, AutoAddPolicy

class Connect:
    '''
    Synopsis:
    Class for connect to server logic

    Details:
    The connect class instantiates various attributes relevant to connecting
    and connects to server through SSH and SFTP
    '''

    def __init__(self, file, host, port, username, password, local_path):
        '''
        Synopsis:
        Constructor for the Connect class

        Details:
        Tells class to instantiate file, host, port, user, password, and local_path attributes
        '''
        self.file = file
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.local_path = local_path

    def connect_to_server(self):
        '''
        Synopsis:
        Method to connect via SFTP/SSH

        Details:
        The SSH and SFTP connection are first closed to make sure that they are closed
        and then they are open to send data

        The SSH connection tells the server to import self.file (JSON file) and closes
        The SFTP connection sends self.file and closes
        '''

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

        except Exception:
            print("Exception occurred, returning false!")
            return False

