"""
Wimbledon Champions
Estimate: 40 minutes
Actual: 60 minutes
"""

import csv


def main():
    filename = "wimbledon.csv"
    champions_data = read_csv_file(filename)
    champion_wins = count_champion_wins(champions_data)
    countries = get_countries(champions_data)

    print("Wimbledon Champions:")
    for champion, wins in champion_wins.items():
        print(f"{champion} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def read_csv_file(filename):
    champions_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header
        for row in reader:
            champions_data.append(row)
    return champions_data


def count_champion_wins(champions_data):
    champion_wins = {}
    for row in champions_data:
        champion = row[2]
        champion_wins[champion] = champion_wins.get(champion, 0) + 1
    return champion_wins


def get_countries(champions_data):
    countries = set()
    for row in champions_data:
        countries.add(row[1])
    return countries


if __name__ == "__main__":
    main()