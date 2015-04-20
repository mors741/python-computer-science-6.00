# Problem Set 1
# Name: Kharitonov Evgeny
# Time Spent: 0:52

initialBalance = float(raw_input("Enter the outstanding balance on your credit card: "))
anInterestRate = float(raw_input("Enter the credit card interest rate as a decimal: "))
monPayment = 0.0
totalPaid = 0
balance = initialBalance
epsilon = 0.005

interestRate = anInterestRate / 12.00

lowerBound = initialBalance / 12.00
upperBound = (initialBalance * (1 + interestRate)**12)/12.00

while abs(balance) > epsilon:
    month = 0
    balance = initialBalance
    monPayment = (lowerBound + upperBound)/2.0
    while month < 12 and abs(balance) > epsilon:
        interestPaid = round(balance * interestRate, 2)
        balance += interestPaid
        balance -= monPayment
        month += 1
    if balance > 0:
        lowerBound = monPayment
    else:
        upperBound = monPayment
monPayment = round(monPayment + 0.004999, 2)
print "RESULT"
print "Monthly payment to pay off debt in 1 year: $" + str(monPayment)
balance = initialBalance
for month in range(1, 13):
    interestPaid = round(balance * anInterestRate/12, 2)
    balance += interestPaid - monPayment
    if balance <= 0:
        break
print "Number of months needed: " + str(month)
print "Balance:", round(balance, 2)
