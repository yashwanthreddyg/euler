# import math
# num = 600851475143
# # for i in xrange(2,sqrt(math.sqrt(num))):
# # 	if num%i==0:

# def check(n):
# 	for i in range(2,n):
# 		if n%i == 0:
# 			return False
# 	return True
# print check(25)
# print check(29)
# def range(start,stop):
# 	i=start
# 	while i<stop:
# 		yield i
# 		i+=1
# for i in range(2,num):
# 	if num%i == 0 and check(num/i):
# 		print num/i
# 		break
n = 600851475143
factor = 2
lastFactor = 1
while n > 1:
    if n % factor == 0:
        lastFactor = factor
        n = n / factor
        while n % factor == 0:
            n = n / factor
    factor += 1
print lastFactor
