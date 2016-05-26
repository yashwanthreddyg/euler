def get_prime_factors(num):
    factor = 2
    result = []
    while num > 1:
        if num % factor == 0:
            power = 0
            while num % factor == 0:
                num /= factor
                power = power + 1
            result.append((factor, power))
        factor = factor + 1
    return result


def getLCM(arr):
    factordict = {}
    for index in range(1, len(arr)):
        num = arr[index]
        factordict[num] = get_prime_factors(num)
    # print factordict
	
    final = {}
    for key in factordict:
        factorlist = factordict[key]
        for tup in factorlist:
            if final.has_key(tup[0]):
                final[tup[0]] = max(tup[1], final[tup[0]])
            else:
                final[tup[0]] = tup[1]
    # print final
    product = 1
    for key in final:
        product = product * pow(key, final[key])
    print product


getLCM(range(1, 21))
