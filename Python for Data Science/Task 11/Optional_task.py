

f = open('input.txt', 'r')
# char set to 1 because for loop range will exclude the very last character
# The rest of the counter variables set to 0
char = 1
words = 0
lines = 0
count_vowels = 0
# Again, using lists to store vowels
# Reference: https://stackoverflow.com/questions/24361761/python-code-to-count-vowels
vowels = ['a' , 'e' , 'i' ,'o' , 'u']

for line in f:
# Count each line
    lines += 1
# Count each character. Check that range of for loop goes through entire length of line
    for c in range (1, len(line)):
        char += 1
# WHile going through each character in length of each line, check to see that we have vowels and count them
        if line[c] in vowels:
            count_vowels += 1    
    word_delimiter = line.split()
# STring split function counts each as a word when whitespace is present
    for w in word_delimiter:
        words += 1
# Print results    
print("The number of characters is: " + str(char) + "\nThe number of words is: " + str(words) + "\nThe number of lines is: " + str(lines) + "\nThe number of vowels is: " + str(count_vowels))

f.close()
