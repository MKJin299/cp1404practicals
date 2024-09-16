import random

# What did you see on line 1?
# Answer: I saw random integers between 5 and 20 (inclusive).

# What did you see on line 2?
# Answer: I saw odd numbers between 3 and 9.
# No, line 2 could not have produced a 4 because it only generates
# odd numbers (starting from 3 and stepping by 2).

# What did you see on line 3?
# Answer: I saw random floating-point numbers between 2.5 and 5.5.

# Write code to produce a random number between 1 and 100 inclusive.
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")