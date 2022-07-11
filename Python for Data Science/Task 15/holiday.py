import math

# Defining function HotelCost to calc hotel cost
def HotelCost(no_nights):
    total_cost = no_nights*699.99
    return total_cost
 
# Defining function PlaneCost to calc cost of plane ride 
def PlaneCost(user_city):
    if city == 'Port Elizabeth':
        total_cost = 499.99
    elif city == 'Cape Town':
        total_cost = 799.99
    elif city == 'Johannesburg':
        total_cost = 749.99
    elif city == 'Durban':
        total_cost = 699.99
    else:
        total_cost = 449.99
    return total_cost
    
# Defining function CarRental to calc cost of hiring a car     
def CarRental(no_car_days):
    total_cost = no_car_days * 50
    return total_cost
   
# Defining function CarRental to calc cost/value of holiday using 3 functions defined above
def HolidayCost(no_nights,user_city,no_car_days):
    x = HotelCost(no_nights)
    y = PlaneCost(user_city)
    z = CarRental(no_car_days)
    # Math function fsum adds input from arguments passed from answers from functions defined above
    answer = math.fsum([x, y, z])
    return answer
    
# Request user input (for function parameters)    
nr_nights = int(input("Enter how many nights you intend on staying at the hotel:\n"))
city = input("Enter which city you are flying to:\n")
nr_car_days = int(input("Enter how many days you you intend on using the car rental service:\n"))

# Call HolidayCost function to do calcs
holiday_cost = HolidayCost(nr_nights,city,nr_car_days)

#Print result
print(f"The total value/cost of your holiday amounts to: R{holiday_cost}")