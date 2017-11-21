

def sum_pair(array, k):

    if len(array) < 2:
        return

    seen = set()
    output = set()

    for num in array:
        target = k - num

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num, target), max(num, target)))

    print('\n'.join(map(str, list(output))))

sum_pair([1, 2, 3, 4], 5)
