import random
import string

while True:
    print("\n========== PASSWORD GENERATOR ==========")

    # Password Length
    while True:
        try:
            length = int(input("Enter password length: "))
            if length > 0:
                break
            else:
                print("Password length must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    # Password Type
    print("\nSelect Password Type")
    print("1. Lowercase Letters")
    print("2. Uppercase Letters")
    print("3. Letters Only")
    print("4. Letters + Numbers")
    print("5. Letters + Numbers + Symbols")
    print("6. Numbers Only")
    print("7. Symbols Only")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        characters = string.ascii_lowercase
    elif choice == "2":
        characters = string.ascii_uppercase
    elif choice == "3":
        characters = string.ascii_letters
    elif choice == "4":
        characters = string.ascii_letters + string.digits
    elif choice == "5":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif choice == "6":
        characters = string.digits
    elif choice == "7":
        characters = string.punctuation
    else:
        print("Invalid choice! Using all characters.")
        characters = string.ascii_letters + string.digits + string.punctuation

    # Generate passwords with the selected settings
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))

        print("\nGenerated Password:")
        print(password)

        print("\n========== MENU ==========")
        print("1. Generate Another Password (Same Length & Type)")
        print("2. Generate New Password (Change Length & Type)")
        print("3. Exit")

        option = input("Enter your choice (1-3): ")

        if option == "1":
            # Generate another password with the same settings
            continue

        elif option == "2":
            # Return to the main menu
            break

        elif option == "3":
            print("\nThank you for using the Password Generator!")
            exit()

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")