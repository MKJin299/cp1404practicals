"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   A ValueError will occur when the user enters a value that cannot be converted to an integer
   using the int() function. This could happen if the user enters a non-numeric value (like
   "hello" or "3.14") or an empty string.

2. When will a ZeroDivisionError occur?
   A ZeroDivisionError will occur when the user enters 0 as the denominator. In mathematics,
   division by zero is undefined, so Python raises a ZeroDivisionError to prevent this
   invalid operation.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   Yes, we can change the code to avoid the ZeroDivisionError by checking if the denominator
   is zero before performing the division. If it is zero, we can handle it without raising
   an exception, for example, by printing a message and not performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")