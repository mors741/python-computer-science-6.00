# Problem Set 1
# Name: Kharitonov Evgeny
# Time Spent: 0:32

initialBalance = float(raw_input("Enter the outstanding balance on your credit card: "))
anInterestRate = float(raw_input("Enter the credit card interest rate as a decimal: "))
monPayment = 0.0
totalPaid = 0
balance = initialBalance

interestRate = anInterestRate / 12

while balance > 0:
    month = 0
    balance = initialBalance
    monPayment += 10
    while month < 12 and balance > 0:
        balance = round(balance * (1 + interestRate), 2) - monPayment
        month += 1

print "RESULT"
print "Monthly payment to pay off debt in 1 year: $" + str(monPayment)
print "Number of months needed: " + str(month)
print "Balance:", balance
