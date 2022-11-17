
def fibonacci(n):
    fib1 = fib2 = 1
    fib_list = []
    while n > 0:
        fib_list.append(fib1)
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    return fib_list


def sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def calculator(a, b, sign):
    if (sign == "+"):
        return a+b
    elif (sign == "-"):
        return a-b
    elif (sign == "*"):
        return a*b
    elif (sign == "/"):
        return a/b