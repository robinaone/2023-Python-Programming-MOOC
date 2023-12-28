string = input("Please type in a string: ")
x = -1
sum = ""
while x >= -len(string):
    sum = string[x] + sum
    print(sum)
    x -= 1