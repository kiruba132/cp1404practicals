# list_exercises.py

# Prompt the user for 5 numbers and store them in a list called numbers
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

# Output information about the numbers
print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is", sum(numbers) / len(numbers))