import unittest
import highly_divisible_triangular_number as hdtn


class HighlyDivisibleTriangularNumberTests(unittest.TestCase):

    def test_calc_triangle_number(self):
        self.assertEqual(1, hdtn.calc_triangle_number(1))
        self.assertEqual(3, hdtn.calc_triangle_number(2))
        self.assertEqual(6, hdtn.calc_triangle_number(3))
        self.assertEqual(10, hdtn.calc_triangle_number(4))
        self.assertEqual(15, hdtn.calc_triangle_number(5))
        self.assertEqual(21, hdtn.calc_triangle_number(6))
        self.assertEqual(28, hdtn.calc_triangle_number(7))
        self.assertEqual(36, hdtn.calc_triangle_number(8))
        self.assertEqual(45, hdtn.calc_triangle_number(9))
        self.assertEqual(55, hdtn.calc_triangle_number(10))

    def test_calc_factors(self):
        self.assertEqual([1], hdtn.calc_factors(1))
        self.assertEqual([1, 3], hdtn.calc_factors(3))
        self.assertEqual([1, 2, 3, 6], hdtn.calc_factors(6))
        self.assertEqual([1, 2, 5, 10], hdtn.calc_factors(10))
        self.assertEqual([1, 3, 5, 15], hdtn.calc_factors(15))
        self.assertEqual([1, 3, 7, 21], hdtn.calc_factors(21))
        self.assertEqual([1, 2, 4, 7, 14, 28], hdtn.calc_factors(28))

    def test_find_first_triangle_with_at_least_divisors(self):
        self.assertEqual((1, [1]), hdtn.find_first_triangle_with_at_least_divisors(1))
        self.assertEqual((2, [1, 2]), hdtn.find_first_triangle_with_at_least_divisors(2))
        self.assertEqual((4, [1, 2, 4]), hdtn.find_first_triangle_with_at_least_divisors(3))
        self.assertEqual((6, [1, 2, 3, 6]), hdtn.find_first_triangle_with_at_least_divisors(4))
        self.assertEqual((16, [1, 2, 4, 8, 16]), hdtn.find_first_triangle_with_at_least_divisors(5))
        self.assertEqual((12, [1, 2, 3, 4, 6, 12]), hdtn.find_first_triangle_with_at_least_divisors(6))
        self.assertEqual((64, [1, 2, 4, 8, 16, 32, 64]), hdtn.find_first_triangle_with_at_least_divisors(7))


if __name__ == '__main__':
    unittest.main()
