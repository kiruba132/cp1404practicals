import csv
from guitar import Guitar  # Import the Guitar class from the guitar module


def main():
    filename = 'guitars.csv'
    guitars = read_guitars_from_file(filename)

    print("All guitars:")
    for guitar in guitars:
        print(guitar)

    add_new_guitars(guitars)

    guitars.sort()

    print("\nGuitars sorted by year (oldest to newest):")
    for guitar in guitars:
        print(guitar)

    write_guitars_to_file(filename, guitars)


def read_guitars_from_file(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def add_new_guitars(guitars):
    """Add new guitars to the list."""
    print("\nAdd new guitars (leave name blank to finish):")
    name = input("Name: ")
    while name:
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")


def write_guitars_to_file(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == "__main__":
    main()
