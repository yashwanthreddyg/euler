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
    sumOfPrimes = 5
    #every prime can be represented as (6k +/- 1)
    k=1
    while True:
        numToCheck1 = 6*k - 1
        numToCheck2 = 6*k + 1

        if numToCheck1 > num:
            return sumOfPrimes
        if isprime(numToCheck1):
            sumOfPrimes+=numToCheck1

        if numToCheck2> num:
            return sumOfPrimes
        if isprime(numToCheck2):
            sumOfPrimes+=numToCheck2
        k+=1

# sievebound := (limit-1) div 2 // last index of sieve
# sieve := new boolean array [1 .. sievebound] false
# crosslimit := ((sqrt(limit))-1) div 2
# for i := 1 to crosslimit
#     if not sieve[i] then // 2*i+1 is prime, mark multiples
#         for j:= 2*i*(i+1) to sievebound with step 2*i+1
#             sieve[j] := true
#         end for
#     end if
# end for
# sum := 2 // 2 is prime
# for i := 1 to sievebound
#     if not sieve[i] then sum := sum+(2*i+1)
# end for
# output sum

# def main(limit):
#     sievebound = (limit - 1)/2
#     sieve = [False for x in xrange(1,sievebound+1)]
#     crosslimit = int((math.sqrt(limit)-1)/2)
#     for i in xrange(1,crosslimit):
#         if not sieve[i]:
#             for j in xrange(2*i*(i+1),sievebound,2+i+1):
#                 sieve[j]=True
#     sum = 2
#     for i in xrange(1,sievebound):
#         if not sieve[i]:
#             sum+=(2*i+1)
#     return sum


print main(2000000)