"""
compare two lists and test the following two points:

1) Equal lenght
2) Elements are equal at the same position in each list

"""


class ListComparator(object):
    def is_equal_len(self, list_01, list_02):
        return len(list_01) == len(list_02)

    def are_list_equal(self, list_01, list_02):
        return list_01 == list_02

    def are_elements_equal(self, list_01, list_02):
        if not self.is_equal_len(list_01, list_02):
            return False
        elif len(list_01) == 0 and len(list_02) == 0:
            return True
        else:
            for index in range(len(list_01)):
                if list_01[index] != list_02[index]:
                    return False
        return True
