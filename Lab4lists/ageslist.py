ages = [12,34,23,45,67,45,2,32,11,16,13,99,88,67,87,43,21,32,21,22,66,38,63]

#Record the length of the ages list in a variable
lengthOfList = len(ages)
print(lengthOfList)

# #display these ages one on each line
# for age in ages:
#     print(age)

# OR
# i=0

# while(i < len(ages)):
#     print(ages[i])
#     i += 1

#Add one year to each age
i =0

while(i < len(ages)):
    print(ages[i]+1)
    i += 1

#The code only takes into account those people in the age range of 16-65(inclusively)
#Delete all ages which are outside of this range

#loops through list and removes at the same time
#YOU SHOULD NEVER USE FOR LOOPS WHILE REMOVING elements from an array while using a for loop
#for loops use iteraters - iterators keeo track of what index we're on
#iterator starts at 0, then 1, then 2, then 3 etc..
#it removes the element from the array and shifts everything else left so indexes get skipped
for age in ages:
    if(age < 16 or age > 65):
        ages.remove(age)

print(ages)




#make a copy of list
for age in list(ages):
    if (age < 16 or age > 65):
        ages.remove(age)

print(ages)




ages.sort()
print(ages)