# Find largest of 2 numbers

def find_largest(a, b):
    """Return the largest of two numbers."""
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None  # equal

# --- Main ---
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

result = find_largest(a, b)

if result is None:
    print("Both numbers are equal")
else:
    print(f"{result} is the largest")