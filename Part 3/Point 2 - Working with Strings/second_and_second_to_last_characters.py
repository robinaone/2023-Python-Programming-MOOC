input_string = input("Please type in a string: ")
if input_string[1] == input_string[-2]:
    print(f"The second and the second to last characters are {input_string[1]}")
else:
    print("The second and the second to last characters are different")