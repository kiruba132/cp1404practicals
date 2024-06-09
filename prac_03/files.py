"""
CP1404/CP5632 - Practical - Suggested Solution
Quick file opening/writing/reading exercises
"""

# Q1 - Write user's name to file
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# Q2 - Read user's name from file
inside_file = open("name.txt", "r")
name = inside_file.read().strip()
inside_file.close()
print("Your name is", name)

# Q3 - Read and compute sum of two numbers from file
inside_file = open("numbers.txt", "r")  # Corrected filename to lowercase
first_line = int(inside_file.readline())
second_line = int(inside_file.readline())
result = first_line + second_line
print("Sum of line 1 & 2 is", result)
inside_file.close()

# Q4 - Read and compute sum of all numbers from file
inside_file = open("numbers.txt", "r")
total = 0
for line in inside_file:
    number = int(line.strip())
    total += number
print("The sum of all lines is", total)
inside_file.close()
