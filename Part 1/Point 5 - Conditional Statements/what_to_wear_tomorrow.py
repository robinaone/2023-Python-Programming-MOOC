print("What is the weather forecast tomorrow?")
temp = int(input("Temperature: "))
rain = (input("Will it rain (yes/no): "))
print("Wear jeans and a T-shirt")
if temp < 21:
    print("I recommend a jumper as well")
if temp < 11:
    print("Take a jacket with you")
if temp < 6:
    print("Make it a warm coat, actually\nI think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")