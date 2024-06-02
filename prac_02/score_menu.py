# I searched online for help for this one, got stuck.

# Main function
def main():
    print("CP1404 - Practical\nScore Evaluation\n")

    score = get_valid_score()

    # Initialize choice variable
    choice = ""
    while choice != "Q":
        # Display menu
        print("\nMENU:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_score_category(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Thank you for using the program. Goodbye!")
        else:
            print("Invalid option. Please choose again.")


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
def print_score_category(score):
    category = determine_category(score)
    print(f"Your score of {score} is considered {category}")


# Function to show stars based on score
def show_stars(score):
    print("*" * int(score))


# Function to get a valid score from user input
def get_valid_score():
    score = -1
    while score < 0 or score > 100:
        score_str = input("Enter score (0-100): ")
        if score_str.isdigit():
            score = float(score_str)
            if score < 0 or score > 100:
                print("Score must be between 0 and 100.")
        else:
            print("Invalid input. Please enter a number.")
    return score


main()
