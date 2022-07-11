#************* HELP *****************
#REMEMBER THAT IF YOU NEED SUPPORT ON ANY ASPECT OF YOUR COURSE SIMPLY LOG IN TO www.hyperiondev.com/support TO: 
#START A CHAT WITH YOUR MENTOR OR SCHEDULE A CALL.
#************************************


# PLEASE ENSURE YOU OPEN THIS FILE IN IDLE otherwise you will not be able to read it.

# *** NOTE ON COMMENTS ***
# This is a comment in Python. 
# Comments can be placed anywhere in Python code and the computer ignores them - they are intended to be read by humans. 
# Any line with a # in front of it is a comment.
# Please read all the comments in this example file and all others.


# ========= if-else Statements =========
# if statements are a type of control structure which controls the flow of logic within a program.
# if statements contain a condition.
# Conditions are statements that can only evaluate to True or False
# After the if statement you can add an else statement.
# An if statement together with an else statement is known as an if-else statement 
# The else statement represents an alternative path for the flow of logic if the condition of the if statement turns out to be False.
# If the if condition turns out to be True, the statements in the indented block following the if statement are executed. 
# If the if condition turns out to be False, the statements in the indented block following the if statement are skipped,
# and the statements in the indented block following the else statement are executed.

# =============  Writing if statements ==================
# If the if condition is True then the indented statements are executed; if the condition is False then the indented statements are skipped 
# In Python, if statements have the following general syntax:
#               if condition :
#                       indented statements

# So, in Python, the general if-else syntax is:
# if condition :
#	indented Statements
# else:
#	indented Statements


# ************ Example 1 ************
print ("Example 1: ")
grade = 66

if grade >= 80:
        print ("Congratulations you have an A")
else:
        print ("You do not have an A")

# Explanation:
# If the grade is greater or equal to 80, the print statement in the indented block after the if statement is executed and "Congratulations you have an A” is printed 
# If the grade is not greater or equal to 80, the print statement in the indented block after the else statement is executed and "You do not have an A" is printed 


# ************ Example 2 ************
# Variables have different types and depending on what sort of operation you wish to do on them you may need to change their type.
# The example below shows that a string value does not equal an integer, even if they appear to be the same  
print ("Example 2: ")
if 9 == "9":                             #Comparing an integer and a string
        print ("Types don't matter")
else:
        print("Types do matter")


# ************ Example 3 ************
# You can only compare data types with each other if they are the same
# To do this you need to change the type by casting.
# This is often used when the user is giving input as it is usually stored as a string.

print ("Example 3: ")
if 9 == int("9"):
        print ("Successful casting")
else:
        print ("I didn't need to cast that!")

 
# ************ Example 4 ************
age = 20
if age >= 18:
        print ("You're over 18 and can come in.")
 
 
# Explanation:
# We check if the age is greater than or equal to 18,
# If the age is 18 or older, then print out "You're over 18 and can come in."
# If they are not 18 or older, then the print statement is skipped and nothing is printed. 
 
 
# =============  Some FAQs on the Syntax of if Statements ==================
#  Q: Why is there a colon at the end of the if statement?
#  A: The colon, as in the English language, serves the purpose of adding extra information.
#      In Python, the colon means that here is code following that statement and can only run if the statement's criteria are met.
 
 
#  Q: Why is the code after the colon indented? And is it important?
#  A: The indentation means that certain code follows from the colon and in this case we have that certain code following from the if statements. 
#      The indentation is there to demonstrate that the program's logic will follow the path indicated by it.
#      Every line in the indentation will run if the program's if statement's conditions are met.
 
 
#  Q: Why do we write the lines of code below each other? 
#  A: The way that programs are run is done in a similar manner to how we humans read books or a newspaper.
#      We read from the top through to the bottom, in programming, this concept is called sequential programming.
#      Sequential programming involves a consecutive and ordered execution of statements, one after the other.
#      Sequential programming is the only programming philosophy we are going follow in this course.
 

# ****************** END OF EXAMPLE CODE ********************* # 


# == Make sure you have read and understood all of the code in this Python file.===
# == Please complete the compulsory task below to proceed to the next task. ===
# == Ensure you complete your work in this folder so that your mentor can easily locate and mark it. ===