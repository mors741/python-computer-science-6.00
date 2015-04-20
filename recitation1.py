# Find the cube root of the perfect cube
#
##x = int(raw_input('Enter the integer: '))
##ans = 0;
##while ans*ans*ans < abs(x):
##    ans = ans + 1
##    print '   current guess =', ans
##
##if ans*ans*ans != abs(x):
##    print x, 'is not a perfect cube'
##else:
##    if x < 0:
##        ans = - ans
##    print 'Cube root of ' + str(x) + ' is ' + str(ans)
#---------------------------------------------

# FizzBuzz
for i in range (1, 101):
    if i % 15 == 0:
        print i, 'FizzBuzz'
    elif i % 3 == 0:
        print i, 'Fizz'
    elif i % 5 == 0:
        print i, 'Buzz'
    else:
        print i
