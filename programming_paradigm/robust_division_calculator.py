# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Safely divide two numbers and handle common errors."""
    try:
        # Try converting inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Check for division by zero
        if den == 0:
            return "Error: Cannot divide by zero."

        # Perform division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."
