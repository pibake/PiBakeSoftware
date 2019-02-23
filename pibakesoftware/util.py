# Python file for basic utilities that are commonly used by yours truly

import os
import sys
import error

class Utility(object):
    def __init__(self):
        pass

    @staticmethod
    def clear_screen(self):
        if os.name == "posix":
            os.system("clear")
        if os.name == "nt":
            os.system("cls")

    @staticmethod
    def is_os_supported(self):
        try:
            if sys.platform != 'linux':
                raise Exception
        except Exception as e:
            print(e)
            print("Your operating system is not supported. Please email the PiBake Team at:")
            print("support@pibake.com")