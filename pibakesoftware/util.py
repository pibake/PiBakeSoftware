# Python file for basic utilities that are commonly used by yours truly
# Written by Wyatt J. Miller, 2019

import os
import sys


class Utility:
    '''Class for misc. utilities regarding the core software'''

    @staticmethod
    def clear_screen(self):
        '''
        Method for clearing the screen (i.e. Ctrl-L)
        '''
        if os.name == "posix":
            os.system("clear")
        if os.name == "nt":
            os.system("cls")

    @staticmethod
    def is_os_supported(self):
        '''
        Method to check if the OS is supported
        '''
        try:
            if sys.platform != 'linux':
                raise Exception
        except Exception as e:
            print(e)
            print("Your operating system is not supported. You must be running Debian on the Raspberry Pi 3+ or better. Please email the PiBake Team at:")
            print("support@pibake.com")
