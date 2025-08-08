def safe_divide(numerator, denominator):
    try:
        answer = float(numerator)/float(denominator)
        return f"The result of the division is {answer}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."



