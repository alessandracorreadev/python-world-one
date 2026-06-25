from abc import ABC, abstractmethod


class HotBeverage(ABC):
    def prepare(self):
        pass

    def boil_water(self):
        pass

    @abstractmethod
    def mix(self):
        pass

    @abstractmethod
    def serve(self):
        pass


class Espresso(HotBeverage):
    def mix(self):
        print("-" * 10 + "Starting preparation" + "-" * 10)
        print(f'''1. Boiling water to 100 degrees Celsius.
2. Passing pressurized water through the ground coffee.''')
        self.serve()

    def serve(self):
        print("3. Serving in a small cup.")
        print("-" * 10 + "Drink Ready" + "-" * 10)

class Tea(HotBeverage):
    def mix(self):
        print("-" * 10 + "Starting preparation" + "-" * 10)
        print('''1. Boiling water to 100 degrees Celsius.
2. Steeping a herbal tea bag in the water.''')
        self.serve()

    def serve(self):
        print("3. Serving in a porcelain mug with lemon.")
        print("-" * 10 + "Drink Ready" + "-" * 10)

class Latte(HotBeverage):
    def mix(self):
        print("-" * 10 + "Starting preparation" + "-" * 10)
        print('''1. Boiling water to 100 degrees Celsius.
2. Passing pressurized steam through the milk.''')
        self.serve()

    def serve(self):
        print("3. Serving in a large mug.")
        print("-"*10 + "Drink Ready" + "-"*10)

