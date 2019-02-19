# Python file for the main loop (and for packaging)

import sys

from pibakesoftware import read

is_running = True
read = read.Read()

while is_running:
    # read data
    # write data
    # connect -> server
    # repeat
    read.read_temperature()
else:
    sys.exit(0)

