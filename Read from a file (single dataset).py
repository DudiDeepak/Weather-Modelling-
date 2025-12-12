import math

with open("input_single.txt", "r") as f:
    lines = f.read().strip().split()

a, b, c = map(float, lines)

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("No real solution")
else:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Solutions: x1 = {x1}, x2 = {x2}")
