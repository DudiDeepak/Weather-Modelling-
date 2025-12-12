import math

# Hard-coded coefficients (example weather-model parameters)
a = 1.2
b = -3.6
c = 2.4

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("No real solution")
else:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Solutions: x1 = {x1}, x2 = {x2}")
