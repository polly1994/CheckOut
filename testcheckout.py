import unittest
import unittest.mock

import math
import database
import product
import promotion
import setup
import checkout

class TestCheckout(unittest.TestCase):
    def setup(self):
        pass

    def test_PrintBasket(self):
        basket = []
        item = product.Product("CH1", 1, '', 3.11, 0)
        basket.append(item)
        item = product.Product("CF1", 1, 'BOGO', 11.23, -11.23)
        basket.append(item)
        item = product.Product("CF1", 2, '', 11.23, 0)
        basket.append(item)
        with unittest.mock.patch.object(setup, "GetBasket", return_value = basket):
            total = checkout.PrintBasket()
            self.assertEqual(total,14.34)


if __name__ == "__main__":
    unittest.main()