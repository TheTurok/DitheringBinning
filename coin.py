

class Coin:
    def __init__(self, value, weight, index):
        self.value = value
        self.index = index
        self.weight = weight

    def get_weight(self):
        return self.weight

    def get_index(self):
        return self.index

    def get_value(self):
        return self.value

