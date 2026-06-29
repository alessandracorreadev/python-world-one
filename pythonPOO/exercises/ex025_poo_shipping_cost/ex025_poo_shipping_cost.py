from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, distance):
        self.distance = distance
        self.shipping_cost = 0

    @abstractmethod
    def calculate_shipping(self):
        pass

class Truck(Vehicle):
    factor = 1.20

    def __init__(self, distance):
        super().__init__(distance)

    def calculate_shipping(self):
        if self.distance >= 50:
            self.shipping_cost = self.distance * Truck.factor
            return f"${self.shipping_cost:.2f}"
        else:
            return f"Minimum distance is 50km."

class Motorcycle(Vehicle):
    factor = 1.20

    def __init__(self, distance):
        super().__init__(distance)

    def calculate_shipping(self):
        self.shipping_cost = self.distance * Truck.factor
        return f"${self.shipping_cost:.2f}"

class Drone(Vehicle):
    factor = 1.20

    def __init__(self, distance):
        super().__init__(distance)

    def calculate_shipping(self):
        if self.distance <= 10:
            self.shipping_cost = self.distance * Truck.factor
            return f"${self.shipping_cost:.2f}"
        else:
            return f"Maximum distance is 10km."