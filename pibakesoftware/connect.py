# 'Connecting to the server' logic 
# Written by Wyatt J. Miller

import os
import sys
import pysftp

'''
Class for connect to server logic
'''
class Connect:
    '''
    Constructor
    '''
    def __init__(self, file, host, port, username, password, local_path):
        self.file = file
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.local_path = local_path

    '''
    Method to connect via SFTP
    TODO: Break everything down into separate methods
    '''
    def connect_to_server(self):
        try:
            sftp = pysftp.Connection(self.host, username=self.username, password=self.password)
            sftp.put(self.file)
            sftp.close()
            return True
        except Exception as e:
            print("Exception occurred: ".format(e)) # pylint: disable=too-many-format-args

