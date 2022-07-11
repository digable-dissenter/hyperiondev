# For this assignment, I had to read ahead on lists
# Also referred to stack overflow: Reference: https://stackoverflow.com/questions/57708727/python-3-input-text-file-manipulation-requiring-loops-splitting-string-indexi
f = open('DOB.txt', 'r+')
count_name = 0
count_birth_date = 0
# Declare names and birth_dates lists to store each of the names and birth dates
names = []
birth_dates = []
print("Name \n")

# Use for loop for each line in file
for line in f:    
    name = ""
    birth_date = ""
# String split used to identify whitespace characters on which to split names and birth dates
    row_delimiter = line.split()
# Add string from 0 index white space and 1 index whitespace for name    
    name = name + row_delimiter[0] + " " + row_delimiter[1]
# Add string from 2nd index white space, 3rd and 4th index whitespace for birth date 
    birth_date = birth_date + row_delimiter[2] + " " + row_delimiter[3] + " " + row_delimiter[4]
# Add name to names list
    names.append(name)
# Add birth date to birth dates list
    birth_dates.append(birth_date)

# Display contents of names list  
for line in names:
    count_name += 1
    print(str(count_name) + ".\t" + line)

# Display contents of birth dates list  
print ("\nBirth dates\n")
for line in birth_dates:
    count_birth_date += 1
    print(str(count_birth_date) + ".\t" + line)
f.close()
