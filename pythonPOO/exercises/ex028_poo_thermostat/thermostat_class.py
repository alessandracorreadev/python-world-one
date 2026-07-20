class Thermostat:
    def __init__(self):
        self.__temperature = 0

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value : int = 24):
        if value < 16:
            self.__temperature = 16
        elif value > 30:
            self.__temperature = 30
        elif value % 0.5 == 0:
            self.__temperature = value

    def ftemperature(self):
        return f"{self.temperature}°C"



