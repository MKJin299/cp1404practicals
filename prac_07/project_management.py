"""
Estimated Time: 90 minutes
Actual Time: 120 minutes
"""

import datetime
from project import Project


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            projects.append(Project(*parts))
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    incomplete = [p for p in projects if not p.is_completed()]
    completed = [p for p in projects if p.is_completed()]

    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed):
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [p for p in projects if p.start_date > date]
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(project)


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    percent_complete = input("Percent complete: ")
    new_project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(new_project)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    project.update(new_percentage if new_percentage else None,
                   new_priority if new_priority else None)


def main():
    filename = "projects.txt"
    projects = load_projects(filename)
    print(f"Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {filename}")

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
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? ")
            if save_choice.lower() in ['yes', 'y']:
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()