"""
File: guitar_test.py
Start Time: 9:10 PM
Finish Time: 11:15 PM
"""

from prac_06.guitar import Guitar


def main():
    """Manage a collection of guitars."""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        name = input("Name: ")

    # For testing purposes.
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))

    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars to display.")


if __name__ == '__main__':
    main()
