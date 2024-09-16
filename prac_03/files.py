# Question 1
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# Question 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# Question 3
with open("numbers.txt", "r") as in_file:
    num1 = int(in_file.readline())
    num2 = int(in_file.readline())
    result = num1 + num2
    print(result)  # Output: 59

# Question 4
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        total += int(line)
    print(f"The total of all numbers is: {total}")