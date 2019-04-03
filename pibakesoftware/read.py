# Logic for reading temperature/humidity
# Written by Wyatt J. Miller, 2019

import math
import os
import glob
import time

from . import temperature


class Read:
    '''
    Class to read temperature and humidity off of the Raspberry Pi temperature sensor
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.temp_c = 0
        self.temp_f = 0

        self.base_dir = '/sys/bus/w1/devices/'
        self.device_folder = glob.glob(self.base_dir + '28*')[0]
        self.device_file = self.device_folder + '/w1_slave'

        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

    def read_temp_raw(self):
        '''
        TODO: Needs documentation
        '''
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        '''
        TODO: Needs documentation
        '''
        lines = self.read_temp_raw()

        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        
        equals_pos = lines[1].find('t=')
        
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
        
            result = temperature.Temperature(temp_c, temp_f)
            return result
    
    def read_temperature(self):
        '''
        Method to read temperature and humidity

        NOTE: DEPRECATED, DO NOT USE
        '''
        try:
            # store temp and humid in variables
            # [temp, hum] = grovepi.dht(self.temp_sensor, self.humid_sensor)

            # placeholder stuff
            temp = 0
            hum = 0

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


        
