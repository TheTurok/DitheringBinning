import os
import time

import coin as c


def setup_coins(x, weight):
    coins = []

    for i in range(0, len(x)):  # Making Coins
        coin = c.Coin(x[i], weight[i], i)
        coins.append(coin)


def binning(x, weight, labels, bin_count):
    labeling = []
    setup_coins(x, weight)


if __name__ == "__main__":
    start_time = time.time()

    x = [1,2,3,4,5,6,7,8,9,10]
    weights = [1,1,1,1,1,1,1,1,1,1]
    labels = ['b1', 'b2', 'b3']
    bin_count = len(labels)
    binning(x, weights, labels, bin_count)

    end_time = time.time()
    print("Total time to run this program: " + str(end_time-start_time) + " seconds")
