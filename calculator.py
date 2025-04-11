# calculator.py

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a divided by b.
    Raises a ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    # Simple CLI interface for testing manually
    print("Add: ", add(10, 5))
    print("Subtract: ", subtract(10, 5))
    print("Multiply: ", multiply(10, 5))
    print("Divide: ", divide(10, 5))
