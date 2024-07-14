"""
File: programming_language.py
Start Time: 7:40 PM
Finish Time: 8:45 PM
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initializes a new programming language object with the given attributes."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns True if the language is  typed, False otherwise."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Returns a string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"


def run_demos():
    """Run simple demos on ProgrammingLanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Create a list of programming languages
    languages = [python, ruby, visual_basic]
    print(python)

    # Loop through and print the names of all the languages with dynamic typing (from paper)
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_demos()
