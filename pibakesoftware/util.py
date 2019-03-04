# Python file for basic utilities that are commonly used by yours truly
# Written by Wyatt J. Miller, 2019

import os
import sys

'''
Class for misc. utilities regarding the core software
'''
class Utility:

    '''
    Method for clearing the screen (i.e. Ctrl-L)
    '''
    @staticmethod
    def clear_screen(self):
        if os.name == "posix":
            os.system("clear")
        if os.name == "nt":
            os.system("cls")

    '''
    Method to check if the OS is supported
    '''
    @staticmethod
    def is_os_supported(self):
        try:
            if sys.platform != 'linux':
                raise Exception
        except Exception as e:
            print(e)
            print("Your operating system is not supported. You must be running Debian in the Raspberry Pi 3+ or better. Please email the PiBake Team at:")
            print("support@pibake.com")