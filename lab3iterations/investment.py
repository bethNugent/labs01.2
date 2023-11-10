#Calculates how many years it will take an initial investment of £100 
# to grow to a target value of £1000 if the interest rate is 10%

initial = int(input("Enter an initial investment: "))
target = int(input("Enter a target value: "))
interestRate = int(input("Enter an interest rate (10 = 10%)"))

years = 0

while (initial < target):
    initial += (interestRate * initial) / 100
    print(initial)
    years+= 1

print(years)