# 1. Line 1's random integer was a value in the range of 5 to 20. The algorithm used by the random number generator will determine the exact number that is produced.

# 2. Line 2's random integer was an even value that fell between 3 and 10 (not included 10). Ten would be the biggest number produced, while four would be the least.

# 3. On line 3, the random floating point value ranged from 2.5 to 5.5. The algorithm used by the random number generator will determine the exact number that is produced.

# 4.
import random

random_number = random.randint(1, 100)
print(random_number)