# 'Connecting to the server' logic 
# Written by Wyatt J. Miller, 2019

import os
import sys
import requests

class Connect:
    '''
    Synopsis:
    Class for connect to server logic

    Details:
    The connect class instantiates various attributes relevant to connecting
    and connects to server through SSH and SFTP
    '''

    def __init__(self, file, host, port, path):
        # TODO: Revise documentation for this constructor
        
        '''
        Synopsis:
        Constructor for the Connect class

        Details:
        Tells class to instantiate file, host, port, user, password, and local_path attributes
        '''
        self.file = file
        self.host = host
        self.port = str(port)
        self.path = path

    def connect_to_server(self):
        # TODO: Revise documentation for this method
        
        '''
        Synopsis:
        Method to connect via SFTP/SSH

        Details:
        The SSH and SFTP connection are first closed to make sure that they are closed
        and then they are open to send data

        The SSH connection tells the server to import self.file (JSON file) and closes
        The SFTP connection sends self.file and closes
        '''

        url = f"http://{self.host}:{self.port}{self.path}"
        json = self.file
        headers = {"Content-Type":"application/json"}
        response = requests.post(url=url, data=json, headers=headers)
        result = response.status_code

        if result != 200:
            return False

        return True

