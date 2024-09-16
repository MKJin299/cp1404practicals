guitar = "Gibson L-5 CES"
year = 1922
cost = 16035.4
print(f"{year} {guitar} for about ${cost:,.2f}!")

print("\nPrinting powers of 2 using f-string formatting:")
for i in range(11):
    print(f"{2} ^ {i:2} is {2 ** i:>5}")