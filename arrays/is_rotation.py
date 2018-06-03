def is_rotation(list1, list2):
    if len(list1) != len(list2):
        return False

    i = 0
    if list1[i] not in list2:
        return False
    j = list2.index(list1[i])
    while i < len(list1):
        if list1[i] != list2[j % len(list2)]:
            return False
        j += 1
        i += 1
    return True

if __name__ == '__main__':
    assert(is_rotation([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7, 8, 1, 2, 3]) == False)
    assert(is_rotation([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7, 1, 2, 3]) == True)
    assert(is_rotation([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 9, 1, 2, 3]) == False)
    assert(is_rotation([1, 2, 3, 4, 5, 6, 7], [4, 6, 5, 7, 1, 2, 3]) == False)
    assert(is_rotation([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7, 0, 2, 3]) == False)
    assert(is_rotation([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]) == True)