"""
CP1404 - Practical
Shop Calculator
"""
total_price = 0
number_items = int(input("Number of items: "))
while number_items < 0:
    print("Can't be below 0")
    number_items = int(input("Number of items: "))
for i in range(number_items):
    price = float(input("Price of item: "))
    total_price += price
if total_price > 100:
    total_price *= 0.9
print(f"Total price for {number_items} items is ${total_price:.2f}")
