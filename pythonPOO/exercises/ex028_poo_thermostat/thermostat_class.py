# Thermostat with a temperature range of 16°C to 30°C in 0.5°C increments.

class Thermostat:
    def __init__(self):
        self.__temperature = 24

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < 16:
             self.__temperature = 16
        elif value > 30:
            self.__temperature = 30
        elif value % 0.5 == 0:
            self.__temperature = value
        else:
            raise ValueError(f"Invalid value.")


    @property
    def ftemperature(self):
        return f"{self.__temperature}°C"



