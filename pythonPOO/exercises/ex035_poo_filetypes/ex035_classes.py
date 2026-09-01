from abc import ABC

class File(ABC):
    def __init__(self, name:str, size:float, extension):
        self.__name = name
        self._extension:str = extension
        self._size = size
        self._complete_name:str = f"'{self.__name}.{self._extension}'({self.size:.2f}MB)"

    @property
    def size(self):
        return self._size / 1_000_000

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("Size cannot be negative.")
        else:
            self._size = value

    @property
    def complete_name(self):
        return self._complete_name

    def open_file(self):
        print(f"Opening the file: {self.complete_name} on ", end='')


class Doc(File):
    def __init__(self, name, size):
        super().__init__(name, size, extension = "doc")

    def open_file(self):
        super().open_file()
        print("Microsoft Word")


class Pdf(File):
    def __init__(self, name, size):
        super().__init__(name, size, extension = "pdf")

    def open_file(self):
        super().open_file()
        print("Adobe Reader")