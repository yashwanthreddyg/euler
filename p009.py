def main():
    a=b=c=1
    for a in xrange(3,(1000-3)/3):
        for b in xrange(a+1,(1000-1-a)/2):
            c=1000-a-b
            if (a*a + b*b == c*c) and (a+b+c == 1000):
                return a*b*c
print main()