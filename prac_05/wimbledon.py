"""
Wimbledon
Estimate: 40 minutes
Actual:   1hr +
This was a bit tricky, looked online
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read data file and print details about Wimbledon champions and countries."""
    records = read_records(FILENAME)
    champion_to_count = count_champions(records)
    countries = collect_countries(records)
    display_results(champion_to_count, countries)


def read_records(filename):
    """Read records from CSV file and return them as a list of lists."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        next(file)
        for line in file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def count_champions(records):
    """Count number of wins for each champion."""
    champion_to_count = {}
    for record in records:
        champion = record[INDEX_CHAMPION]
        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1
    return champion_to_count


def collect_countries(records):
    """Collect unique countries of the champions."""
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
    return countries


def display_results(champion_to_count, countries):
    """Display champions and countries."""
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
