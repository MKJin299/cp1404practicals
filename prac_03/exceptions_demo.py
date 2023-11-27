# 1. When either the denominator or the numerator is not a valid integer, a ValueError will occur. For example, a ValueError will be raised if the user enters "five" rather than 5.

# 2. A ZeroDivisionError will occur when the denominator is 0. In this code, this would happen if the user inputs 0 for the denominator.

# 3.
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction, remainder = divmod(numerator, denominator)
    if remainder:
        print(f"{numerator} divided by {denominator} is {fraction} with a remainder of {remainder}")
    else:
        print(f"{numerator} divided by {denominator} is {fraction}")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")