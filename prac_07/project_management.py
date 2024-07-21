"""
File: project_management.py
This module contains the main program
Time Estimate: 2 hours
"""
import csv
from datetime import datetime
from project import Project

MENU = """\nMenu:
L - Load projects  
S - Save projects  
D - Display projects  
F - Filter projects by date
A - Add new project  
U - Update project
Q - Quit"""


def main():
    """Main function to run the project management program."""
    filename = 'projects.txt'
    projects = load_projects(filename)

    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {filename}")
    print(MENU)

    choice = input(">>> ").upper()

    while choice != 'Q':
        if choice == 'L':
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()

    if input("Would you like to save to projects.txt? ").lower() in ['yes', 'y']:
        save_projects('projects.txt', projects)

    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)
        for row in reader:
            projects.append(Project(*row))
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion"])
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime("%d/%m/%Y"), project.priority, project.cost,
                             project.completion])
    print(f"Saved {len(projects)} projects to {filename}")


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete = [project for project in projects if not project.is_complete()]
    completed = [project for project in projects if project.is_complete()]
    incomplete.sort()
    completed.sort()

    print("Incomplete projects: ")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects: ")
    for project in completed:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter projects by start date and display them."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.starts_after(filter_date)]
    filtered_projects.sort(key=lambda x: x.start_date)

    for project in filtered_projects:
        print(project)

if __name__ == "__main__":
    main()
