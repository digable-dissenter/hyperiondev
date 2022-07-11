# menu list created
menu = ['chicken','beef','lamb','vegan']

# stock and price dictionaries created
stock = {
            'chicken': 100,
            'beef': 150,
            'lamb': 44,
            'vegan': 36
        }

price = {
            'chicken': 6.00,
            'beef': 5.50,
            'lamb': 10.99,
            'vegan': 9.00
        } 

# totalStock function calcs the worth of the cafe by multiplying each item on menu with stock and price       
def totalStock():
    answer = 0
    for item in menu:
        answer = answer + (float(stock[item]) * float(price[item]))
    return answer    

# Displaty cafe stock worth          
print("The total worth of the stock in the cafe is R" + str(totalStock()))      
