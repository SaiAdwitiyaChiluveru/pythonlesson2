def calculate_circumference(radius):
    pi = 3.14159
    return 2 * pi * radius
r = float(input("Enter the radius: "))
circumference = calculate_circumference(r)
print("The circumference is: ", circumference)