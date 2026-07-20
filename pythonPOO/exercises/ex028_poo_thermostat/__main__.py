from rich import print, inspect
from thermostat_class import *


def main():
    t = Thermostat()
    t.temperature = 22.4
    inspect(t, private=True, methods=True)
    print(f"The temperature now is {t.ftemperature()}")

if __name__ == "__main__":
    main()