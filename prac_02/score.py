import random

def score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    score = float(input("Enter score: "))
    print(score_status(score))

    random_score = random.randint(0, 100)
    print("Random score:", random_score)
    print("Status:", score_status(random_score))

if __name__ == "__main__":
    main()