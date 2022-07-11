#************* HELP *****************
#REMEMBER THAT IF YOU NEED SUPPORT ON ANY ASPECT OF YOUR COURSE SIMPLY LOG IN TO www.hyperiondev.com/support TO:
#START A CHAT WITH YOUR MENTOR, SCHEDULE A CALL OR GET SUPPORT OVER EMAIL.
#************************************


# PLEASE ENSURE YOU OPEN THIS FILE IN IDLE otherwise you will not be able to read it.

# *** NOTE ON COMMENTS ***
# This is a comment in Python.
# Comments can be placed anywhere in Python code and the computer ignores them - they are intended to be read by humans.
# Any line with a # in front of it is a comment.
# Please read all the comments in this example file and all others.



# ========= What are Booleans? =========
# The Boolean data type has only two values, namely True and False.
# Booleans are closely related to conditional statements, which evaluate to either True or False.
# Conditional statements are found in control statements such as if statements


# ========= Declaring Boolean Variables  =========
# Boolean variables are declared like any other type of variable

# ************ Example 1 ************
has_drivers_licence = True
has_traffic_fines = False
# Please note when assigning either True or False to a variable don't forget to capitalise the first letter.
# Python is case sensitive which means, true, True and TRUE, mean three diffrent things!


# ========= Booleans in if Statements =========
# The if statement is an example of a control statement.
# A control statement is a statement that determines whether or not other statements will be executed.
# The if statement contains a condition that evaluates to either True or False which is a Boolean value.
# This determines whether or not the indented statements will be executed.


# ************ Example 2 ************
print("Example 2: ")

is_sunny = True

if is_sunny:
    print ("It is sunny today, don't forget the sunscreen!")

#Explanation:
# Since is_sunny is True the print statement will execute and print out "It is sunny today, don't forget the sunscreen!”
# If is_sunny is changed to False the print statement will not execute and nothing will be printed.

# ========= Operators ===========
# Operators are symbols that tell the computer which mathematical calculations to perform or which comparisons to make.


# ========= Comparison Operators ===========
# As a programmer, it's important to not forget the basic logical commands.
# We can check if values or values stored in variables are equal to, less than, greater than, or not equal to one another.
# These work well with if statements to control what goes on in our programs.

# The four basic comparative operators are:
# greater than      >
# less than         <
# equal to          ==
# not equal         !


# We can combine the greater than, less than and not operator with the equals operator and form three new operations:
# greater than or equals to     >=
# less than or equals to        <=
# not equals to                 !=

# A tip to remember it is to word out the condition. Say the condition out loud if you need to
# and it will naturally come to you through practice.


# ************ Example 1 ************
# Comparing Numbers

print ("Example 1: ")

num1 = 10
num2 = 20

if num1 >= num2:        # 'greater than or equal to'
       print ("It's not possible that 10 is bigger than or equal to 20.")
elif num1 <= num2:      # 'less than or equal to'
       print ("10 is less than or equal to 20." )
elif num1 != num2:      # 'not equal to'
       print ("This is also true since 10 isn't equal to 20, but the elif statement before comes first and is true so Python will execute that!")
elif num1==num2 :       # 'equal'
       print ("Will never execute this print statement...")


# Explanation:
# The program will check the first part of the if statement (is num 1 bigger than or equal to num 2?).
# If it is not, then it goes into the first 'elif' statement and checks if num1 is less than or equal to num2.
# If it is not then it goes into the next 'elif' statement...etc.


# ************ Example 2 ************
# Comparing Strings

print ("Example 2: ")
my_name = "Tom"

if my_name == "Tom":
       print ("Hey Tom!")


# ========= Logical Operators  ===========
# Logical operators are another type of operator that is used to control the flow of a program.
# They are usually found as part of a control statement such as an if statement.
# Logical operators basically allow a program to make a decision based on multiple conditions.
# For example, if you would like to test more than one condition in an if statement.

# The three logical operations are:
# and   -  both conditions need to be true for the whole statement to be true (also called the conjunction operation)
# or    -  at least one condition needs to be true for the whole statement to be true (also called the disjunction operation)
# not   -  the statement is true if the condition is false (only requires one condition)

# The 'and' and 'or' operators require two operands, while the 'not' operator requires one.


# ************ Example 3 ************
# Let's look at a real world examples:

# If there are eggs and there is enough money to buy eggs, then you can buy eggs. Otherwise you can't.
# This is an example of a conjunction operation where both conditions need to be true for the whole statement to be true.
# This is called the 'and' operation.

# If your friends are at the cinema or if the hot-dogs are among the best at the cinema, then you will go to the cinema, otherwise you won't.
# This is a disjunction operation where at least one of the conditions need to be met for the whole statement to be true.
# This is also called the 'or' operation.


# ************ Example 4 ************
# Example of an 'and' condition:

print ("Example 4: ")
my_name = "Tom"
my_favourite_colour = "orange"

if my_name == "Tom" and my_favourite_colour == "orange":
        print ("Your name is Tom and your favourite colour is orange.")
else:
        print ("Your name isn't Tom or your favourite colour isn't orange.")


# Explanation:
# If my_name is Tom and my_favourite_colour is orange, then the if statement's print statement will execute.
# Both conditions need to be met otherwise the else statement and its' print statement will execute.


# ************ Example 5 ************
#Example of an 'or' condition:

print ("Example 5: ")
item = "chair"

if item == "dog" or len(item) == 5:
       print ("Either item is a dog, or the length of your item is 5.")

# Explanation:
# If item is dog or the length of item is 5, the print statement will execute
# At least one of the conditions need to be met otherwise print statement will not execute.


# ************ Example 6 ************
#Example of a 'not' condition:

print ("Example 6: ")
has_traffic_fines = False

if not has_traffic_fines:
    print ("You are a good driver.")

# Explanation:
# If has_traffic_fines is false the print statement will execute
# By adding the not operator, the has_traffic_fines variable is interpreted as being true when it is actually false



# ************ Example 7 ************
print ("Example 7: ")

if item == "dog" or len(item) == 5:                 #Branch 1
        print ("Either item is a dog, or the len of your item is 5.")
elif item =="chair" and len(item) == 5:             #Branch 2
       print ("Your item is both a chair and len of item is 5.")

# When you run the above code, what will be the output? Run this program and find out!
# Remember only one branch of the if statement will execute, even if multiple branch conditions are 'true'.


# ========= Arithmetic Operators ===========

# The arithmetic operators in Python are as follows:
# + (Addition)          -       Adds values on either side of the operator
# - (Subtraction)       -       Subtracts the value on the right of the operator from the value on the left
# * (Multiplication)    -       Multiplies values on either side of the operator
# / (Division)          -       Divides the value on the left of the operator by the value on the right
# % (Modulus)           -       Divides the value on the left of the operator by the value on the right and returns the remainder
# ** (Exponent)         -       Performs exponential calculation



# ****************** END OF EXAMPLE CODE ********************* #


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===
