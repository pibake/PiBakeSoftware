# Model for temperature/humidity reading
# Written by Wyatt J. Miller

import time
import datetime

'''
Model class for the temmperature, humidity, and the date and time it was read
'''
class Temperature:
    '''
    Contructor method
    '''
    def __init__(self, temp, humid):
        self.temp = temp
        self.humid = humid

        self.time = time.time()
        self.date = str(datetime.date.today())

    '''
    Get the current temperature, humidity, time in Epoch, and date; for debugging only
    '''
    def current_reading(self):
        print("Current temperature: ".format(self.temp)) # pylint: disable=too-many-format-args
        print("Current humidity: ".format(self.humid)) # pylint: disable=too-many-format-args
        print("Time stamped: ".format(self.time)) # pylint: disable=too-many-format-args
        print("Date stamped: ".format(self.date)) # pylint: disable=too-many-format-args

    '''
    Get the current date; for debugging only
    '''
    def current_date(self):
        print(datetime.date.today())

    '''
    Get the current temperature; for debugging only
    '''
    def get_temp(self):
        return self.temp
    '''
    Get the current humidity; for debugging only
    '''
    def get_humid(self):
        return self.humid