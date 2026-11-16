
import unittest
from revenue import calculate_revenue

class TestRevenue(unittest.TestCase):

    def test_normal_sale(self):
        self.assertEqual(calculate_revenue(10, 5), 50)

    def test_zero_quantity(self):
        self.assertEqual(calculate_revenue(10, 0), 0)

if __name__ == "__main__":
    unittest.main()
