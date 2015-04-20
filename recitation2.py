### Prints even number from 0 to 10
### while
##even_number = 0
##while even_number <= 10:
##    print even_number
##    even_number += 2
##    
###---------------------------------------------
### Prints even number from 0 to 10
### for
##for i in (0, 2, 4, 6, 8, 10):
##    print i
#---------------------------------------------
### range
##
###print range(1,100)
##
##for i in range (0, 1001, 2):
##    print i
#---------------------------------------------
# tuples

tuple_of_numbers = (3.14159, 2, 1, -100, 100, 240)
#tuple_of_strings = ('What', 'is', 'my', "name?")
tuple_of_strings = (3.14159, 'is', 'an imperfect', "represtnation of Pi")
#print tuple_of_numbers[-3]
#print tuple_of_strings[4]
#print len(tuple_of_strings)
#tuple_of_tuples = (('stuff', 'just'), 'got', 'real')
#print tuple_of_tuples[0]

#IMMUTABLE
#tuple_of_numbers[3] = 4

#SLICING
#print tuple_of_numbers[1:2]
#print tuple_of_numbers[:-1]
##
##for number in tuple_of_numbers:
##    print number

#CREATING A NEW TUPLE
print "Before", tuple_of_numbers
tuple_of_numbers = tuple_of_numbers + (100, 20)
print "After", tuple_of_numbers
