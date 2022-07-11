
# ========= What are Strings? ===========
# A string is a common data type which is used to represent text.
# It is a sequence of characters, such as, letters, numerals, symbols and special characters.
# In Python, strings must be written within “quotation marks” in order for the computer to be able to read it.
# The smallest possible string contains 0 characters and is called an empty string.


# ************ Example 1 ************
# Some examples of strings

name = "John Doe"
fact = "A traffic jam lasted lasted for more than 10 days, with cars only moving 0.6 miles a day."
address = "77 Winchester Lane"
empty_str = ""


# ========= Indexing Strings ===========
# Since a string is basically a list of characters, you can extract the characters of a String.
# Each character of a string (including spaces) is indexed by numbers starting from 0 for first character on the left.
# The characters are also indexed from right to left using negative numbers, where -1 is the rightmost index and so on.

# ************ Example 2 ************
word = "Hello"
print ("Example 2: ")

# Indexing from 0 to 4
char1 = word[0]
char2 = word[1]
char3 = word[2]
char4 = word[3]
char5 = word[4]
print (char1)
print (char2)
print (char3)
print (char4)
print (char5)

print ("Example 2 backwards: ")
# Indexing from -5 to -1
char1 = word[-1]
char2 = word[-2]
char3 = word[-3]
char4 = word[-4]
char5 = word[-5]
print (char1)
print (char2)
print (char3)
print (char4)
print (char5)


# ========= Slicing Strings ===========
# Slicing in Python, extracts characters from a string based on a starting index and ending index
# It enables you to extract more than one character or "chunk" of characters from a string.


# ************ Example 3 ************
print ("Example 3: ")

very_long_word = "supercalifragilisticexpialidocious"
print (very_long_word[0:5])      # prints out 'super',

# ************ Example 4 ************
print ("Example 4: ")
index = 6
print (very_long_word[index:9])     # prints out 'ali' - you can use variables as indices

# ************ Example 5 ************
# You can omit either or both of the indices
# If the first index is omitted it defaults to 0, so that your chunk starts from the beginning of the original string
# If the second index is omitted it defaults to the highest index in the string, so that your chunk ends at the end of the original string.

print ("Example 5: ")
print (very_long_word[0:])
print (very_long_word[:])
# both these statements print out all the characters from the 0th position (the start of the string) to the end.

print (very_long_word[:9])      # prints out 'supercali'


# ==== Concatenating Strings ====
# You can add, or 'concatenate' Strings together to form a sentence or longer word.
# Simply use the '+' operator to join strings together


# ************ Example 6 ************
name = "Tim"
sentence = "My name is " + name


# ************ Example 7 ************ IMPORTANT
# You cannot add a string and a non string together, you must convert the non string if you want to do this.
# If you try run code that adds a string with a non-string, you will get an error.
# You'll see many examples in our code where we have to cast things to a string in order to print (them out.

age = 12
sentence = "And my age is " + str(age)  # Casting integer to string.

# Explanation:
# The way numbers are stored and arranged differ to the way strings are stored.
# In the example above, we are wanting to state that your age is 12.
# The problem lies with the integer, how do we convert an integer to a string that can be easily joined in the string statement?
# We do this by converting the integer to a String using casting and then joining it to the desired text.

# ************ Example 8 ************
print ("Example 8: ")

sentence_two = "No people under the age of " + str(18)+"."
age = int(input("Enter your age: "))

# Explanation:
# We wish to join the number 18 as a string with another string, the result of the concatenation is stored in the variable sentence_two.
# In the next line, we would like input of the user's age, so we make use of the function input(...) and call it with a string parameter.
# input(...) is a function and a function is a series of operations used to access, perform and/or set some actions to/with data if it is needed.
# The string "Enter your age" is read by the function input(...) which accesses the string given to it and prints it on the screen.
# The next step input(...) takes is to read what the user types on the keyboard. This is given back to us as a string.
# Seeing that age is a something which could increase or decrease, we can say that it should be treated like a number.
# That is why we use the int(...) function to take the user's input, and return it as a number which is then stored as such in the age variable.


# ===== Defining multi-line Strings ====
# Sometimes, it's useful to have long strings that can go over one line.
# We use triple single quotes to define a multi-line string
# Defining a multi-line String preserves the formatting of the string

# ************ Example 9 ************
long_string = ''' This is a long string
 using triple quotes preserves everything inside it as a string
 even on different lines and with different /n spacing. '''


# ========= The len() Function ===========
# A function is a group of statements that perform a specific task.
#  A useful function is the len("string") function which returns the length of the string


# ========= String Methods ===========
# String methods are built in code that perform certain operations on strings
# There are many built in string methods that can provide useful functionality to your program without extra coding.
# You are able to reuse these methods over and over again.

# Some useful String methods are as follows:
#   - string.upper()                --->   converts lowercase letters to uppercase
#   - string.lower()                --->   converts uppercase letters to lowercase
#   - string.replace("old" , "new") --->   replaces all occurrences of substring old with the substring new
#   - string.strip('char')          --->   removes leading and trailing characters 'char'



# ************ Example 10 ************
print ("Example 10: ")

manip_string = "***Welcome$to$the$world$of$programming***"

manip_string = manip_string.replace("$", " ")
print ("manip_string.replace(""$"", " "): " + manip_string)

manip_string = manip_string.strip('*')
print ("manip_string.strip(""*""): " + manip_string)

manip_string = manip_string.upper()
print ("manip_string.upper(): " + manip_string)

manip_string = manip_string.lower()
print ("manip_string.lower(): " + manip_string)

print ("len(manip_string): " + str(len(manip_string)))


# Remember that you can run this file to see output, or copy and paste sections of it into your own Python files and run them to understand the code better.

# ========= Note on Lists ===========
# If you noticed, the split method above returns a list
# A list is a datatype that can be thought of as a container that holds a number of other items, such as strings, integers or floats.
# A list is created by placing all the items inside a square bracket [ ] and separating them by commas.
# For example, a list of integers can be created as follows:
# int_list = [1, 2, 3, 4]
# To add an item to the end of your list, you use the append method.
# For example list.append(item) adds the single item within the brackets to the end of list
# You will learn more about lists later on in this course.

#  ========= Escape Character ===========
# Python uses the backslash (\) as an escape character
# The backslash (\) is used as a marker character to tell the compiler/interpreter that the next character has some special meaning.
# The backslash together with certain other characters are known as escape sequences

# Some useful escape sequences can be found below:
# \n    -   Newline
# \t    -   Tab
# \s    -   Space

# The escape character can also be used if you need to include quotation marks within a string.
# You can put a backslash (\) in front of a quotation mark so that it doesn't terminate the string.
# You can also but a backslash in front of another backslash if you need to include a backslash in a string.


# ************ Example 11 ************
print ("Example 11: ")
people = "Person 1 \nPerson 2"
print (people)
# Notice the line break between the two words. The \n character is invisible - it's a command to insert a new line.


# ************ Example 12 ************
print ("Example 12: ")
wage = "Person 1: \t R123.22"
print (wage)
# Notice the tab between the two words. The \t character is invisible - it's a command to insert a new tab space.

# ************ Example 13 ************
print ("Example 13: ")
sentence = "\"The escape character (\\) is a character which invokes an alternative interpretation on subsequent characters in a character sequence.\""
print (sentence)
# Notice that the quotation marks and backslash are printed out as part of the string.



# ****************** END OF EXAMPLE CODE ********************* #



# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory tasks in the lesson (refer to the PDF file) to proceed to the next task. ===
# == Ensure you complete your work in this folder so that your mentor can easily locate and mark it. ===
