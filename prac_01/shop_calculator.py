"""
CP1404/CP5632 - Practical 1
"""

total = 0

num_of_items = int(input("Number of items: "))

while num_of_items < 0:
    print("Invalid number of items!")
    num_of_items = int(input("Number of items: "))

for i in range(num_of_items):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9

print(f"Total price for {num_of_items} items is ${total:.2f}")