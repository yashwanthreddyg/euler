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
    numToCheck = 5
    while True:
        if isprime(numToCheck):
            primeCount+=1
            if primeCount == num:
                return numToCheck
        numToCheck+=2

print main(10001)