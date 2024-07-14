"""
File: language.py.py
Start Time: 7:40 PM
Finish Time: 8:45 PM
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)


# Create a list of programming languages
languages = [python, ruby, visual_basic]
print(python)

# Loop through and print the names of all the languages with dynamic typing
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)

