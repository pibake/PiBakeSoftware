# Logic for reading temperature/humidity
# Written by Wyatt J. Miller, 2019

import math
import grovepi
from . import temperature


class Read:
    '''
    Class to read temperature and humidity off of the Raspberry Pi temperature sensor
    '''

    def __init__(self, temp_sensor, humid_sensor):
        '''
        Constructor
        '''
        self.temp_sensor = temp_sensor
        self.humid_sensor = humid_sensor

    def read_temperature(self):
        '''
        Method to read temperature and humidity
        '''
        try:
            # store temp and humid in variables
            [temp, hum] = grovepi.dht(self.temp_sensor, self.humid_sensor)

            # check if we have nans
            # if so, then raise a type error exception
            if math.isnan(temp) is True or math.isnan(hum) is True:
                raise TypeError('nan error')

            # convert temp/humid vars to strings
            t = str(temp)
            h = str(hum)

            # temperature instance, store it in var, return that var
            result = temperature.Temperature(t, h)
            return result

        except (IOError, TypeError) as e:
            print(str(e))

        except KeyboardInterrupt as e:
            print(str(e))
        
