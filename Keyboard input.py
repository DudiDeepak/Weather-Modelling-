import math

print("Enter coefficients for ax^2 + bx + c = 0")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("No real solution")
else:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Solutions: x1 = {x1}, x2 = {x2}")

