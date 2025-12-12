import math

with open("input_multiple.txt", "r") as f:
    for line in f:
        if not line.strip():
            continue
        a, b, c = map(float, line.split())
        discriminant = b**2 - 4*a*c

        print(f"\nEquation: {a}x^2 + {b}x + {c} = 0")

        if discriminant < 0:
            print("  No real solutions")
        else:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            print(f"  x1 = {x1}, x2 = {x2}")
