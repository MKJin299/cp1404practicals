"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer
        data.append(parts)
    input_file.close()
    return data


def display_subject_details(data):
    """Display subject details."""
    for subject in data:
        code, lecturer, students = subject
        print(f"{code} is taught by {lecturer} and has {students} students")


main()