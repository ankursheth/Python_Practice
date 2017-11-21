
def string_compression(s):

    l = len(s)

    if l == 0:
        print("String is Empty")

    if l == 1:
        print(s+1)

    r = ""
    count = 1
    i = 1

    while i < l:
        if s[i] == s[i-1]:
            count += 1
        else:
            r = r + s[i-1] + str(count)
            count = 1
        i += 1
    r = r + s[i-1] + str(count)
    print(r)

s1 = "AAADDDCCCaaabsabffGG"
string_compression(s1)

