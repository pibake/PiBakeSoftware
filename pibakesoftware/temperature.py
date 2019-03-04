# Model for temperature/humidity reading
# Written by Wyatt J. Miller

import time
import datetime

class Temperature:
    '''
    Model class for the temmperature, humidity, and the date and time it was read
    '''

    def __init__(self, temp, humid):
        '''
        Contructor method
        '''
        self.temp = temp
        self.humid = humid

        self.time = time.time()
        self.date = str(datetime.date.today())

    def current_reading(self):
        '''
        Get the current temperature, humidity, time in Epoch, and date; for debugging only
        '''
        print("Current temperature: ".format(self.temp)) # pylint: disable=too-many-format-args
        print("Current humidity: ".format(self.humid)) # pylint: disable=too-many-format-args
        print("Time stamped: ".format(self.time)) # pylint: disable=too-many-format-args
        print("Date stamped: ".format(self.date)) # pylint: disable=too-many-format-args


    def current_date(self):
        '''
        Get the current date; for debugging only
        '''
        print(datetime.date.today())

    def get_temp(self):
        '''
        Get the current temperature; for debugging only
        '''
        return self.temp

    def get_humid(self):
        '''
        Get the current humidity; for debugging only
        '''
        return self.humid
