import collections


def finder1(arr1, arr2):

    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            print(num1)

    print(arr1[-1])


def finder2(arr1, arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            print(num)
        else:
            d[num] -= 1


def finder3(arr1, arr2):

    result = 0

    for num in arr1 + arr2:
        result ^= num
        print(result)

    return result

ar1 = [5, 2, 2, 3, 1]
ar2 = [1, 2, 2, 5]

finder1(ar1, ar2)
finder2(ar1, ar2)
finder3(ar1, ar2)
