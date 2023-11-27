# TODO: Use f-string formatting to produce the output:
model_name = "Gibson L-5 CES"
year_made = 1922
cost = 16035.4

print(f"{year_made} {model_name} for about ${cost:,.2f}!")

# TODO: Using a for loop with the range function and string formatting,
numbers = [1, 19, 123, 456, -25]

for number in numbers:
    print(f"{number:6}")