
import unittest
from grades import (
    calculate_average,
    highest_mark,
    lowest_mark,
    get_result,
)


class TestStudentGrades(unittest.TestCase):

    def test_average(self):
        self.assertEqual(calculate_average([80, 90, 70]), 80)

    def test_highest(self):
        self.assertEqual(highest_mark([80, 90, 70]), 90)

    def test_lowest(self):
        self.assertEqual(lowest_mark([80, 90, 70]), 70)

    def test_pass(self):
        self.assertEqual(get_result([60, 70]), "PASS")

    def test_fail(self):
        self.assertEqual(get_result([30, 40]), "FAIL")

    def test_negative_marks(self):
        with self.assertRaises(ValueError):
            calculate_average([-10, 80])

    def test_marks_above_100(self):
        with self.assertRaises(ValueError):
            calculate_average([110, 90])

    def test_empty_marks(self):
        with self.assertRaises(ValueError):
            calculate_average([])


if __name__ == "__main__":
    unittest.main()
