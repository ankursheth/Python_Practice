
def reverse_string(s):

    reverse_str = ""

    index = len(s)

    while index > 0:
        reverse_str += s[index-1]
        index = index -1
        print(reverse_str)

reverse_string("Hello World")

