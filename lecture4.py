##Find the square of the value
# bisection search

##def withinEpsilon(x, y, epsilon):
##    return abs(x - y) <= epsilon
##
##def f(x):
##    x +=1;
##    print "x=",x
##    return x
##
##def f1(x):
##   def g():
##       x = 'abc'
##   x = x + 1
##   print 'x =', x
##   g()
##   assert False
##   return x
##
##x = 3
##z = f1(x)

##x = 25.0
##epsilon = 0.01
##numGuesses = 0
##low = 0.0
##high = max(x, 1)
##ans = (high + low)/2.0
##print ans
##while not withinEpsilon(ans**2, x, epsilon):    
##    if ans**2 < x: #too little
##        low = ans
##    else:
##        high = ans #too large
##    numGuesses += 1
##    ans = (high + low)/2.0
##    print ans
#-------------------------------------------
sumDigits = 0
for c in str(1952):
    sumDigits += int(c)
print sumDigits
