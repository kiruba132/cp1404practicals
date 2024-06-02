"""
CP1404- Practical
Broken program to determine score status
"""
# I searched online for help for this one, got stuck.


import random


def main():
    # Get a numeric score, display its status, and also display the status of a random score.
    score = float(input("Enter score: "))
    print(determine_status(score))

    # Generate a random score and display its status
    random_score = random.uniform(0, 100)  # Generate a random score between 0 and 100
    print(f"Random score: {random_score:.2f}, Status: {determine_status(random_score)}")


def determine_status(score):
# Determine the status of a given score
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
