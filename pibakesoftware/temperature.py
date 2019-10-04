# Model for temperature/humidity reading
# Written by Wyatt J. Miller, 2019

import os
import os.path
import time
import datetime
from . import uuid_gen

class Temperature:
    '''
    Synopsis:
    Model class for the temperature, humidity, date, time

    Details:
    Class for temperature modelling and other stats needed to be
    inserted into database. This includes celsisus and Fahrenheit temperatures,
    time and date stamps, and the UUID, used for identifying hardware.
    '''

    def __init__(self, temp_celsius, temp_fahrenheit):
        '''
        Synopsis:
        Constructor method

        Details:
        Instantiates two temperatures, time, date, and UUID attributes
        '''
        self.temp_celsius = temp_celsius
        self.temp_fahrenheit = temp_fahrenheit

        self.time = str(datetime.datetime.now().time())
        self.date = str(datetime.date.today())
        self.uuid = self.get_uuid()

    def current_reading(self):
        '''
        Synopsis:
        Current reading method

        Details:
        Get the current temperature, humidity, time in Epoch, and date; for debugging only.
        Developers can get individual statisics as well, labeled below.
        '''
        print("Current temperature (C): ".format(self.temp_celsius)) # pylint: disable=too-many-format-args
        print("Current temperature (F): ".format(self.temp_fahrenheit)) # pylint: disable=too-many-format-args
        print("Time stamped: ".format(self.time)) # pylint: disable=too-many-format-args
        print("Date stamped: ".format(self.date)) # pylint: disable=too-many-format-args


    def current_date(self):
        '''
        Synopsis:
        Current date method

        Details:
        Get the current date; for debugging only
        '''
        print(datetime.date.today())

    def get_temp_celsius(self):
        '''
        Synopsis:
        Current celsius temperature

        Details:
        Get the current temperature in celsius; for debugging only
        '''
        return self.temp_celsius

    def get_temp_fahrenheit(self):
        '''
        Synopsis:
        Current Fahrenheit temperature method

        Details:
        Get the current temperature in fahrenheit; for debugging only
        '''
        return self.temp_fahrenheit

    def get_uuid(self):
        '''
        Synopsis:
        Obtain UUID method

        Details:
        Obtain UUID from text file already generated.
        '''
        uuid = uuid_gen.Uuid()
        result = uuid.read_uuid_file()
        return result

