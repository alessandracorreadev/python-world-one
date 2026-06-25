from abc import ABC, abstractmethod

class HotBeverage(ABC):
    def prepare(self):
        print("-" * 20 + "Starting preparation" + "-" * 20)
        self.boil_water()
        self.mix()
        self.serve()
        print("-" * 20 + "Drink Ready" + "-" * 20)

    def boil_water(self):
        print("1. Boiling water to 100 degrees Celsius.")

    @abstractmethod
    def mix(self):
        pass

    @abstractmethod
    def serve(self):
        pass


class Espresso(HotBeverage):
    def mix(self):
        print("2. Passing pressurized water through the ground coffee.")

    def serve(self):
        print("3. Serving in a small cup.")

class Tea(HotBeverage):
    def mix(self):
        print("2. Steeping a herbal tea bag in the water.")

    def serve(self):
        print("3. Serving in a porcelain mug with lemon.")

class Latte(HotBeverage):
    def mix(self):
        print("2. Passing pressurized steam through the milk.")

    def serve(self):
        print("3. Serving in a large mug.")

