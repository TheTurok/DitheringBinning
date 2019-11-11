

class Bin:
    def __init__(self, label):
        self.label = label
        self.total_weight = 0
        self.coins = []

    def add_coin(self, coin):
        self.total_weight += coin.get_weight()
        self.coins.append(coin)

    def get_coins(self):
        return self.coins

    def get_label(self):
        return self.label

    def get_total_weight(self):
        return self.total_weight
