# Easy To-Do List App

tasks = ""

while True:
    print()
    print("----- TO-DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Save Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter your task: ")
        tasks = tasks + "- " + task + "\n"
        print("Task Added!")

    # View Tasks
    elif choice == "2":
        if tasks == "":
            print("No Tasks Found.")
        else:
            print()
            print("Your Tasks:")
            print(tasks)

    # Save Tasks
    elif choice == "3":
        file = open("tasks.txt", "w")
        file.write(tasks)
        file.close()
        print("Tasks Saved in tasks.txt")

    # Exit
    elif choice == "4":
        print("Goodbye!")
        break

    # Invalid Choice
    else:
        print("Invalid Choice!")