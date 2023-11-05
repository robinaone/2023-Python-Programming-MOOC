times_week = int(input("How many times a week do you eat at the student cafeteria? "))
price_lunch = float(input("The price of a typical student lunch? "))
groceries_week = float(input("How much money do you spend on groceries in a week? "))
weekly = (times_week*price_lunch)+groceries_week
daily = weekly/7
print(f"Average food expenditure:\nDaily: {daily} euros\nWeekly: {weekly} euros")

#Sample solution:
#times_in_cafeteria = int(input("How many times a week do you eat at the student cafeteria? "))
#price_of_lunch = float(input("The price of a typical student lunch? "))
#groceries = float(input("How much money do you spend on groceries in a week? "))
# 
#weekly = groceries + times_in_cafeteria * price_of_lunch
# 
#print("Average food expenditure:")
#print(f"Daily: {weekly / 7} euros")
#print(f"Weekly: {weekly} euros")