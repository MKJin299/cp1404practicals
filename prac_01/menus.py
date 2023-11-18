user_name = input("Enter name: ")

choice = input("(H)ello\n(G)oodbye\n(Q)uit\n>>> ").upper()

while choice != 'Q':
    if choice == 'H':
        print("Hello", user_name)
    elif choice == 'G':
        print("Goodbye", user_name)
    else:
        print("Invalid choice")
    choice = input("(H)ello\n(G)oodbye\n(Q)uit\n>>> ").upper()

print("Finished.")