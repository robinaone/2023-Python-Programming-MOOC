gift = int(input("Value of gift: "))
if gift > 1000000:
    lower_limit = 1000000
    lower_tax = 142100
    exceeding_tax = .17
    tax = (lower_tax + (gift - lower_limit) * exceeding_tax)
    print(f"Amount of tax: {tax}")
elif gift < 1000000 and gift >= 200000:
    lower_limit = 200000
    lower_tax = 22100
    exceeding_tax = .15
    tax = (lower_tax + (gift - lower_limit) * exceeding_tax)
    print(f"Amount of tax: {tax}")
elif gift < 200000 and gift >= 55000:
    lower_limit = 55000
    lower_tax = 4700
    exceeding_tax = .12
    tax = (lower_tax + (gift - lower_limit) * exceeding_tax)
    print(f"Amount of tax: {tax}")
elif gift < 55000 and gift >=25000:
    lower_limit = 25000
    lower_tax = 1700
    exceeding_tax = .10
    tax = (lower_tax + (gift - lower_limit) * exceeding_tax)
    print(f"Amount of tax: {tax}")
elif gift < 25000 and gift >= 5000:
    lower_limit = 5000
    lower_tax = 100
    exceeding_tax = .08
    tax = (lower_tax + (gift - lower_limit) * exceeding_tax)
    print(f"Amount of tax: {tax}")
else:
    print("No tax!")

#model solution - WAY simpler
#value = int(input("Value of gift: "))
#if value < 5000:
#    tax = 0
#elif value <= 25000:
#    tax = 100 + (value - 5000) * 0.08
#elif value <= 55000:
#    tax = 1700 + (value - 25000) * 0.10
#elif value <= 200000:
#    tax = 4700 + (value - 55000) * 0.12
#elif value <= 1000000:
#    tax = 22100 + (value - 200000) * 0.15
#else:
#    tax = 142100 + (value - 1000000) * 0.17 
#if tax == 0:
#    print("No tax!")
#else:
#    print(f"Amount of tax: {tax} euros")