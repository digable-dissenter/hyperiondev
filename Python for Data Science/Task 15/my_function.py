# math library will be used in this task
import math

# Exercise a)
# Defining my own function that will print out days of the week
def own_function():
    answer = ''
    # Decided to use a list to store the weeks' days
    weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    # Loop through list to append to answer string
    for i in weekdays:
        answer += i + "\n"
    # Result should not have any leading/trailing spaces
    return answer.strip()

# Print result    
print(own_function())

# Exercise b)

# Defining replace_hello function that will replace every 2nd word from user input into 'Hello'
def replace_hello(snt):
    # Delimiter is a List which stores every sentence word as an item. 
    delimiter = snt.split()
    # Instantiate new sentence
    new_sentence = ''
    count_word = 0
    # Loop through List
    for i in delimiter:
        # Increase word count as loop through List
        count_word += 1
        # fmod here is used to see if a word in the sentence order is odd. If so, then that word is not replaced
        if math.fmod(count_word,2) != 0:
            new_sentence += delimiter[count_word-1] + " "
        # else here implies a word in the sentence order is even. If so, then that word is replaced with 'Hello'
        else:
            new_sentence += "Hello "
    # Remove leading/trailing whitespace characters
    return new_sentence.strip()

# Request user input
sentence = input("Add a sentence: \n")

# Call replace_hello function
answer = replace_hello(sentence)

# Print result
print(answer)