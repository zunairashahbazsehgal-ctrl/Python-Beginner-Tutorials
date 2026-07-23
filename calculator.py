# Calculator App using Python Functions
# Features: Add, Subtract, Multiply, Divide + History

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b


history = []

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "6":
        print("Goodbye 👋")
        break

    elif choice == "5":
        print("\nHistory:")
        if len(history) == 0:
            print("No calculations yet.")
        else:
            for h in history:
                print(h)
        continue

    # Error handling for numbers
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except:
        print("Invalid input! Please enter numbers only.")
        continue

    if choice == "1":
        result = add(num1, num2)
        print(f"Result: {result}")
        history.append(f"{num1} + {num2} = {result}")

    elif choice == "2":
        result = subtract(num1, num2)
        print(f"Result: {result}")
        history.append(f"{num1} - {num2} = {result}")

    elif choice == "3":
        result = multiply(num1, num2)
        print(f"Result: {result}")
        history.append(f"{num1} * {num2} = {result}")

    elif choice == "4":
        result = divide(num1, num2)
        print(f"Result: {result}")
        history.append(f"{num1} / {num2} = {result}")

    else:
        print("Invalid choice!")