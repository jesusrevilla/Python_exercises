import unittest

from compare_two_lists import ListComparator


class ListComparatorTest(unittest.TestCase):
    def setUp(self):
        self.list_01 = ["1", "2", 3]
        self.list_02 = ["1", "2", 3]
        self.list_03 = []
        self.list_04 = ["1", 3, "2"]
        self.listcomparator = ListComparator(self.list_01, self.list_02)

    def test_lists_length(self):
        is_equal_lenth = self.listcomparator.are_list_equal_len()
        self.assertEqual(True, is_equal_lenth)

    def test_are_elements_equal(self):
        are_elements_equal = self.listcomparator.are_elements_equal()
        self.assertEqual(True, are_elements_equal)

    def test_are_elements_not_equal(self):
        listcomparator_different = ListComparator(self.list_01, self.list_03)
        elements_not_equal = listcomparator_different.are_elements_equal()
        self.assertEqual(False, elements_not_equal)

    def test_different_position(self):
        self.listcomparator_different_position = ListComparator(
            self.list_01, self.list_04
        )
        different_position = self.listcomparator_different_position.are_list_equal()
        self.assertEqual(False, different_position)
