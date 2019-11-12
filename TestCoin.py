import unittest
import coin


class TestCoin(unittest.TestCase):
    """Testing Coin Class"""

    def test_coin(self):
        c = coin.Coin(1, 9)
        self.assertEqual(1, c.value)
        self.assertEqual(9, c.weight)


if __name__ == '__main__':
    unittest.main()