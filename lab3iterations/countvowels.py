#Count Vowels
# word = input("Enter a word: ")

# vowelCount = 0

# for char in word:
#     if char.lower() in 'aeiou':
#         vowelCount += 1
# print(f"The number of vowels in {word} are {vowelCount}")



#OR

word = input("Enter a word: ")

vowels = 0
index = 0

while (index < len(word)):
        if (word[index] == "a" or word[index] == "e" or word[index] == "i" or word[index] == "0" or word[index] == "u"):
                vowels += 1
        index += 1

print("The number of vowels in", word, "is:", vowels)

