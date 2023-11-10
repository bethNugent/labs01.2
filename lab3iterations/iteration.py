#Looping

x = 1

# while x < 5:
#     print(x,"Hello world")
#     x = x + 1

while (x < 5):
    print("The value is", x)
    x += 1


# '*' is print
n = 1

while n <= 5:
    print('*' * n)
    n += 1

print('*' * n)

print("hello" * n)


while n > 0:
    n -= 1
    print('*' * n)



# #Program will run until you hit 21
# total = 0
# running = True

# while (running):
#     total += int(input("Enter a number (1-10)\n"))

#     if (total >= 21):
#         break
#     choice = input("Would you like to give another number? y or n\n")
#     if (choice == "y"):
#         running = True
#     elif (choice == "n"):
#         running = False
#     else:
#         print("invalid choice")

# print("total is", total)



# #continue / hit continue you go back to the top
# total = 0
# running = True

# while (running):
#     increase = int(input("Enter a number (1-10)\n"))

#     if (increase < 1 or increase > 10):
#         print("Invalid selection. Number must be between 1-10 (inclusive). Try again")
#         continue

#     total += increase

#     if (total >= 21):
#         break

#     flag = True
#     while (flag):
#         choice = input("Would you like to give another number? y or n\n")
#         if (choice == 'y'):
#             flag = False
#         elif (choice == 'n'):
#             flag = False
#         else:
#             print("Invalid choice - try again")

# print("total is", total)



#Ranges

#prints out 0,1,2,3,4
range(5)

#the end value is not inclusive
#prints out 1,2,3,4
range(1,5)

#reverse order and end value is not inclusive
#-1 reverses
#prints out 5,4,3,2,1
range(5,0,-1)



#For loops

for x in range(5):
    print(x, "Hello World")