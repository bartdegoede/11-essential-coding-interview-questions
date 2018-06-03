def most_frequent(given_list):
    if not given_list:
        return None

    max_item = None
    max_count = -1
    frequencies = {}
    for item in given_list:
        if item not in frequencies:
            frequencies[item] = 0
        frequencies[item] += 1
        if frequencies[item] > max_count:
            max_count = frequencies[item]
            max_item = item
    return max_item

if __name__ == '__main__':
    assert(most_frequent([1, 3, 1, 3, 2, 1]) == 1)
    assert(most_frequent([3, 3, 1, 3, 2, 1]) == 3)
    assert(most_frequent([]) == None)
    assert(most_frequent([0]) == 0)