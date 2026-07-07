print("========== SIMPLE CALCULATOR ==========")

while True:

    # Take input from the user
    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Choose an operation
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")

    choice = input("Enter your choice (1-5): ")

    # Perform the calculation
    if choice == "1":
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")

    elif choice == "2":
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")

    elif choice == "3":
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")

    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
        else:
            print("\nError: Division by zero is not allowed.")

    elif choice == "5":
        if num2 != 0:
            result = num1 % num2
            print(f"\nResult: {num1} % {num2} = {result}")
        else:
            print("\nError: Division by zero is not allowed.")

    else:
        print("\nInvalid choice! Please select a valid operation.")

    # Continue Menu
    print("\n========== MENU ==========")
    print("1. Perform Another Calculation")
    print("2. Exit")

    option = input("Enter your choice (1-2): ")

    if option == "2":
        print("\nThank you for using the Simple Calculator!")
        break