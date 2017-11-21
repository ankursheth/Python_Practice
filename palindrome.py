example = ["Asa", "eH e", "z", "0o0", "ret", "On0"]


def palindrome1(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace(" ", "")
    if len(sentence) <= 1:
        return True
    else:
        left = 0
        right = len(sentence) - 1
        while left <= right:
            if sentence[left] == sentence[right]:
                left += 1
                right -= 1
                return True
            else:
                return False
        return True


def palindrome2(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace(" ", "")
    if len(sentence) <= 1:
        return True
    else:
        if sentence[0] == sentence[-1]:
            new_word = sentence[1:-1]
            return palindrome1(new_word)
        else:
            return False


def palindrome3(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace(" ", "")
    if sentence == "".join(reversed(sentence)):
        return True
    else:
        return False


def palindrome4(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace(" ", "")
    if len(sentence) <= 1:
        return True
    else:
        for i in range(int(len(sentence)/2)):
            if sentence[i] != sentence[-(i+1)]:
                return False
            else:
                return True


def palindrome5(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace(" ", "")
    if len(sentence) <= 1:
        return True
    else:
        if sentence == sentence[::-1]:
            return True
        else:
            return False

for ex in example:
    if palindrome1(ex):
        print(ex)
        print("-"*10)
for ex in example:
    if palindrome2(ex):
        print(ex)
        print("*"*10)
for ex in example:
    if palindrome3(ex):
        print(ex)
        print("&"*10)
for ex in example:
    if palindrome4(ex):
        print(ex)
        print("#"*10)
for ex in example:
    if palindrome5(ex):
        print(ex)
        print("%"*10)
