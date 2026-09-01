from rich import print

class Rectangle:
    def __init__(self, base:float=1, height:float=1):
        self._base = None
        self._height = None
        self._area = None
        self.base = base
        self.height = height

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        if value < 0:
            raise ValueError("Invalid value.")
        if not isinstance(value, (int, float)):
            raise TypeError("Value have to be a number.")
        else:
            self._base = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value have to be a number.")
        if value < 0:
            raise ValueError("Invalid. Value must be positive.")
        else:
            self._height = value

    @property
    def area(self):
        return self._base * self._height

    @area.setter
    def area(self):
        raise PermissionError("You cannot override the area.")

    @property
    def dimensions(self):
        return f'''Base = {self.base} \nHeight = {self.height} \nArea = {self.area}'''

    @dimensions.setter
    def dimensions(self, values:tuple):
        if not isinstance(values, tuple):
            raise TypeError("The values must be inside a tuple.")
        if isinstance(values[0], (int, float)):
            if values[0] > 0:
                self.base = values[0]
        else:
            raise TypeError("Value have to be a number and positive.")
        if isinstance(values[1], (int, float)):
            if values[1] > 0:
                self.height = values[1]
        else:
            raise TypeError("Value have to be a number and positive.")


