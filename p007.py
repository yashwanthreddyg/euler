import math
def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def main(num):
    primeCount = 2
    if num == 1:
        return 2
    if num == 2:
        return 3
    #every prime can be represented as (6k +/- 1)
    k=1
    while True:
        numToCheck1 = 6*k - 1
        numToCheck2 = 6*k + 1
        if isprime(numToCheck1):
            primeCount+=1
        if primeCount == num:
            return numToCheck1

        if isprime(numToCheck2):
            primeCount+=1
        if primeCount == num:
            return numToCheck2
        k+=1


print main(10001)