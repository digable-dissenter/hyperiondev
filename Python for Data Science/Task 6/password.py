
# Declare Boolean variables
have_length = False
up_case = False
low_case = False
have_num = False

# For each of the Boolean variables declared above, ask user input is required to determine if criteria met
pass_length = input("Is your password longer than 6 character? Yes/No: ")
pass_ucase = input("Does your password have any uppercase characters? Yes/No: ")
pass_lcase = input("Does your password have any lowercase characters? Yes/No: ")
pass_nr = input("Does your password have any numeric characters? Yes/No: ")

# Used to count number of criteria met. Will be increased by one if each question is answered with \"Yes"\. Instantiated to zero.
count = 0

# For each condition below, user input entered will be used to determine if password is satisfactory. 
# Count will incremented if true or else it will remain as is 
if pass_length == "Yes":
    have_length = True
    count = count + 1
elif pass_length == "No":
    have_length = False
    count
    
if pass_ucase == "Yes":
    up_case = True
    count = count + 1
elif pass_ucase == "No":
    up_case = False
    count
    
if pass_lcase == "Yes":
    low_case = True
    count = count + 1
elif pass_lcase == "No":
    low_case = False
    count
    
if pass_nr == "Yes":
    have_num = True
    count = count + 1
elif pass_nr == "No":
    have_num = False
    count

# Displays message if 3 or more positive password criteria are met. If not, tells user to change password   
if count >= 3:
    print ("Your password is satisfactory. Well done!")
else:
    print ("Please change your password.")

