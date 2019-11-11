import time

import coin as c
import bin as b
import math


class DitheringBinning:
    def __init__(self):
        self.coins = []
        self.bins = []
        self.start_range = None
        self.end_range = None
        self.bin_count = 0

    def setup_coins(self, values, weight):
        for i in range(0, len(values)):  # Making Coins
            value = values[i]
            if value or not math.isnan(value):
                coin = c.Coin(value, weight[i], i)
                self.coins.append(coin)
                if self.start_range is None or self.start_range > value:
                    self.start_range = value
                if self.end_range is None or self.end_range < value:
                    self.end_range = value

    def setup_bins(self, labels, count):
        self.bin_count = count
        for i in range(0, count):
            empty_bin = b.Bin(labels[i])
            self.bins.append(empty_bin)

    def distribution_by_value(self, coin_list, bin_list):
        split = int((self.end_range - self.start_range) / self.bin_count)

        for coin in coin_list:
            fit = int((coin.get_value() - self.start_range) / split)
            if fit == split:
                bin_list[fit-1].add_coin(coin)
            else:
                bin_list[fit].add_coin(coin)

    def binning(self, x, weight, bin_label, bin_count):
        self.setup_coins(x, weight)
        self.setup_bins(bin_label, bin_count)
        self.distribution_by_value(self.coins,self.bins)




if __name__ == "__main__":
    start_time = time.time()

    x = [1,2,3,4,5,6,7,8,9,10]
    weights = [1,1,1,1,1,1,1,1,1,1]
    bl = ['b1', 'b2', 'b3']
    bc = len(bl)

    db = DitheringBinning()
    db.binning(x, weights, bl, bc)
    for bin in db.bins:
        print(bin.get_label())
        for coin in bin.get_coins():
            print(coin.get_value())


    end_time = time.time()
    print("Total time to run this program: " + str(end_time-start_time) + " seconds")
