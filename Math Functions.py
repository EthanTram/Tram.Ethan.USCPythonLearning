import math

# Testing points

a = 3

b = 4

c = 5

# Testing functions
def sum(a, b, c):
    return a + b + c

def product(a, b, c):
    return a * b * c

def largest(a, b, c):
    return max(a, b, c)

def smallest(a, b, c):
    return min(a, b, c)

def area(a, b, c):
    # Check triangle if it's possible
    if not triangle_possible(a, b, c):
        return f"No triangle exists with side lengths {a}, {b}, and {c}"

    # Calculate area using Heron's formula
    s = (a + b + c) / 2
    area_value = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area_value

def triangle_possible(a, b, c):
    return ( a + b > c) and (b + c > a) and (a + c > b )

# Print outputs

print("Sum:", sum(a, b, c))
print("Product:", product(a, b, c))
print("Largest:", largest(a, b, c))
print("Smallest", smallest(a, b, c))
print("Area", area(a, b, c))
