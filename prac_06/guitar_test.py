"""
guitar
Estimate: 60 minutes
Actual: 70 minutes
"""

from guitar import Guitar
import datetime

def run_tests():
    current_year = datetime.datetime.now().year

    # Test 1
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    guitar = Guitar(name, year, cost)
    age = current_year - year
    print(f"{guitar.name} get_age() - Expected {age}. Got {guitar.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")

    # Test 2
    name = "Another Guitar"
    year = 2013
    cost = 1000.00
    guitar = Guitar(name, year, cost)
    age = current_year - year
    print(f"{guitar.name} get_age() - Expected {age}. Got {guitar.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected False. Got {guitar.is_vintage()}")

    # Test 3 (Edge case: exactly 50 years old)
    name = "Edge Case Guitar"
    year = current_year - 50
    cost = 2000.00
    guitar = Guitar(name, year, cost)
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")

    # Test 4 (Intentional failure case)
    name = "Failure Case Guitar"
    year = current_year - 49
    cost = 2000.00
    guitar = Guitar(name, year, cost)
    print(f"{guitar.name} is_vintage() - Expected False. Got {guitar.is_vintage()}")

if __name__ == '__main__':
    run_tests()