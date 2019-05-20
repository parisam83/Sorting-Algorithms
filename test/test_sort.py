from algorithms.sort import (
    insertion_sort_slow,
    insertion_sort_fast
)

import unittest


class TestSuite(unittest.TestCase):

    def test_insertion_sort_slow(self):
        self.assertEqual([1, 5, 23, 57, 65, 1232],
                         insertion_sort_slow([1, 5, 65, 23, 57, 1232]))
    
    def test_insertion_sort_fast(self):
        self.assertEqual([1, 5, 23, 57, 65, 1232],
                         insertion_sort_fast([1, 5, 65, 23, 57, 1232]))


if __name__ == "__main__":
    unittest.main()
