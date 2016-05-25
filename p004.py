m = 0
def check(num):
	s = str(num)
	l = len(str(num))
	i =0 
	j = l-1
	while i<j:
		if s[i] == s[j]:
			i = i+1
			j = j-1
			continue
		else:
			return False
	return True
for num1 in xrange(999,99,-1):
	for num2 in xrange(999,99,-1):
		n = num1*num2
		if n > m and check(n):
			m=n
print m