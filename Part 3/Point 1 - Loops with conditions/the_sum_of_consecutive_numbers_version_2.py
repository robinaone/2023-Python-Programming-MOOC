limit = int(input("Limit:"))
num = 1
sum = 1
x= "1"
while sum < limit:
    num += 1
    sum += num
    x += f" + {num}"
print(f"The consecutive sum: {x} = {sum}")