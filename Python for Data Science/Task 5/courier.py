# Convert the user's input into float variable
pack_price = float(input("Enter the price of the package you would like to purchase: "))

# Convert the user's input into float variable. Could also be integer.
distance = float(input("Enter the delivery distance: "))

# Prompt user input for each of the categories
delivery = input("Select which delivery method would you prefer between air or freight? ")
insurance = input("Select whether you'd prefer full or limited insurance: ")
gift = input("Would you like to include this as a gift or not? Choose Y/N ")
priority_del = input("Would you prefer priority or standard delivery? ")

# For each category except gift option (uppercase), convert user input into lowercase
# This is to eliminate ambiguity for each condition for the if-statements.
# Multiply distance by air delivery price. Otherwise multiply by freight delivery price
if delivery.lower() == "air":
        total_cost = 0.36 * distance
else:
        total_cost = 0.25 * distance

# Add the full insurance cost to total cost. Otherwise add standard insurance cost to total cost insurance.lower() == "full":
        total_cost = total_cost + 50.00
else:
        total_cost = total_cost + 25.00

# Add the gift cost to total cost if 'Y' selected. Otherwise leave total cost as is       
if gift.upper() == "Y":
        total_cost = total_cost + 15.00
else:
        total_cost

# Add the priority delivery cost to total cost. Otherwise add standard delivery cost to total cost      
if priority_del.lower() == "priority":
        total_cost = total_cost + 100.00
else:
        total_cost = total_cost + 20.00
        
# Add the product purchase price to total cost
total_cost = total_cost + pack_price

# Print total cost
print ("Your total cost comes to: $" + str(total_cost))
