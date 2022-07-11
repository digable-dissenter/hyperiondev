#************* HELP *****************
#REMEMBER THAT IF YOU NEED SUPPORT ON ANY ASPECT OF YOUR COURSE SIMPLY LOG IN TO www.hyperiondev.com/support TO:
#START A CHAT WITH YOUR MENTOR OR SCHEDULE A CALL.
#*************************************


# PLEASE ENSURE YOU OPEN THIS FILE IN IDLE otherwise you will not be able to read it.

# *** NOTE ON COMMENTS ***
# This is a comment in Python.
# Comments can be placed anywhere in Python code and the computer ignores them - they are intended to be read by humans.
# Any line with a # in front of it is a comment.
# Please read all the comments in this example file and all others.


# ============= while Loops ==================
print ("While loops: ")
# A loop is a sequence of statements that are continually repeated until a certain condition is met.
# One of the simplest loops is the while loop.
# Like an if statement a while loop tests a condition, but instead of executing the code once, a while loop runs until its condition becomes False.
# In other words, the statements are repeatedly executed "while" the condition is true.


# In Python, the general syntax for a while loop is as follows:
# while condition_is_true:
#     execute_these_statements


# ************ Example 1 ************
i = 9

while i < 10:
   i = i + 1
# The above loop will only execute once because the condition while i < 10 is not true after you have added 1 to i.


# ************ Example 2 ************
print ("Example 2: ")
i = 0

while i < 100:
        print (i)
        i = i+1
# The above loop will print out all the numbers from 0 to 99, and then terminate.

# ************ Example 3 ************
i = 100

while i < 50:
        print (i)

# The above while loop will not execute at all, because i is already bigger than 50.


# ************ Example 4 ************
print ("Example 4: ")
a=0

while a < 10:
        print (a)
        a += 1       # a += 1 is equivalent to a = a + 1


# Initially a is set to 0.
# The while loop then checks the condition (a < 10) to see if it is true.
# If it is true the indented statements following the while loop are executed
# So if a is less than 10, the value of a is printed and then increased by one.
# The loop then begins again by checking the the condition and determining whether to execute the indented statements.
# This goes on until the condition becomes False.


# ============= Infinite Loops ==================
# A while loop runs the risk of running forever if the condition never becomes False.
# A loop that never ends is called an infinite loop.
# Creating an infinite loop is not desirable, so you should make sure that your loop condition eventually becomes False and you loop is exited.
# You can do this by using a variable such as a in the previous example. This variable is incremented with every iteration (each time the statements within the loop are repeated)
# By incrementing the variable the condition should at some point become False and the loop will exit.
# While loops are know as event-controlled loops as iterations continue until some non-counter-related condition (event) stops the process.


# ************ Example 5 ************
# The following example, shows a program whose while-statement sums successive even integers (2 + 4 + 6 + 8 + ...), until the total is greater than 250.
# An update statement increments i by 2
# so that it becomes the next even integer.

print ("Example 5: ")
sum1 = 0
i=0                  #initial even integer for the sum
while sum1 <= 250:
        sum1 += i
        i += 2
        print (sum1)



# ============= for Loops ==================
print ("For loops:")
# Programmers don't want to have to copy and paste the same statement over and over again.
# Just like a while loop, a for loop allows statements to be repeated a number of times
# However, unlike a while loop the number of repetitions is know ahead of time
# A for loop is a counter-controlled loop.
# It starts with a start value and counts up to an end value.

# In Python a for loop has the following syntax:
# for index_variable in sequence:
#	statements

# As you can see the Python for loop starts with the keyword 'for' followed by a variable that will hold each of the values of the
# sequence, as we move through it.
# The indexVariable can tell you what 'iteration' the loop is on.
# In each 'iteration'(repetition) of the for loop the code indented inside the for loop is repeated.
# You can use the Python range() function to generate a sequence of numbers, which are then used to iterate through a for loop.
# The range() function needs two integer values, a start number and a stop number.
# For the function range(start, stop), the start number IS included and stop number is NOT included.


# ************ Example 6 ************
print ("Example 6: ")
for i in range(1, 10):
        print (i)

# Explanation:
# This for loop prints the numbers 1 to 9. Again, note the indentation and the colon, just like in the if statement.
# In this for loop, when the variable i (which is an integer) is in the range of 1 to 10 (i.e. either 1, 2, 3 ,4 ,5 ,6 ... or 9), the code under the for loop will execute.
# range(1, 10) specifies that i = 1 in the first iteration of the loop.
# Through each iteration of the loop i will be increased by 1 until i is 10 and therefore not in the range (1,10).
# The loop will then stop executing.



# ************ Example 7 ************
# You can use an if statement within a for loop!
print ("Example 7: ")
for i in range (1,10):
        if i > 5:
                print (i)

# This will only print the numbers 6, 7, 8 and 9 because numbers less than or equal to 5 are filtered out.




# ****************** END OF EXAMPLE CODE ********************* #


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task(s) in the content PDF to proceed to the next task. ===
# == Ensure you complete your work in this folder so that your mentor can easily locate and mark it. ===
