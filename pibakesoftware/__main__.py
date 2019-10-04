# Python file for the main loop (and for packaging)
# Written by Wyatt J. Miller, 2019
#
#
# Master TODO list:
# * Create a common file API
# * Make the connect_to_server() method less monolithic
# * Probs more

import sys
import time
import uuid

from . import read
from . import write
from . import connect
from . import temperature
from . import uuid_gen

is_running = True
read = read.Read()
attempts = 0

try:
    while is_running:
        # read data, write data, connect -> server, repeat
        uuid = uuid_gen.Uuid()
        uuid.does_file_exist()
        temp = read.read_temp()
        #temp = temperature.Temperature(45,56)
        w = write.Write(temp)
        file = w.write_to_json()
        con = connect.Connect(file, "thepibake.com", 22, "pibake", "123abc", ".")
        result = con.connect_to_server()

        if result == True:
            time.sleep(60)
        else:
            attempts += 1

            if attempts == 5:
                is_running = False
            else:
                pass

    else:
        sys.exit(0)

except KeyboardInterrupt:
    print("Keyboard interrupt: manual intervention has been invoked!")
