"""
compare two lists and test the following two points:

1) Lists length is equal
2) Elements are equal and in the sam position of the list

"""


def are_elements_equal(list_01, list_02):
    for index in range(len(list_01)):
        if list_01[index] != list_02[index]:
            return False
    return True


def are_list_equal(list_01, list_02):
    pass
