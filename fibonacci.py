def fibonacci1(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci1(number-1)+fibonacci1(number-2)


def fibonacci2(number):
    x, y = 1, 1
    for i in range(number-1):
        x, y = y, x+y
    return x


def fibonacci3():
    x, y = 1, 1
    while True:
        yield x
        x, y = y, x+y


for i in range(1, 10):
    print(fibonacci1(i), end=" ")
print()

for i in range(1, 300):
    print(fibonacci2(i), end=" ")
print()

n = 0
for i in fibonacci3():
    if n >= 15:
        break
    print(i, end=" ")
    n = n + 1
