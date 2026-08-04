# Contact Book

FILE_NAME = "contacts.txt"


def add_contact():
    print("\n--- Add Contact ---")

    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone},{email}\n")

    print("Contact added successfully!")


def view_contacts():
    print("\n--- All Contacts ---")

    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

            if len(contacts) == 0:
                print("No contacts found.")
                return

            for contact in contacts:
                name, phone, email = contact.strip().split(",")

                print(f"Name : {name}")
                print(f"Phone: {phone}")
                print(f"Email: {email}")
                print("-" * 25)

    except FileNotFoundError:
        print("No contacts found.")


def search_contact():
    print("\n--- Search Contact ---")

    search_name = input("Enter Name: ")

    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for contact in file:
                name, phone, email = contact.strip().split(",")

                if name.lower() == search_name.lower():
                    print("\nContact Found!")
                    print(f"Name : {name}")
                    print(f"Phone: {phone}")
                    print(f"Email: {email}")
                    found = True
                    break

        if not found:
            print("Contact not found.")

    except FileNotFoundError:
        print("No contacts found.")


def delete_contact():
    print("\n---- Delete Contact ----")

    delete_name = input("Enter Name to Delete: ")

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:

        skip = False

        for line in lines:

            if line.strip() == "Name: " + delete_name:
                skip = True
                continue

            if skip:
                if line.strip() == "--------------------":
                    skip = False
                continue

            file.write(line)

    print("Delete process completed.")

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice. Please try again.")