# Python file for basic utilities that are commonly used by yours truly

import os
import sys

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
        if sys.platform != "linux":
            sys.exit(0)