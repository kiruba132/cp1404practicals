"""
CP1404- Practical
Broken program to determine score status
"""
# I searched online for help for this one, got stuck.

import random


# Main function
def main():
    # Function to determine score category
    def determine_category(score):
        if score < 0 or score > 100:
            return "Invalid score"
        elif score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"

    # Function to print score category
    def print_score_category(score, category):
        print(f"Your score of {score} is considered {category}")

    print("CP1404 - Practical\nScore Evaluation\n")

    # Get user score
    user_score = float(input("Enter score: "))
    user_category = determine_category(user_score)
    print_score_category(user_score, user_category)

    # Generate random score
    random_score = random.randint(0, 100)
    random_category = determine_category(random_score)
    print(f"\nRandomly generated score: {random_score}")
    print_score_category(random_score, random_category)


main()
