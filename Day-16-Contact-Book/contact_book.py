
import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


contacts = load_contacts()


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if not name or not phone:
        print("Name and phone are required!")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts()
    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found!")
        return

    print("\n====== CONTACT LIST ======")

    for index, contact in enumerate(contacts, start=1):
        print(f"\n{index}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")


def search_contact():
    search_name = input("Enter name to search: ").strip().lower()

    found = False

    for contact in contacts:
        if search_name in contact["name"].lower():
            print("\nContact Found!")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if not found:
        print("Contact not found!")


def update_contact():
    view_contacts()

    if not contacts:
        return

    try:
        number = int(input("\nEnter contact number to update: "))

        if 1 <= number <= len(contacts):
            contact = contacts[number - 1]

            new_name = input("New name (Enter to keep old): ").strip()
            new_phone = input("New phone (Enter to keep old): ").strip()
            new_email = input("New email (Enter to keep old): ").strip()

            if new_name:
                contact["name"] = new_name
            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email

            save_contacts()
            print("Contact updated successfully!")
        else:
            print("Invalid contact number!")

    except ValueError:
        print("Please enter a valid number!")


def delete_contact():
    view_contacts()

    if not contacts:
        return

    try:
        number = int(input("\nEnter contact number to delete: "))

        if 1 <= number <= len(contacts):
            removed = contacts.pop(number - 1)
            save_contacts()
            print(f"{removed['name']} deleted successfully!")
        else:
            print("Invalid contact number!")

    except ValueError:
        print("Please enter a valid number!")


while True:
    print("\n====== CONTACT BOOK ======")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid choice!")
