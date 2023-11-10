#Selection

#Part 2
#Create a Calculator

import math

num1 = int(input("Enter the first number to calculate: "))

print("Calculator Menu")
print("1. Add (+)")
print("2. Subrtact (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
print("5. Square Root (s)")

operator = input("Chose an operator to calculate your numbers: ")

if operator == '1':
    num2 = int(input("Enter the second number to calculate: "))
    result = num1 + num2
    print("The result is: ", result)
elif operator == '2':
    num2 = int(input("Enter the second number to calculate: "))
    result = num1 - num2
    print("The result is: ", result)
elif operator == '3':
    num2 = int(input("Enter the second number to calculate: "))
    result = num1 * num2
    print("The result is: ", result)
elif operator == '4':
    num2 = int(input("Enter the second number to calculate: "))
    result = num1 / num2
    print("The result is: ", result)
elif operator == '5':
    if num1 >= 0:
        squareRoot = math.sqrt(num1)
        print("Square root is: ", squareRoot)
else:
    print("invalid operator")
    