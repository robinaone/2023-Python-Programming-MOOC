year = int(input("Please type in a year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("That year is a leap year.")
    else:
        print("That year is not a leap year.")
elif year % 4 == 0:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")


#first thing - % 4
#second thing - IF % 100, ALSO % 400
#else nope

#model solution:
#year = int(input("Please type in a year: "))
# 
# First, we make assumption that a year is not a leap year
#leap_year = False
# 
#if year % 100 == 0:
#    if year % 400 == 0:
#        leap_year = True
#elif year % 4 == 0:
#    leap_year = True
# 
#if leap_year:
#    print("That year is a leap year.")
#else:
#    print("That year is not a leap year.")