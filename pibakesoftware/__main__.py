# Python file for the main loop (and for packaging)
# Written by Wyatt J. Miller, 2019

import sys
import time

from . import read
from . import write
from . import connect
from . import temperature

is_running = True
read = read.Read(7, 0)

try:
    while is_running:
        # read data, write data, connect -> server, repeat
        temp = read.read_temperature()
        #temp = temperature.Temperature(45,56)
        w = write.Write(temp)
        file = w.write_to_json()
        con = connect.Connect(file, "thepibake.com", 22, "pibake", "123abc", ".")
        result = con.connect_to_server()
    
        if result == True:
            time.sleep(60)
        else:
            is_running = False
    else:
        sys.exit(0)

except KeyboardInterrupt:
    print("Keyboard interrupt: manual intervention has been invoked!")