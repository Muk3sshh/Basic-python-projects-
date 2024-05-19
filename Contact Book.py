contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts):
            print(f"{idx + 1}. {contact['name']} - {contact['phone']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    if not found_contacts:
        print("No contacts found.")
    else:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact():
    search_term = input("Enter name or phone number of the contact to update: ")
    found_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    if not found_contacts:
        print("No contacts found.")
    else:
        contact = found_contacts[0]
        print(f"Updating contact: {contact['name']} - {contact['phone']}")
        contact['name'] = input(f"Enter new name ({contact['name']}): ") or contact['name']
        contact['phone'] = input(f"Enter new phone number ({contact['phone']}): ") or contact['phone']
        contact['email'] = input(f"Enter new email ({contact['email']}): ") or contact['email']
        contact['address'] = input(f"Enter new address ({contact['address']}): ") or contact['address']
        print("Contact updated successfully.")

def delete_contact():
    search_term = input("Enter name or phone number of the contact to delete: ")
    found_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    if not found_contacts:
        print("No contacts found.")
    else:
        contact = found_contacts[0]
        contacts.remove(contact)
        print("Contact deleted successfully.")

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
