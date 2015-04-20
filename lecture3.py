#### Find the cube root of the perfect cube
### with for loop
##x = int(raw_input('Enter the integer: '))
##for ans in range (0, abs(x)+1):
##    if ans**3 >= abs(x):
##        break
##    #print '   current guess =', ans
##
##if ans**3 != abs(x):
##    print x, 'is not a perfect cube'
##else:
##    if x < 0:
##        ans = - ans
##    print 'Cube root of ' + str(x) + ' is ' + str(ans)
#------------------------------------------------

####Find the square of the value
##
##x = 25
##epsilon = 0.01
##numGuesses = 0
##ans = 0.0
##while abs(ans**2 - x) >= epsilon and ans <= x:
##    ans += 0.001
##    numGuesses += 1
##if abs(ans**2 - x) >= epsilon:
##    print 'Failed on square root of', x
##else:
##    print ans, 'is close to square root of', x

#------------------------------------------------
####Find the square of the value
### bisection search
##
##x = 12345.0
##epsilon = 0.01
##numGuesses = 0
##low = 0.0
##high = x
##ans = (high + low)/2.0
##print ans
##while abs(ans**2 - x) >= epsilon:
##    if ans**2 < x: #too little
##        low = ans
##    else:
##        high = ans #too large
##    numGuesses += 1
##    ans = (high + low)/2.0
##    print ans

#------------------------------------------------
##Find the cube of the value
# bisection search

x = 27.0
epsilon = 0.01
numGuesses = 0
low = -abs(x)
high = abs(x)
ans = (high + low)/2.0
print ans
while abs(ans**3 - x) >= epsilon:
    if ans**3 < x: #too little
        low = ans
    else:
        high = ans #too large
    numGuesses += 1
    ans = (high + low)/2.0
    print ans
