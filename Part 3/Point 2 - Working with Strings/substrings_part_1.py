string = input("Please type in a string: ")
x = 0
sum = ""
while x < len(string):
    sum += string[x]
    print(sum)
    x += 1