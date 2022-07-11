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



# ========= elif Statements ===========
# elif is short for else if.
# It allows you to specify a new condition to test, if the first condition is False.
# Unlike the else statement, you can have multiple elif statements in an if-elif-else statement.
# If the condition of the if statement is False, the condition of the next elif statement is checked.
# If the elif statement condition is False the condition of the next elif statement is checked, etc.
# If all the elif conditions are False, the else statement and its indented block of statements are executed.

# In Python, if-elif-else statements have the following syntax:
# if condition1 :
#       indented Statements
# elif condition2 :
#       indented Statements
# elif condition3 :
#       indented Statements
# elif condition4 :
#       indented Statements
# else:
#       indented Statements


# ************ Example 1 ************
print ("Example 1: ")
grade = 66

if grade >= 80:
        print ("Congratulations! You have an A")
elif grade >= 70:
        print ("Good job! You have a B")
elif grade >= 60:
        print ("Keep it up! You have a C")
elif grade >= 50:
        print ("Try a little harder next time! You have a D")
else:
        print ("Oh No! You have an F")

# Run this program to see what prints out, then try changing the value of the grade variable and running it again.


# ========= Some Important Points to Note on the Syntax of if-elif-else Statements ===========
# Make sure that the if/elif/else statements end with a colon (the : symbol).
# Ensure that your indentation is done correctly (i.e. statements that are part of a certain control structure's 'code block' need the same indentation).
# To have an elif you must have an if above it.
# To have an else you must have an if or elif above it.
# You can't have an else without an if - think about it!
# You can have as many elif under an if, but only one else right at the bottom. It's like the fail-safe statement that executes if the other if/elif statements fail!




# ************ Example 2 ************
print ("Example 2: ")

if len("Hello World") > 6:
        print("This sentence is long!")
elif len("Hello World") > 3:
        print("Slightly more manageable!")
else:
        print("Easy stuff")

# ================== Some notes on the Compulsory Task ==================
# Now that you know more about Python it’s time to write a small useful program.
# You will be utilising everything you have learnt to create a simple Investment Calculator program.
# This task will help you strengthen your understanding of all the concepts you have encountered so far.
# Feel free to go back and revise your previous tasks, as it will help you complete this task.


# ================== Interest ==================
# Interest is the cost of using someone else's money.
# When you borrow money, you pay interest and when you lend money, you earn interest.
# Interest can either be classified as simple interest or compound interest.
# Simple interest is continually calculated on the initial amount invested, and is only calculated once per year.
# This interest amount is then added to the amount that you initial amount invested (known as the Principal amount).
# Compound interest is calculated on the principal amount and also on the accumulated interest of previous periods

# ************ Example 1 ************
# An example of simple interest:
# Just say you invest R1000 at 10%.
# The first year you will earn R100 interest (R1000 * 0.10) giving you R1100.
# The next year the interest is still calculated on the principal amount (R1000) giving you another R100,
# making a total of R1200.


# ************ Example 2 ************
# An example of compound interest:
# Imagine you invest R1000 at 10% compounded once a year.
# The first year you will earn R100, giving you an Accumulated amount of R1100.
# The second year you will earn interest on the Accumulated amount (1100 * 0.10), to earn R110 interest,
# giving you R1210.


# ================== How to Calculate Interest ==================
# Simple interest rate is calculated as follows:
#   A = P(1 + r * t)
#   The Python equivalent is very similar:
#       A =P*(1+r*t)

# Compound interest rate is calculated as follows:
#   A = P(1 + r) ^ t
#   The Python equivalent is slightly different:
#       A = P* math.pow((1+r),t)

# ‘r’ is the interest entered divided by 100, e.g. if 8% is entered, then r is 0.08.
# 'P' is the initial amount deposited
# 't' is the number of years of the investment


# ****************** END OF EXAMPLE CODE ********************* #


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===
