# math library will be used in this task
import math

# Defining binary function that will convert binary input into a decimal number
def binary(nr):
    # Instantiate answer local variable
    answer = 0
    # Convert to string to get length below (used in loop)
    y = str(nr)
    # Get length of binary
    x = len(y)
    # Loop through binary number length
    for dec in range(x):
        # Logic here tricky. Had to use string & integer types simultaneously to get sequence right
        answer += int(y[dec])*math.pow(2,x-dec-1)
    return answer

# Request user input. Integer conversion minimises chance program accepts non-numeric characters    
binary_nr = int(input("Enter a binary number: \n"))

# Call binary function
decimal_nr = binary(binary_nr)

# Print result
print(f"The equivalent decimal of binary number {binary_nr} is: {decimal_nr}")