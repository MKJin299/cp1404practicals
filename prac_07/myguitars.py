"""
My Guitars
Estimate: 20 minutes
Actual:   25 minutes
"""

import csv


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= 50

    def __lt__(self, other):
        return self.year < other.year


CURRENT_YEAR = 2023


def read_guitars():
    with open('guitars.csv', 'r') as file:
        reader = csv.reader(file)
        guitars = [Guitar(name, int(year), float(cost)) for name, year, cost in reader]
    return guitars


def write_guitars(guitars):
    with open('guitars.csv', 'w') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def add_guitar():
    name = input("Enter guitar name: ")
    year = int(input("Enter year: "))
    cost = float(input("Enter cost: "))
    return Guitar(name, year, cost)


def main():
    guitars = read_guitars()
    new_guitar = add_guitar()
    guitars.append(new_guitar)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    write_guitars(guitars)


if __name__ == "__main__":
    main()