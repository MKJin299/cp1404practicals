total_price = 0

items = int(input("Number of items: "))

while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))
for i in range(1, items+1):
    price = float(input(f"Price of item {i}: "))
    total_price += price
if total_price > 100:
    total_price *=100

print(f"Total price for {items} items is ${total_price:.2f}")