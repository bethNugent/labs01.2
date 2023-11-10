#Part 1 - Using while loops

#Write a while loop that starts at 1 and ends at 100
#Calculates and displays each number and its square
#End the loop if that square is bigger than 2000

# n = 1

# while n < 100:
#     n += 1
#     nSquare = (n**2)
    
#     if (nSquare >= 2000):
#         print('Number',n,"square is bigger than 2000 and will not print")
#         break
#     else:       
#         print("number: ",n, "number's square: ",nSquare)



#Part 2 - Using for loops

#Write a for loop that starts at 1 and ends at 100
#Calculates and displays each number and its square
#End the loop if that square is bigger than 2000

for i in range(1, 101):
    iSquare = (i**2)
    
    if (iSquare >= 2000):
        print('Number',i,"square is bigger than 2000 and will not print")
        break
    else:       
        print("number: ",i, "number's square: ",iSquare)
    