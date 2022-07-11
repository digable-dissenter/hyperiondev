# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.


print ("Welcome to the error program") # Error 1: Compilation error (missing parenthesis)
print ("\n")                           # Error 2: Compilation error (indentation & missing parenthesis)

age_str = "24 years old" #I'm 24 years old. # Error 3+4: Compilation error(indentation) + Runtime error (double == to assign variable)
age = int(age_str[0:2])                     # Error 5+6: Compilation error (indentation) + Runtime error (integer variable can't have string components)
print("I'm "+ str(age) +" years old.")          # Error 7+8: Compilation error (indentation) + Runtime error (need to convert int back to string when displaying in print)
three = "3"                         # Error 9: Compilation error (indentation)

answer_years = age + int(three)          # Error 10+11: Compilation error (indentation) + Runtime error (need to convert three to int)

print ("The total number of years: " + str(answer_years)) # Error 12+13: Compilation error (missing parenthesis) + Runtime error (need to convert int back to string when displaying in print)
answer_months = answer_years*12+6               # Error 14+15: Logic error. answer never declared. need to add the 6 months to reach correct total of 330
print ("In 3 years and 6 months, I'll be " + str(answer_months) + " months old") # Error 15+16: Compilation error (missing parenthesis) +
                                                                                 # Runtime error (need to convert int back to string when displaying in print)
                                                                                  

 #HINT, 330 months is the correct answer

