# import math library / framework
import math

# Request user input for each of pricipal amount, int rate, time in years, and int type
P = int(input("Enter amount to deposit: "))
i = int(input("Enter interest rate (as a percentage): "))
t = int(input("Enter the number of years to invest: "))
interest = input("Choose between simple and compound interest: ")

# Divide interest rate above by 100.
# No need to cast to float as Python does that already
r = i / 100

# Conditional statement based on user selections, in particular compound vs simple interest
if interest.lower() == "simple":
    answer = round(P*(1+r*t),2)
    print (f"The value of your investment is ${answer} after {t} years with {i}% interest rate: ") 
elif interest.lower() == "compound":
    answer = round(P* math.pow((1+r),t),2)
    print (f"The value of your investment is ${answer} after {t} years with {i}% interest rate: ")
# Fail safe only on condition no valid entry for interest is input
else:
    print ("Please choose between simple and compound interest. (HINT: Check your spelling!")
    
