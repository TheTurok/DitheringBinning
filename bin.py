

class Bin:
    def __init__(self, label):
        self._label = label
        self._total_weight = 0
        self._coins = []

    @property
    def label(self):
        return self._label

    def add_coin(self, coin):
        self._total_weight += coin.weight
        self._coins.append(coin)

    @property
    def coins(self):
        return self._coins

    @property
    def total_weight(self):
        return self._total_weight
