

def anagram0(s1, s2):

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return (sorted(s1) == sorted(s2))


def anagram1(s1, s2):

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for L in s1:
        if L in count:
            count[L] += 1
        else:
            count[L] = 1

    for L in s2:
        if L in count:
            count[L] -= 1
        else:
            count[L] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True

de1 = "true"
de2 = "eurt"
de3 = "Hello"
de4 = "world"

anagram0(de1, de2)
anagram1(de3, de4)
