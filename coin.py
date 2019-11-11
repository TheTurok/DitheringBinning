

class Coin:
    def __init__(self, value, weight, index):
        self._value = value
        self._index = index
        self._weight = weight

    @property
    def weight(self):
        return self._weight

    @property
    def index(self):
        return self.index

    @index.setter
    def index(self, index):
        self.index = index

    @property
    def value(self):
        return self._value

