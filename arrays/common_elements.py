def common_elements(a, b):
    common = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            common.append(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1
    return common

if __name__ == '__main__':
    assert(common_elements([1, 3, 4, 6, 7, 9], [1, 2, 4, 5, 9, 10]) == [1, 4, 9])
    assert(common_elements([1, 2, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]) == [1, 2, 9, 10, 12])
    assert(common_elements([0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]) == [])