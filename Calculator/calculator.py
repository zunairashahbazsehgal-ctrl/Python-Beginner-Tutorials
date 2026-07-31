# Simple Calculator

while True:
    print()
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "5":
        print("Goodbye!")
        break

    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Please enter numbers only")
        continue

    if choice == "1":
        print("Result:", num1 + num2)

    elif choice == "2":
        print("Result:", num1 - num2)

    elif choice == "3":
        print("Result:", num1 * num2)

    elif choice == "4":
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)

    else:
        print("Invalid choice!")