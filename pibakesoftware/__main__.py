# Python file for the main loop (and for packaging)

import sys

from pibakesoftware import read
from pibakesoftware import write
from pibakesoftware import connect

is_running = True
read = read.Read(7, 0)

while is_running:
    # read data, write data, connect -> server, repeat
    read = read.read_temperature()
    write = write.Write(read)
    file = write.write_to_json()
    connect = connect.Connect(file, "thepibake.com", "22", "pibake", "f4rh54dfg$r", ".", ".")
    result = connect.connect_to_server()

    if result == True:
        pass
    else:
        is_running = False
else:
    sys.exit(0)

