
# Instantiate variables
name = input("Enter your name: ")
wrong_names = []
print_names = ""
print_names_final = ""

# While loop for each name entered that is not John
while name != "John":
    wrong_names.append(name)
    name = input("Enter your name: ")

# Add each name to a string
for names in wrong_names:
    print_names = print_names + "\'" + names + "\'" + ","
 
 # Could have used rstrip() function here to remove trailing comma. Didn't work when I tried
 # This is just another way
for i in range(0, len(print_names)-1): 
    print_names_final = print_names_final + print_names[i]
 
# Print result as in example 
print("Incorrect names: [" + print_names_final + "]")
    