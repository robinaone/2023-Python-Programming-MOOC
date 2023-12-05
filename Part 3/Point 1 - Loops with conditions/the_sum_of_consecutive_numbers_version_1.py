limit = int(input("Limit:"))
num = 1
sum = 1
while sum < limit:
    num += 1
    sum += num
print(sum)