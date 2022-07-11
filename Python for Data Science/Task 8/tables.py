# Req user input and instantiate variables
# product is the multiplication of the user_input and the index variable
user_input = int(input("Choose any number: \n"))
product = 0
print("The " + str(user_input) + " times table is:")

# for this for loop, the range can be anything (not specified in instructions)
# index variable multiplied by user input to produce product
for i in range(1, 13):
    product = i * user_input    
    print(str(user_input) + " * " + str(i) + " = " + str(product))

