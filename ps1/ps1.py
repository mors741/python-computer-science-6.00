# Problem Set 1
# Name: Kharitonov Evgeny
# Time Start: 0:29

balance = float(raw_input("Enter the outstanding balance on your credit card: "))
interestRate = float(raw_input("Enter the credit card interest rate as a decimal: "))
minPayRate = float(raw_input("Enter the minimum monthly payment rate as a decimal: "))
totalPaid = 0

for month in range (1, 13):
    print "Momth:", month
    minMonPay = round(balance * minPayRate, 2)
    print "Minimum monthly payment: $" + str(minMonPay)
    interestPaid = round((interestRate / 12) * balance, 2)
    prPaid = minMonPay - interestPaid
    print "Principle paid: $" + str(prPaid)
    balance -= prPaid
    totalPaid += minMonPay
    print "Remaining balance: " + str(balance)
print "RESULT"
print "Total amount paid: $" + str(totalPaid)
print "Remaining balance: $" + str(balance)
    
