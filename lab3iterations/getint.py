#Iteration
#Task 4

#Ask the user to input an integer between minimum and maximum values
#If the user fails to enter an acceptable value after three attempts then you stop asking

#Create two variables for min and max
#write a while loop that attempts to get an integer from the user between the limits of min and max
#If the user fails to enter an acceptable value after 3 attempts then stop asking

min = 1
max = 100
finalChoice = None
attempt = 1

while (attempt <= 3):
    choice = int(input("Enter a number between " + str(min) + " and " + str(max) + "\n"))
    if (choice >= 1 and choice <=100):
        finalChoice = choice
        break
    else:
        attempt += 1

print("Chosen value is:", finalChoice)