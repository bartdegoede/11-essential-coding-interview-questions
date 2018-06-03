def non_repeating(s):
    if not s:
        return None

    frequencies = {}
    for c in s:
        if c not in frequencies:
            frequencies[c] = 0
        frequencies[c] += 1

    # this is ugly, but still O(N)
    for c in s:
        if frequencies[c] == 1:
            return c


if __name__ == '__main__':
    assert(non_repeating('abcab') == 'c')
    assert(non_repeating('abab') == None)
    assert(non_repeating('aabbbc') == 'c')
    assert(non_repeating('aabbdbc') == 'd')
