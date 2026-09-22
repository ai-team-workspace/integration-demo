import unittest
from cart import summarize_cart


class CartTests(unittest.TestCase):
    def test_multiple_items(self):
        self.assertEqual(summarize_cart([10, 20]), {'item_count': 2, 'total': 30, 'average_price': 15})

    def test_single_item(self):
        self.assertEqual(summarize_cart([12.5]), {'item_count': 1, 'total': 12.5, 'average_price': 12.5})


if __name__ == '__main__':
    unittest.main()
