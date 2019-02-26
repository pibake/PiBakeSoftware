class Temperature(object):
    def __init__(self, temp, humid):
        self.temp = temp
        self.humid = humid

    def current_reading(self):
        print(f"Current temperature: {self.temp}")
        print(f"Current humidity: {self.humid}")

    def get_temp(self):
        return self.temp

    def get_humid(self):
        return self.humid