# user inputs for start year and number of consecutive years to display
# end_year will serve as the outer limit of the range
start_year = int(input("What year do you want to start with? \t"))
no_years = int(input("How many years do you want to check? \t"))
end_year = start_year + no_years

# for loop loops from range input (start) and calculated (end)
# conditional statement to determine if each year is a leap year or not
for i in range (start_year, end_year):
    if i%4==0:
        print(str(i) + " is a leap year")
    elif i%4!=0:
        print(str(i) + " isn’t a leap year")