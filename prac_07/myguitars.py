import csv
from guitar import Guitar


def main():
    """Read guitars from file, display them, and sort by year."""
    guitars = load_guitars("guitars.csv")
    display_guitars("All guitars:", guitars)

    guitars.sort()
    display_guitars("\nGuitars sorted by year:", guitars)

    add_new_guitars(guitars)
    save_guitars("guitars.csv", guitars)


def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(title, guitars):
    """Display a list of guitars."""
    print(title)
    for guitar in guitars:
        print(guitar)


def add_new_guitars(guitars):
    """Add new guitars to the list."""
    print("\nAdd new guitars (leave name blank to finish):")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))


def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == "__main__":
    main()
