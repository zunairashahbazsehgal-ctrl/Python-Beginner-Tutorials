# Easy To-Do List App

tasks = []

while True:
    print("\n----- TO-DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Save Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task Added!")

    # View Tasks
    elif choice == "2":
        if tasks == []:
            print("No Tasks Found.")
        else:
            print("\nYour Tasks:")
            for task in tasks:
                print("-", task)

    # Save Tasks
    elif choice == "3":
        file = open("tasks.txt", "w")

        for task in tasks:
            file.write(task + "\n")

        file.close()
        print("Tasks Saved in tasks.txt")

    # Exit
    elif choice == "4":
        print("Goodbye!")
        break

    # Invalid Choice
    else:
        print("Invalid Choice!")









    