password = input("Password: ")
while True:
    repeat_password = input("Repeat password: ")
    if password != repeat_password:
        print("They do not match!")
    elif password == repeat_password:
        print("User account created!")
        break