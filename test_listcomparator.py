import unittest

from compare_two_lists import ListComparator


class ListComparatorTest(unittest.TestCase):
    def setUp(self):
        self.listcomparator = ListComparator()

    def test_lists_length(self):
        is_equal_lenth = self.listcomparator.is_equal_len([], [])
        self.assertTrue(is_equal_lenth)

    def test_are_elements_equal(self):
        are_elements_equal = self.listcomparator.are_elements_equal([1, 2], [1, 2])
        self.assertTrue(are_elements_equal)

    def test_are_elements_not_equal(self):
        elements_not_equal = self.listcomparator.are_elements_equal([], [1])
        self.assertFalse(elements_not_equal)

    def test_different_position(self):
        different_position = self.listcomparator.are_list_equal([1, 2], [2, 1])
        self.assertFalse(different_position)

    def test_empty_lists(self):
        self.assertTrue(self.listcomparator.are_list_equal([], []))


if __name__ == "__main__":
    unittest.main()
