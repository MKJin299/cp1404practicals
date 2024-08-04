# File: myguitars.py

from guitar import Guitar


def main():
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("Loaded guitars:")
    display_guitars(guitars)

    print("\nSorted guitars by year:")
    guitars.sort()
    display_guitars(guitars)

    print("\nAdd new guitars:")
    while True:
        new_guitar = get_new_guitar()
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        if input("Add another guitar? (y/n) ").lower() != 'y':
            break

    print("\nUpdated list of guitars:")
    display_guitars(guitars)

    save_guitars(filename, guitars)
    print(f"\nGuitars saved to {filename}")


def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def save_guitars(filename, guitars):
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def display_guitars(guitars):
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def get_new_guitar():
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    return Guitar(name, year, cost)


if __name__ == "__main__":
    main()