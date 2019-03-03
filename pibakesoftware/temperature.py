import time
import datetime

class Temperature:
    def __init__(self, temp, humid):
        self.temp = temp
        self.humid = humid

        self.time = time.time()
        self.date = str(datetime.date.today())

    def current_reading(self):
        print("Current temperature: ".format(self.temp)) # pylint: disable=too-many-format-args
        print("Current humidity: ".format(self.humid)) # pylint: disable=too-many-format-args
        print("Time stamped: ".format(self.time)) # pylint: disable=too-many-format-args
        print("Date stamped: ".format(self.date)) # pylint: disable=too-many-format-args

    def current_date(self):
        print(datetime.date.today())

    def get_temp(self):
        return self.temp

    def get_humid(self):
        return self.humid