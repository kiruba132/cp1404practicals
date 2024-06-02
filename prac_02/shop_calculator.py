"""
CP1404 - Practical
Shop Calculator
"""
# NOTE:  I didn't read the practice instructions properly. I thought we could choose two programs ourselves from prac 1 to refactor for functions. Its complete anyways.

def main():
    total_price = 0
    number_items = get_number_of_items()
    total_price = get_total_price(number_items, total_price)
    if total_price > 100:
        total_price *= 0.9
    print(f"Total price for {number_items} items is ${total_price:.2f}")


def get_total_price(number_items, total_price):
    for i in range(number_items):
        price = float(input("Price of item: "))
        total_price += price
    return total_price


def get_number_of_items():
    number_items = int(input("Number of items: "))
    while number_items < 0:
        print("Can't be below 0")
        number_items = int(input("Number of items: "))
    return number_items


main()
