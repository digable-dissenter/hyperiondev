# Request user input and instantiate variables
# total for sum of all numbers entered
# count_num counts the number of numbers entered
# average will then divide the total by count_num

user_nr = int(input("Enter a number: \n"))
total = 0
count_num = 0
average = 0.00

# while loop runs infinitely until user enters -1
# if statement has to come first to evaluate initial user input (to see if it -1)
# if it is -1, program terminates and total & count_num aren't added to
# else if not -1, total & count_num are added to
while user_nr != -1:
    if user_nr == -1:
        total
        count_num
    else:
        total += user_nr
        count_num += 1
    user_nr = int(input("Enter another number: \n"))
    
# calculate average    
average = total / count_num
# print result
print("The average of the numbers you entered is: " + str(average))
