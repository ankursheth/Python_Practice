
def sentence_reversal1(s):
    print(" ".join(reversed(s.split())))


def sentence_reversal2(s):
    print(" ".join(s.split()[::-1]))


def initial_sentence(s):

    words = []
    length = len(s)
    spaces = [' ']
    i = 0

    while i < length:

        if s[i] not in spaces:
            word_start = i

            while i < length and s[i] not in spaces:
                i += 1

            words.append(s[word_start:i])

        i += 1
    return words
    # print(" ".join(reversed(words)))


def final_reversal(word_lst):
    new_list = []
    index = 0
    while index < len(word_lst):
        new_list.append(word_lst[len(word_lst) - 1 - index])
        index = index + 1
    print(" ".join(new_list))


s1 = "host Your am I"
sentence_reversal1(s1)

s2 = " come Wel"
sentence_reversal2(s2)

s3 = " World Hello"
lst = initial_sentence(s3)
final_reversal(lst)
