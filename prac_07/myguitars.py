import csv
from guitar import Guitar


def main():
    """Read guitars from file, display them, and sort by year."""
    guitars = load_guitars("guitars.csv")
    display_guitars("All guitars:", guitars)

    guitars.sort()
    display_guitars("\nGuitars sorted by year:", guitars)


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


if __name__ == "__main__":
    main()
