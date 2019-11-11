class Coin:
    """Coin Properties

    Attributes:
        value (int): Value of the coin.
        index (int): The index from where the coin came from
        weight (int): the weight of the coin
    """

    def __init__(self, value, weight, index):
        self._value = value
        self._index = index
        self._weight = weight

    @property
    def weight(self):
        """int: Property of coin's weight"""
        return self._weight

    @property
    def index(self):
        """int: Property of the index the coin came from"""
        return self.index

    @property
    def value(self):
        """int: Property of coin's value"""
        return self._value

