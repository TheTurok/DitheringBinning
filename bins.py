

class Bins:
    def __init__(self, label):
        self.label = label
        self.total_weight = 0
        self.coins = []

    def add_coin(self, coin):
        self.coins.append(coin)

    def get_coins(self):
        return self.coins

