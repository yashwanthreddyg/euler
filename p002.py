sum = 2
a=1
b=2
for x in xrange(1, 100):
	c = a+b
	# print c
	if c > 4000000:
		break
	if c%2 == 0:
		sum = sum+c
	a=b
	b=c
print sum