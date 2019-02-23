# Python file for reading temperature data

import os
import time
import math
import grovepi
# from grovepi_rgb_lcd import *

class Read(object):
    def __init__(self, temp_sensor, humid_sensor):
        self.temp_sensor = temp_sensor
        self.humid_sensor = humid_sensor

    def read_temperature(self):
        try:
            [temp, hum] = grovepi.dht(self.temp_sensor, self.humid_sensor)

            # check if we have nans
            # if so, then raise a type error exception
            if math.isnan(temp) is True or math.isnan(hum) is True:
                raise TypeError('nan error')

            t = str(temp)
            h = str(hum)

            return t, h
            #setText_norefresh("Temp:" + t + "C\n" + "Humidity :" + h + "%")

        except (IOError, TypeError) as e:
            print(str(e))
            # setText("")

        except KeyboardInterrupt as e:
            print(str(e))
            # setText("")

