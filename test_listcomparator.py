import unittest

from compare_two_lists import ListComparator


class ListComparatorTest(unittest.TestCase):
    def setUp(self):
        list_01 = ["1", "2", 3]
        list_02 = ["1", "2", 3]
        list_03 = []
        list_04 = ["1", 3, "2"]
        self.listcomparator = ListComparator(list_01, list_02)
        self.listcomparator_different = ListComparator(list_01, list_03)
        self.listcomparator_different_position = ListComparator(list_01, list_04)

    def test_lists_length(self):
        is_equal_lenth = self.listcomparator.are_list_equal_len()
        self.assertEqual(True, is_equal_lenth)

    def test_are_elements_equal(self):
        are_elements_equal = self.listcomparator.are_elements_equal()
        self.assertEqual(True, are_elements_equal)

    def test_are_elements_not_equal(self):
        elements_not_equal = self.listcomparator_different.are_elements_equal()
        self.assertEqual(False, elements_not_equal)

    def test_different_position(self):
        different_position = self.listcomparator_different_position.are_list_equal()
        self.assertEqual(False, different_position)
