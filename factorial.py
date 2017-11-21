num = int(input("Please enter the number to get the factorial"))


def factorial1(number):
    product = 1
    for i in range(number):
        product = product * (i+1)
    print(product)


def factorial2(number):
    if number == 1:
        return 1
    else:
        return number * factorial2(number-1)

factorial1(num)
print(factorial2(num))
