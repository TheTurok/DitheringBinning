import unittest
import DitheringBinning as db


class TestDitheringBinning(unittest.TestCase):
    """Testing Dithering Binning functions"""

    def setUp(self):
        self.the_bins = db.DitheringBinning()
        self.x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.weight = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.labels = ['b1', 'b2', 'b3']
        self.label_length = len(self.labels)

    def test_setup_coins(self):
        self.the_bins.setup_coins([], [])  # empty test
        self.assertEqual(0, self.the_bins.total_weight)
        self.assertEqual(0, len(self.the_bins.coin_list))

        self.assertRaises(ValueError, self.the_bins.setup_coins, [1, 2], [0])  # test uneven weights and values

        self.the_bins.setup_coins(self.x, self.weight)
        self.assertEqual(9, self.the_bins.total_weight)
        for i in range(0, 9):
            self.assertEqual(i, self.the_bins.coin_list[i].value)


    def test_setup_bins(self):
        self.the_bins.setup_bins([], 0, 0)  # empty test
        self.assertEqual(0, len(self.the_bins.bins))
        self.assertEqual(0, len(self.the_bins.label))

        #self.binning.setup_bins(self.labels, self.label_length, len(self.x))
        #self.assertEqual(0, len(self.binning.bins))
        #self.assertEqual(0, len(self.binning.label))





if __name__ == '__main__':
    unittest.main()