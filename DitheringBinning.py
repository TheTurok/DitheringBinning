import time

import coin as c
import bin as b
import math


class DitheringBinning:
    """Class to distribute the coins in their appropriate bins according to its weight and values.

    Attributes:
        coin_list (list: coin object): A list to hold values and weights after it has been converted to coins.
        bins (list: bin object): A list of bins to distribute the coins into
        start_range (int): The lowest value of a coin
        end_range (int): The highest value of a coin
        label (list: str): The output on the distribution of coins into certain bins
        total_weight (int): total weight of all coins
        bin_count (int): Number of bins
    """

    def __init__(self):
        self._coin_list = []
        self._bins = []
        self._min_value = None
        self._max_value = None
        self._label = []
        self._total_weight = 0  # NOT USING CURRENTLY
        self._bin_count = 0   # NOT USING CURRENTLY

    @property
    def bins(self):
        """:obj:'list' of :obj:'bin': Property of DB bin list"""
        return self._bins

    @property
    def coin_list(self):
        """:obj:'list' of :obj:'coin': Property of DB coin list"""
        return self.coin_list

    @property
    def min_value(self):
        """int: Property of DB min value"""
        return self._min_value

    @min_value.setter
    def min_value(self, value):
        self._min_value = value

    @property
    def max_value(self):
        """int: Property of DB max value"""
        return self._max_value

    @max_value.setter
    def max_value(self, value):
        self._max_value = value

    def _setup_coins(self, values, weight):
        """Turn the input of values and weight into coins

        set values for the min and max range for values

        Args:
            values: the input values
            weight: the weight of each value
        """
        for i in range(0, len(values)):  # Making Coins
            value = values[i]
            if value or not math.isnan(value):
                coin = c.Coin(value, weight[i], i)
                self._coin_list.append(coin)
                if self._min_value is None or self._min_value > value:
                    self._min_value = value
                if self._max_value is None or self._max_value < value:
                    self._max_value = value

    def _setup_bins(self, labels, count):
        """Setup empty bins with appropriate labels

        Args:
            labels: list of labels for the bins
            count: the number of bins
        """
        self._bin_count = count
        for i in range(0, count):
            empty_bin = b.Bin(labels[i])
            self._bins.append(empty_bin)

    def distribution_by_value(self, coin_list, bin_list):
        """Distribute coins into bins according to its value

        Args:
            coin_list: list of coins
            bin_list: list of nins
        """
        split = int((self._max_value - self._min_value) / self._bin_count)

        for cl in coin_list:
            fit = int((cl.value - self._min_value) / split)
            if fit == split:
                bin_list[fit-1].add_coin(cl)
            else:
                bin_list[fit].add_coin(cl)

    def dithering_balance(self, bins):
        """Balance the weight in each bin by moving coins around

        Using Dithering, choosing the min/max value of each bins with random weight until the weights are close to
        being evenly distributed.

        Args:
            bins: list of bins that hold coins
        """

        return bins

    def binning(self, x, weight, bin_label, bin_count):
        """Distribute coins into bins according to its value
            TODO
            TODO
            TODO
        Args:
            coin_list: list of coins
            bin_list: list of nins
        """
        self._setup_coins(x, weight)
        self._setup_bins(bin_label, bin_count)
        self.distribution_by_value(self._coin_list, self._bins)  # Distribute by value initially

        self.dithering_balance(self.bins)


if __name__ == "__main__":
    start_time = time.time()

    x = [1,2,3,4,5,6,7,8,9,10]
    weights = [1,1,1,1,1,1,1,1,1,1]
    bl = ['b1', 'b2', 'b3']
    bc = len(bl)

    db = DitheringBinning()
    db.binning(x, weights, bl, bc)
    for bin in db.bins:
        print(bin.label)
        for coin in bin.coins:
            print(coin.value)

    end_time = time.time()
    print("Total time to run this program: " + str(end_time-start_time) + " seconds")
