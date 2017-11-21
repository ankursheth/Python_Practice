

def pangram(s):

    List = []

    for l in range(26):
        List.append(False)

    for L in (s.replace(" ", "").lower()):
        if not L == " ":
            List[ord(L) - ord('a')] = True

    for c in List:
        if c == False:
            return False
    return True

s = "The quick brown fox jumps over the little lazy dog"
s1 = " Hello world "

if pangram(s):
    print(s + " " + "is a pangram")
else:
    print(s + " " + "is not a pangram")

if pangram(s1):
    print(s1 + " " + "is a pangram")
else:
    print(s1 + " " + "is not a pangram")
