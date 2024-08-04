"""Score Menu Program"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
   """Score Menu Program"""
   print("Welcome to the Score Menu Program!")
   score = get_valid_score()

   choice = input(MENU).upper()
   while choice != 'Q':
       if choice == 'G':
           score = get_valid_score()
       elif choice == 'P':
           print(get_score_status(score))
       elif choice == 'S':
           print_stars(score)
       else:
           print("Invalid choice")
       print()
       choice = input(MENU).upper()

   print("Farewell!")

def get_valid_score():
   """Get a valid score between 0 and 100 inclusive"""
   score = int(input("Enter a score between 0 and 100: "))
   while score < 0 or score > 100:
       print("Invalid score")
       score = int(input("Enter a score between 0 and 100: "))
   return score

def get_score_status(score):
   """Determine status based on score"""
   if score < 0 or score > 100:
       return "Invalid score"
   elif score >= 90:
       return "Excellent"
   elif score >= 50:
       return "Passable"
   else:
       return "Bad"

def print_stars(score):
   """Print stars based on the score"""
   print('*' * score)

main()