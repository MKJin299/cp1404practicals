import random

MAX_NUMBER = 45
MIN_NUMBER = 1
NUMBERS_PER_PICK = 6

def main():
    num_picks = int(input("How many quick picks? "))
    for pick in range(num_picks):
        quick_pick = generate_quick_pick()
        print(" ".join("{:2}".format(number) for number in quick_pick))

def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick

main()