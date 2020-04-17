"""
compare two lists and test the following two points:

1) Equal lenght
2) Elements are equal at the same position in each list

"""


class ListComparator(object):
    def __init__(self, list_01, list_02):
        self.list_01 = list_01
        self.list_02 = list_02

    def are_elements_equal(self):
        return self.list_01 == self.list_02

    def are_list_equal_len(self):
        return self.list_01 == self.list_02

    def are_list_equal(self):
        return self.list_01 == self.list_02
