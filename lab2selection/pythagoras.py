#Selection
#Task 4

#Pythagoras
#Write a program that calculates the lengths of sides of a triangle using Pythagoras's Theorem
#Pythagoras' Theorem states that the square of the long side (C) of a right-angled triangle is
#the sum of the squares of the two shorter sides (A and B)
#n**2 in Python will raise n to the power of 2, i.e. square it. e.g. 3**2 is 9


import math

print("Pythagoras' Calculator")
print("1. Find the length of A given B and C")
print("2. Find the length of B given A and C")
print("3. Find the length of C given A and B")

choice = int(input("Enter your choice - 1, 2 or 3: "))
if choice == 1:
    sideB = int(input("Enter the length of side B: "))
    sideC = int(input("Enter the length of side C: "))
    sideA = math.sqrt(sideB**2 + sideC**2)
    print("The length of side A is:", sideA)
elif choice == 2:
    sideA = int(input("Enter the length of side A: "))
    sideC = int(input("Enter the length of side C: "))
    sideB = math.sqrt(sideA**2 + sideC**2)
    print("The length of side B is:", sideB)
elif choice == 3:
    sideA = int(input("Enter the length of side A: "))
    sideB = int(input("Enter the length of side B: "))
    sideC = math.sqrt(sideA**2 + sideB**2)
    print("The length of side C is:", sideC)