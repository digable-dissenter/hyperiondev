# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

animal = "Lion"       # Error 1: Runtime error (Lion incorrectly defined)    
animal_type = "cub" # Error 2: Compilation error (no indent)
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" # Error 3+4: Runtime error (No formatting applied) + Logic error (last two variable should be swapped)

print (full_spec)   # Error 3: Compilation error (no parenthesis)

