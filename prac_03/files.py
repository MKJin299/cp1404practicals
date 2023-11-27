def read_write_name():
    name = input("Enter your name: ")
    with open('name.txt', 'w') as file:
        file.write(name)

def read_print_name():
    with open('name.txt', 'r') as file:
        name = file.read()
    print(f"Your name is {name}")

def sum_numbers():
    with open('numbers.txt', 'r') as file:
        numbers = file.readlines()
    numbers = [int(num) for num in numbers]
    print(f"The sum of the first two numbers is {sum(numbers[:2])}")

def total_numbers():
    with open('numbers.txt', 'r') as file:
        numbers = file.readlines()
    numbers = [int(num) for num in numbers]
    print(f"The total for all lines in numbers.txt is {sum(numbers)}")

read_write_name()
read_print_name()
sum_numbers()
total_numbers()