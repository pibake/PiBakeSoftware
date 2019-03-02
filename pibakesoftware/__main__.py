# Python file for the main loop (and for packaging)

import sys
import json

#from pibakesoftware import read
from . import write
from . import connect
from . import temperature

is_running = True
#read = read.Read(7, 0)

while is_running:
    # read data, write data, connect -> server, repeat
    #r = read.read_temperature()
    temp = temperature.Temperature(45,56)
    w = write.Write(temp)
    file = w.write_to_json()
    con = connect.Connect(file, "thepibake.com", 22, "pibake", "123abc", ".")
    result = con.connect_to_server()

    if result == True:
        pass
    else:
        is_running = False
else:
    sys.exit(0)

