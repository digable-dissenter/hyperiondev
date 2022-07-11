# Getting user product inputs
product1 = input("Enter product name: ")
product2 = input("Enter another product name: ")
product3 = input("Enter a third product name: ")

# Getting user float product price inputs
# Use the f-Strings format function to dynamically match product to price in user prompt
# Source: HyperionDev Python Chapter 3: The String Data Type
price1 = float(input(f"Enter {product1} price with decimals: "))
price2 = float(input(f"Enter {product2} price with decimals: "))
price3 = float(input(f"Enter {product3} price with decimals: "))

# Calculate the sum of all the prices user entered
total_price = price1 + price2 + price3
# Calculate the average of the prices user entered
ave_price = total_price / 3

# Again, used f-string format function to dynamically generate the user input products and the calculated total and average prices
print(f"The total of {product1}, {product2}, {product3} is R{total_price} and the average price of the items are R{ave_price}") 
