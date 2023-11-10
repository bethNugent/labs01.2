# numbers = [1,3,5,7,9]

# print(numbers[0])
# print(numbers[2])


# names = ["Bob", "Steve", "Beth"]

# print(names[1])


# numbers = [4,7,6,2,9]

# print(len(numbers))

#first index of a list is always -
#final index of a list is always length - 1 as it starts from index 0

# names = ["Ralph", "Conor", "Beth"]

# for name in names:
#     print(name)


# names = ["Ralph", "Conor", "Beth"]

# i=0

# while(i < len(names)):
#     print(names[i])
#     i+= 1


numbers = [4,7,6,2,9]

# i=0
# while(i < len(numbers)):
#     print("index", i, "=", numbers[i])
#     i += 1

#same as below

for i in range(len(numbers)):
    print("index", i, "=", numbers[i])



greeting = "Hello"
for char in greeting:
    print(char)

#same as

greeting2 = "Hello"
i=0

while(i < len(greeting2)):
    print(greeting2[i])
    i += 1



#FINISH NUMBERS
# numbers = [1,2,3,4,5]

# numbers.append(6)
#     print(numbers)


fruits=[]

fruits.append("apple")
fruits.append("pear")
fruits.append("banana")
fruits.append("kiwi")
fruits.append("peach")

for fruit in fruits:
    print(fruit)

fruits[0] = "pineapple"

for fruit in fruits:
    print(fruit)


# numbers = [1,3,5,7,9]
# #removes first occourance of value
# numbers.remove(5)
# #deletes at index 0
# del(numbers[0])

# for number in numbers:
#     print(number)




# adminIDs = [12,23,34,45,56,67,78,89]
# iD = int(input("Enter your ID: "))
# if id in adminIDs:
#     print("Welcome")



