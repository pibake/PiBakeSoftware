# 'Connecting to the server' logic 
# Written by Wyatt J. Miller

import os
import sys
import pysftp

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
        TODO: Break everything down into separate methods
        '''

        attempts = 0

        try:
            cnopts = pysftp.CnOpts()
            cnopts.hostkeys = None
            sftp = pysftp.Connection(self.host, username=self.username, password=self.password, cnopts=cnopts)

            result = sftp.put(self.file)

            return True

        except Exception as e:
            print("Exception occurred: ".format(e)) # pylint: disable=too-many-format-args

