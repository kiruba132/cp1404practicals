"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# NOTE:  I didn't read the practice instructions properly. I thought we could choose two programs ourselves from prac 1 to refactor for functions. Its complete anyways.

def main():
    get_and_calculate_sales()


def get_and_calculate_sales():
    sales = get_sales()
    while sales >= 0:
        bonus = calculate_bonus(sales)
        print_bonus(bonus)
        sales = get_sales()


def get_sales():
    return float(input("Enter sales: $"))


def calculate_bonus(sales):
    if sales < 1000:
        return sales * 0.10
    else:
        return sales * 0.15


def print_bonus(bonus):
    print("Bonus is $", bonus, sep='')

main()
