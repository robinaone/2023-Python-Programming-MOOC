num = int
times = 0
sum = 0
mean = int
positive = 0
negative = 0
print("Please type in integer numbers. Type in 0 to finish. ")
while True:
    num = int(input("Number: "))
    if num == 0:
        break
    times += 1
    sum = sum + num
    if num > 0:
        positive += 1
    if num < 0:
        negative += 1
    mean = sum/times
print(f"... the program asks for numbers")
print(f"Numbers typed in {times}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")