# Instantiating user input & count_factor
# count_factor counts the number of factors in a particular number
user_nr = int(input("Enter any number: \n"))
count_factor = 0

# Start with checking that user has entered a valid positive number
if user_nr < 1:
    print("Enter another number greater than 1 \n")
    user_nr = int(input(""))
# In this for-statement (within elif statement, we make sure we count 1 AND the user number (with the +1)
# Check to see that any number within range has no remainder, if so, count as a factor
elif user_nr > 1:
    for x in range (1, user_nr+1):
        if (user_nr % x == 0):
            count_factor += 1
            
# If a number only has itself and the number 1 as factors, that number is prime
# Otherwise, it's not
if count_factor == 2:
    print(str(user_nr) + " is a prime number")
elif count_factor > 2:
    print(str(user_nr) + " is not a prime number")
    
