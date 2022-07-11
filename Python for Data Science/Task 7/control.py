
# Request user input for age and then convert to integer
age = int(input("Enter your age: "))

# Conditional calculations. If user is over 18, they're old enough. 
if age > 18:
    print ("You are old enough!")
# If user is over 16, they are almost old enough
elif age > 16:
    print ("Almost there.")
# Otherwise, the user is too young
else:    
    print("You're just too young!")