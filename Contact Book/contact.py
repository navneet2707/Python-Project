FILE_NAME = "contacts.txt"

def add_contact():
    name = input("Enter name: ").rstrip()
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone},{email}\n")

    print("Contact added successfully!")

def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            print("\n--- Contact List ---")
            for line in file:
                name, phone, email = line.strip().split(",")
                print(f"Name: {name}, Phone: {phone}, Email: {email}")
    except FileNotFoundError:
        print("No contacts found.")

def search_contact():
    search_name = input("Enter name to search: ")
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",") 
                if name.lower() == search_name.lower():
                    print(f"Found -> Name: {name}, Phone: {phone}, Email: {email}")
                    found = True
                    break
        if not found:
            print("Contact not found.")
    except FileNotFoundError:
        print("No contacts file found.")

def delete_contact():
    name_to_delete = input("Enter name to delete: ")
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        with open(FILE_NAME, "w") as file:
            for line in lines:
                name, phone, email = line.strip().split(",")
                if name.lower() != name_to_delete.lower():
                    file.write(line)
                else:
                    found = True

        if found:
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")
    except FileNotFoundError:
        print("No contacts file found.")

def menu():
    print("\n=== Contact Book ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
