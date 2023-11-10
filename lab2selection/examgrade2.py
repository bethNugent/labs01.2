#Selection
#Part 2
#Task3

#Write code to input a grade and calculate the grade but this time you'll take into account the different levels of studies

examGrade = int(input("Enter your exam mark between 1 and 100: "))

if (examGrade < 1 or examGrade > 100):
    print("Error: marks must be between 1 and 100")
else:
    level = int(input("Enter your level"))

    if (level == 1):
        if (examGrade > 70):
            print("Distinction")
        elif (examGrade > 60):
            print("Merit")
        elif (examGrade >= 50):
            print("Fail")
    elif (level == 2):
        if (examGrade > 65):
            print("Distinction")
        elif (examGrade > 50):
            print("Merit")
        elif (examGrade >= 40):
            print("Pass")
        elif (examGrade < 40):
            print("Fail")
    else:
        print("Invalid student level. Must be level 1 or 2.")
