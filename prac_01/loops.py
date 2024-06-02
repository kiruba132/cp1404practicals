"""
CP1404- Practical
loops
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. Print number stars. Ask the user for a number, then print that many stars (*), all on one line.
number_stars = int(input("Number of stars: "))
for i in range(number_stars):
    print('*', end='')
print()

# d. Print number lines of increasing stars.
for i in range(1, number_stars + 1):
    print('*' * i)
print()
