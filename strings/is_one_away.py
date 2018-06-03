def is_one_away_same_length(s1, s2):
    c = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            c += 1
        if c > 1:
            return False
    return True


def is_one_away_diff_length(s1, s2):
    i = 0
    c = 0
    while i < len(s2):
        if s1[i + c] == s2[i]:
            i += 1
        else:
            c += 1
            if c > 1:
                return False
    return True


def is_one_away(s1, s2):
    if abs(len(s1) - len(s2)) >= 2:
        return False
    elif len(s1) == len(s2):
        return is_one_away_same_length(s1, s2)
    else:
        if len(s1) > len(s2):
            return is_one_away_diff_length(s1, s2)
        else:
            return is_one_away_diff_length(s2, s1)


if __name__ == '__main__':
    assert(is_one_away('abcde', 'abcd') == True)
    assert(is_one_away('abde', 'abcde') == True)
    assert(is_one_away('a', 'a') == True)
    assert(is_one_away('abcdef', 'abqdef') == True)
    assert(is_one_away('abcdef', 'abccef') == True)
    assert(is_one_away('abcdef', 'abcde') == True)
    assert(is_one_away('aaa', 'abc') == False)
    assert(is_one_away('abcde', 'abc') == False)
    assert(is_one_away('abc', 'abcde') == False)
    assert(is_one_away('abc', 'bcc') == False)