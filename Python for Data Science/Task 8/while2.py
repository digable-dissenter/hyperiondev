# This task confused me. It specified finding asking for the user's name, but says user should input the correct number?
# Request user input and instantiate variables
# count_tries counts the number of numbers entered

user_number = int(input("Enter any number: \n"))

# user_name = input("Enter your name: \n")
correct_number = 9
count_tries = 0

# while loop runs infinitely until user enters the correct number
# count_tries is incremented for every wrong number entered
while user_number != correct_number:
    count_tries += 1
    user_number = int(input("Incorrect. Enter another number: \n"))  

# print result: no of tries before correct number entered
print("The number of tries it took before you entered correct number: " + str(count_tries))

# Added a prompt for user to immediately quit the program
quit_prompt = input("Would you like to quit the game? Y/N \n")    
if quit_prompt == "Y":
        quit()
