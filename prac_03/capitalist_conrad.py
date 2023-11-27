import random

MAX_INCREASE = 0.175 # 17.5%
MAX_DECREASE = 0.075 # 7.5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = 'stock_prices.txt'

number_of_days = 0
price = INITIAL_PRICE

out_file = open(OUTPUT_FILE, 'w')
print(f"Starting price: ${price:,.2f}")
out_file.write(f"Starting price: ${price:,.2f}\n")

while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1
    price_change = 0

    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}")
    out_file.write(f"On day {number_of_days} price is: ${price:,.2f}\n")

out_file.close()