def unique1(s):
    print(len(set(s)) == len(s))


def unique2(s):
    alphabets = set()

    for alphabet in s:
        if alphabet in alphabets:
            print(False)
        else:
            alphabets.add(alphabet)
            print(True)

s1 = "Helo"
s2 = "Hello"
unique1(s1)
unique2(s2)
