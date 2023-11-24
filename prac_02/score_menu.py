def main():
    print("Welcome to the Score Calculator")

    while True:
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Enter your choice: ").upper()
        print()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def get_valid_score():
    while True:
        try:
            score = int(input("Enter a valid score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def print_result(score):
    if score is None:
        print("You have not entered a valid score yet.")
    else:
        print(f"Your score is: {score}")


def show_stars(score):
    if score is None:
        print("You have not entered a valid score yet.")
    else:
        print("Your stars: " + '*' * score)


if __name__ == "__main__":
    main()