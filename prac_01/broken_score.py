"""
CP1404- Practical
Broken program to determine score status
"""

# TODO: Fix this! - I know the category variable is not necessary as it can be done without it, i have chosen to do this way so it replicates what was tought in lectures.

score = float(input("Enter score: "))
if score < 0 or score > 100:
    category = "Invalid score"
elif score >= 90:
    category = "Excellent"
elif score >= 50:
    category = "Passable"
else:
    category = "Bad"
print(f"Your score of {score} is considered {category}")

