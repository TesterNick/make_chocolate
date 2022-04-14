import unittest

from make_chocolate import make_chocolate, validate


class TestMakeChocolate(unittest.TestCase):

    def test_package_can_be_made_with_exact_amounts_of_small_bars(self):
        """ Function works correctly with only small bars """
        amount = make_chocolate(7, 0, 7)
        self.assertEqual(amount, 7)

    def test_package_can_be_made_with_minimal_amount_of_bars(self):
        """ Function works correctly with exact amount of small and big bars """
        amount = make_chocolate(2, 1, 7)
        self.assertEqual(amount, 2)

    def test_package_can_be_made_with_only_big_bars(self):
        """ Function works correctly without small bars """
        amount = make_chocolate(0, 1, 5)
        self.assertEqual(amount, 0)

    def test_package_can_be_made_with_exceeding_amount_of_small_bars(self):
        """ Function works correctly with too much small bars """
        amount = make_chocolate(15, 1, 7)
        self.assertEqual(amount, 2)

    def test_package_can_be_made_with_exceeding_amount_of_big_bars(self):
        """ Function works correctly with too much big bars """
        amount = make_chocolate(2, 15, 2)
        self.assertEqual(amount, 2)

    def test_package_can_not_be_made_with_shortage_of_small_bars(self):
        """ Function works correctly with too less small bars """
        amount = make_chocolate(2, 2, 3)
        self.assertEqual(amount, -1)

    def test_package_can_not_be_made_with_shortage_of_bars(self):
        """ Function works correctly with too much big bars """
        amount = make_chocolate(1, 1, 7)
        self.assertEqual(amount, -1)


class TestValidate(unittest.TestCase):

    def test_package_can_not_be_made_with_non_numeric_amount_of_bars(self):
        """ Function throws ValueError on incorrect input """
        self.assertRaises(ValueError, validate, "")

    def test_package_can_not_be_made_with_negative_amount_of_bars(self):
        """ Function throws RuntimeError on negative input """
        self.assertRaises(RuntimeError, validate, -1)


if __name__ == '__main__':
    unittest.main()
