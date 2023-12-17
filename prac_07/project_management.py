"""
Project Management
Estimate: 100 minutes
Actual:   120 minutes
"""

import datetime
from project import Project


def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r') as file:
            next(file)  # Skip header
            for line in file:
                data = line.strip().split('\t')
                start_date = datetime.datetime.strptime(data[1], "%d/%m/%Y").date()
                project = Project(data[0], start_date, int(data[2]), float(data[3]), int(data[4]))
                projects.append(project)
    except FileNotFoundError:
        pass  # Handle file not found error if needed
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects, date_str):
    filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > filter_date]

    for project in filtered_projects:
        print(f"  {project}")


def add_new_project(projects):
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = int(input("Project choice: "))
    selected_project = projects[choice]

    new_completion_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")

    if new_completion_percentage:
        selected_project.completion_percentage = int(new_completion_percentage)
    if new_priority:
        selected_project.priority = int(new_priority)


if __name__ == "__main__":
    projects_filename = "projects.txt"
    projects = load_projects(projects_filename)

    while True:
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()

        if choice == 'l':
            projects = load_projects(input("Enter filename to load projects from: "))
        elif choice == 's':
            save_projects(input("Enter filename to save projects to: "), projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_date = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, filter_date)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            print("Thank you for using custom-built project management software.")
            break
