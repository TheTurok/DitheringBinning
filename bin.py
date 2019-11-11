class Bin:
    """Bins to hold coin values.

    Attributes:
        label (str): Bin's label
        weight (int): Bin's weight, coin's total weight
        coins (list: coin object): The coins inside this bin
    """

    def __init__(self, label):
        self._label = label
        self._weight = 0
        self._coins = []

    @property
    def label(self):
        """str: Property of bin's label"""
        return self._label

    def add_coin(self, coin):
        self._weight += coin.weight
        self._coins.append(coin)

    @property
    def coins(self):
        """:obj:'list' of :obj:'coin': Property of bin's coins"""
        return self._coins

    @property
    def weight(self):
        """int: Property of the bin's weight, total amount of coin's weights"""
        return self._weight
