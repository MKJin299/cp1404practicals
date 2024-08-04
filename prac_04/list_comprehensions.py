"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)
    print("Completed list comprehensions:")
    print(subject_codes(data))
    print(subject_names(data))
    print(subject_numbers(data))
    print(subject_stats(data))


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = [line.strip().split(",") for line in input_file]
    input_file.close()
    for i in range(len(data)):
        data[i][2] = int(data[i][2])
    return data


def subject_codes(data):
    """Return a list of subject codes from the data."""
    # TODO: Create a list of subject codes from the data
    return [subject[0] for subject in data]


def subject_names(data):
    """Return a list of subject names from the data."""
    # TODO: Create a list of subject names from the data
    return [subject[1] for subject in data]


def subject_numbers(data):
    """Return a list of subject numbers from the data."""
    # TODO: Create a list of subject numbers from the data
    return [subject[2] for subject in data]


def subject_stats(data):
    """Return a list of tuples with subject details."""
    # TODO: Create a list of tuples with details for each subject
    return [(subject[0], subject[1], subject[2]) for subject in data]


main()