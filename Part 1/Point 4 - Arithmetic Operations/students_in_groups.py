number_of_students = int(input("How many students on the course? "))
desired_group_size = int(input("Desired group size? "))
print(f"Number of groups formed: {-(-number_of_students//desired_group_size)}")
#SO, -(-numerator//denominator) does something called "ceiling division" where the SMALLEST integer is displayed. WOW.