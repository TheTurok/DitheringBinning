import unittest
import DitheringBinning as db
import coin
import bin


class TestDitheringBinning(unittest.TestCase):
    """Testing Dithering Binning functions"""

    def test_coin(self):
        c = coin.Coin(1, 9)
        self.assertEqual(c.value, 1)
        self.assertEqual(c.weight, 9)

    def test_bin(self):
        b = bin.Bin('test')
        self.assertEqual(b.label, 'test')
        c1 = coin.Coin(-1, 1)
        c2 = coin.Coin(1, 1)
        c3 = coin.Coin(None, 3)
        c4 = coin.Coin(float('nan'), 10)
        b.add_coin(c1, 0)
        self.assertEqual(len(b), 1)
        self.assertEqual(b.coins[0].value, -1)
        self.assertEqual(b.coins[0].weight, 1)
        b.add_coin(c3, 2)
        self.assertEqual(len(b), 1)
        self.assertRaises(ValueError, b.add_coin, c2, 0)  # test adding coin in same index




if __name__ == '__main__':
    unittest.main()