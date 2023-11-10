#Task 6

#Code a program that calculates the average of three exam marks

artMark = -1
mediaMark = -1
englishMark = -1

while (artMark < 0 or artMark > 100):
    artMark = int(input("Enter a mark for art between 0 and 100: "))

while (mediaMark < 0 or mediaMark > 100):
    mediaMark = int(input("Enter a mark for media between 0 and 100: "))

while (englishMark < 0 or englishMark > 100):
    englishMark = int(input("Enter a mark for english between 0 and 100: "))

totalMark = artMark + mediaMark + englishMark
averageMark = totalMark / 3

print("The total mark is: ", totalMark)
print("The average mark is: ", averageMark)