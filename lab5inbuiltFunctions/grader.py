#Inbuilt Functions - Chapter 5
#Your task is to present some statistics on the following students' grades that are read from a file

import statistics

data = "100,30,23,56,67,78,78,89,9,88,7,67,543,54,83,4,56,67,64,53,43,75,76,83,71,92,58,79,48,88,99,66,44,55,77,75,68,97,98,59,73,61,69,75,68,73,47,66,89,87,68,75,74,79,89,80,70,60,57,67,89,76,53,46,78,90,87,6,54,67,89"

#Extract information from this string, you'll need to split it by ',' as a delimiter
#put the resultsing list into a variable called grades
grades = data.split(',')
# print(dataList)

#without this line it goes wrong
#min gives us 100 / max gives us 99
#we need to map through first to get the right result
#this line of code casts the grades into a list of ints
grades = list(map(int, grades))

#Display the mimimum value of the grades
minimumGrade = min(grades)
print("The minimum grade is:", minimumGrade)

#Display the max grade
maximumGrade = max(grades)
print("The minimum grade is", maximumGrade)


# #display the average of grades to 2 decimal points
# #divide sum of grades by length of grades
# #and then round to the 2nd decimal point
# averageGrade = sum(grades) / len(grades)
# averageGrade2dec = round(averageGrade, 2)
# print("The average grade is:", averageGrade2dec)

#import the statistics library
#Use the statistics mean() function to get the average grade to 2 decimal places
averageGrade = statistics.mean(grades)
averageGrade = round(averageGrade, 2)


medianGrade = statistics.median(grades)

print("The average grade is:", averageGrade)
print("Themedian grade is:", medianGrade)

#using string.format() function display the min, max, average, mean and median values
str = "The minimum grade is {}. The maximum grade is {}. The average grade is {}. The median is {}".format(minimumGrade, maximumGrade, averageGrade, medianGrade)
print(str)