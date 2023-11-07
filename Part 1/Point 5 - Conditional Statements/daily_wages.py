hourly = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
day_of_week = input("Day of the week: ")
daily_wage = hourly*hours_worked

if day_of_week == "Sunday":
    print(f"Daily wages: {(hourly*2)*hours_worked} euros")
else:
    print(f"Daily wages: {daily_wage} euros")

#Sample solution (I like it better:)
#hourly_wage = float(input("Hourly wage: "))
#hours_worked = int(input("Hours worked: "))
#weekday = input("Day of the week: ")
# 
#if weekday == "Sunday":
    # The salary is double on Sundays
    #hourly_wage *= 2
# 
#total_wage = hourly_wage * hours_worked
#print(f"Daily wages: {total_wage} euros")