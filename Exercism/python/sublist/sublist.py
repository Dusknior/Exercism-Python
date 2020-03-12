SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)


def sublist(first_list, second_list):
    if first_list == second_list:
        return EQUAL
    if first_list in _slices(second_list, len(first_list)):
        return SUBLIST
    if second_list in _slices(first_list, len(second_list)):
        return SUPERLIST
    return UNEQUAL


def _slices(lst, length):
    return (lst[i:i+length] for i in range(len(lst) - length + 1))
