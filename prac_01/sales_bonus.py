"""
CP1404/CP5632 - Practical 1
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus =sales * 0.1
    else:
        bonus =sales * 0.15

    print("Bonus is $", bonus, sep='')
    sales = float(input("Enter sales: $"))