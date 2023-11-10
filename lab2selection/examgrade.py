#Selection
#Part 2
#Task 2

#Write code to input a grade and calculate the grade 
#Display the exam grade 

examGrade = int(input("Enter your exam grade: "))

if examGrade < 1 or examGrade > 100:
    print("Error: marks must be between 1..100")
elif examGrade >= 71:
    print("Distinction")
elif examGrade >= 61:
    print("Merit")
elif examGrade >= 50:
    print("Pass")
elif examGrade < 50:
    print("Fail")
else:
    print("Invalid input")
