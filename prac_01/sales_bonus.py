"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

BONUS_UNDER_1000 = 0.1
BONUS_OVER_1000 = 0.15

while True:
    sales = float(input("Enter sales: $"))

    if sales < 0:
        break

    if sales < 1000:
        bonus = sales * BONUS_UNDER_1000
    else:
        bonus = sales * BONUS_OVER_1000

    print("Bonus: $", bonus)