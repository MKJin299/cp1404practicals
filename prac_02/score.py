"""Score categorizer program"""
import random

def main():
   """Get user score and print result, then generate random score and print result"""
   user_score = float(input("Enter score: "))
   result = get_score_status(user_score)
   print(result)

   random_score = random.randint(0, 100)
   result = get_score_status(random_score)
   print(f"Random score of {random_score} is {result}")

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

main()