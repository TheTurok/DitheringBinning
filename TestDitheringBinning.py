import unittest
import DitheringBinning as db


class TestDitheringBinning(unittest.TestCase):
    """Testing Dithering Binning functions"""

    def setUp(self):
        self.db_object = db.DitheringBinning()
        self.x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.weights = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.labels = ['b1', 'b2', 'b3']
        self.label_length = len(self.labels)

    def test_setup_coins(self):
        """Testing setup_coins function"""
        self.db_object.setup_coins([], [])  # empty test
        self.assertEqual(0, self.db_object.total_weight)
        self.assertEqual(0, len(self.db_object.coin_list))

        self.assertRaises(ValueError, self.db_object.setup_coins, [1, 2], [0])  # test uneven weights and values

        self.db_object.setup_coins(self.x, self.weights)
        self.assertEqual(9, self.db_object.total_weight)
        for i in range(0, 9):
            self.assertEqual(i, self.db_object.coin_list[i].value)

    def test_setup_bins(self):
        """Testing setup bins function"""
        self.assertRaises(ValueError, self.db_object.setup_bins, [], 0, 0)  # empty test

        self.db_object.setup_bins(self.labels, self.label_length, len(self.x))
        self.assertEqual(3, len(self.db_object.bins))  # Check lengths
        self.assertEqual(9, len(self.db_object.label))

        self.assertEqual('b1', self.db_object.bins[0].label)  # Check Bin Label
        self.assertEqual('b2', self.db_object.bins[1].label)
        self.assertEqual('b3', self.db_object.bins[2].label)

    def test_distribution_by_value(self):
        """Testing distribution_by_value function"""
        self.db_object.setup_coins(self.x, self.weights)
        self.db_object.setup_bins(self.labels, self.label_length, len(self.x))
        self.db_object.distribution_by_value()

        self.assertTrue(coin.value == 0 for index, coin in self.db_object.bins[0].coins)
        self.assertTrue(coin.value == 1 for index, coin in self.db_object.bins[0].coins)
        self.assertTrue(coin.value == 2 for index, coin in self.db_object.bins[1].coins)
        self.assertTrue(coin.value == 3 for index, coin in self.db_object.bins[1].coins)
        self.assertTrue(coin.value == 4 for index, coin in self.db_object.bins[2].coins)
        self.assertTrue(coin.value == 5 for index, coin in self.db_object.bins[2].coins)
        self.assertTrue(coin.value == 6 for index, coin in self.db_object.bins[2].coins)
        self.assertTrue(coin.value == 7 for index, coin in self.db_object.bins[2].coins)
        self.assertTrue(coin.value == 8 for index, coin in self.db_object.bins[2].coins)

    def test_inverse_distribution_by_value(self):
        """Test db in values in reversed order"""
        self.x.reverse()
        self.db_object.setup_coins(self.x, self.weights)
        self.db_object.setup_bins(self.labels, self.label_length, len(self.x))
        self.db_object.distribution_by_value()

        self.assertTrue(coin.value == 0 for index, coin in self.db_object.bins[0].coins)
        self.assertTrue(coin.value == 1 for index, coin in self.db_object.bins[0].coins)
        self.assertTrue(coin.value == 2 for index, coin in self.db_object.bins[1].coins)
        self.assertTrue(coin.value == 3 for index, coin in self.db_object.bins[1].coins)
        self.assertTrue(coin.value == 4 for index, coin in self.db_object.bins[2].coins)
        self.assertTrue(coin.value == 5 for index, coin in self.db_object.bins[2].coins)
        self.assertTrue(coin.value == 6 for index, coin in self.db_object.bins[2].coins)
        self.assertTrue(coin.value == 7 for index, coin in self.db_object.bins[2].coins)
        self.assertTrue(coin.value == 8 for index, coin in self.db_object.bins[2].coins)

    def test_negative_distribution_by_value(self):
        """DB with negative value added."""
        self.x.append(-10)
        self.weights.append(1)
        self.db_object.setup_coins(self.x, self.weights)
        self.db_object.setup_bins(self.labels, self.label_length, len(self.x))
        self.db_object.distribution_by_value()

    def test_dithering_balancd_values(self):
        """Normal values to test"""
        self.db_object.binning(self.x, self.weights, self.labels, self.label_length)
        self.assertTrue(coin.value == 0 for index, coin in self.db_object.bins[0].coins)
        self.assertTrue(coin.value == 1 for index, coin in self.db_object.bins[0].coins)
        self.assertTrue(coin.value == 2 for index, coin in self.db_object.bins[0].coins)
        self.assertTrue(coin.value == 3 for index, coin in self.db_object.bins[1].coins)
        self.assertTrue(coin.value == 4 for index, coin in self.db_object.bins[1].coins)
        self.assertTrue(coin.value == 5 for index, coin in self.db_object.bins[1].coins)
        self.assertTrue(coin.value == 6 for index, coin in self.db_object.bins[2].coins)
        self.assertTrue(coin.value == 7 for index, coin in self.db_object.bins[2].coins)
        self.assertTrue(coin.value == 8 for index, coin in self.db_object.bins[2].coins)

    def test_db_inbalance(self):
        """Inbalance of weight on one side"""
        for i in range(0, 3):
            self.x.append(i+8)
            self.weights.append(3)
        self.db_object.binning(self.x, self.weights, self.labels, self.label_length)

        for i in range(0, self.label_length):
            self.assertTrue(self.db_object.bins[i].weight == 6)

    def test_db_zero_weights(self):
        """" Test with values and weight staggered but each have even amount of weight

        """
        self.x = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
        self.weights = [0] * len(self.x)
        self.db_object.binning(self.x, self.weights, self.labels, self.label_length)
        for i in range(0, self.label_length):
            self.assertTrue(len(self.db_object.bins[i]) == 5)

    def test_db_stagger_weights(self):
        """" Test with values and weight staggered but each have even amount of weight

        """
        self.x = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
        self.weights = [10, 6, 4, 2, 1, 1, 1, 1, 1, 1, 1, 2, 4, 6, 10]
        self.db_object.binning(self.x, self.weights, self.labels, self.label_length)


if __name__ == '__main__':
    unittest.main()