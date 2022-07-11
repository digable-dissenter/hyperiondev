fav_rest = input("Enter your favourite restaurant: ")
int_fav = int(input("Enter your favourite number: "))
print ("Your favourite restaurant is " + fav_rest)
print ("Your favourite number is " +  str(int_fav))

# When trying to cast fav_rest to int a runtime error occurs.
# The actual error in Python produces the value error meesage: invalid literal for int() with base 10: '{string input}'
# It indicates that you are passing a string argument with non-integer characters, i.e. digits, or null/empty value
# Source 1: Runtime error - https://techterms.com/definition/runtime_error#:~:text=A%20runtime%20error%20is%20a,which%20produces%20the%20wrong%20output.
# Source 2: https://www.edureka.co/community/30685/this-valueerror-invalid-literal-for-with-base-error-python#:~:text=The%20error%20message%20invalid%20literal,it%20other%20than%20a%20digit.
