from rich import print, inspect
from thermostat_class import *


def main():
    t = Thermostat()
    try:
        t.temperature = 22.5
        #inspect(t, private=True, methods=True)
    except:
        print("Invalid Value")
    else:
        print(f"The temperature now is {t.ftemperature}")

if __name__ == "__main__":
    main()