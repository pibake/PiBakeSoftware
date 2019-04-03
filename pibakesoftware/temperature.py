# Model for temperature/humidity reading
# Written by Wyatt J. Miller

import time
import datetime

class Temperature:
    '''
    Model class for the temperature, humidity, and the date and time it was read
    '''

    def __init__(self, temp_celsius, temp_fahrenheit):
        '''
        Constructor method
        '''
        self.temp_celsius = temp_celsius
        self.temp_fahrenheit = temp_fahrenheit

        self.time = str(datetime.datetime.now().time)
        self.date = str(datetime.date.today())

    def current_reading(self):
        '''
        Get the current temperature, humidity, time in Epoch, and date; for debugging only
        '''
        print("Current temperature (C): ".format(self.temp_celsius)) # pylint: disable=too-many-format-args
        print("Current temperature (F): ".format(self.temp_fahrenheit)) # pylint: disable=too-many-format-args
        print("Time stamped: ".format(self.time)) # pylint: disable=too-many-format-args
        print("Date stamped: ".format(self.date)) # pylint: disable=too-many-format-args


    def current_date(self):
        '''
        Get the current date; for debugging only
        '''
        print(datetime.date.today())

    def get_temp_celsius(self):
        '''
        Get the current temperature in celsius; for debugging only
        '''
        return self.temp_celsius

    def get_temp_fahrenheit(self):
        '''
        Get the current temperature in fahrenheit; for debugging only
        '''
        return self.temp_fahrenheit
