#Ask the user to input an integer
# #Display the numbers factorial using a while loop


# num = int(input("Enter an integer: "))
# result = 1
# while (num > 1):
#     result *= num
#     num -= 1

# print(result)


#for loop

number = int(input("Enter an integer: "))
result = 1

for num in range(number, 0, -1):
    result *= num

print(result)