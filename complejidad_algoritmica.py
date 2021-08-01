import time
import sys


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def factorial_r(m):
    if m == 1:
        return 1
    return m * factorial_r(m-1)

if __name__ == '__main__':
    sys.setrecursionlimit(150000)
    print(sys.getrecursionlimit())
    n = 100

    # comienzo = time.time()
    # factorial(n)
    # final = time.time()
    # print(final - comienzo)

    comienzo1 = time.time()
    factorial_r(n)
    final1 = time.time()
    print(final1 - comienzo1)

