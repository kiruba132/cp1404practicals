"""
File: project.py
This module contains the Project class and related methods.
"""

from datetime import datetime


class Project:
    """Class to represent a project."""

    def __init__(self, name, start_date, priority, cost, completion):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost = float(cost)
        self.completion = int(completion)

    def __str__(self):
        """Return a string representation of a Project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority: {self.priority}, estimate: ${self.cost:,.2f}, completion: {self.completion}%"

    def __lt__(self, other):
        """Less than, used for sorting Projects by priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Check if the project is complete."""
        return self.completion == 100

    def update_completion(self, completion):
        """Update the completion percentage of the project."""
        self.completion = completion

    def update_priority(self, priority):
        """Update the priority of the project."""
        self.priority = priority

    def starts_after(self, date):
        """Check if the project starts after the given date."""
        return self.start_date > date
