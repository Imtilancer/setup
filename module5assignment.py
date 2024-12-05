import csv

FILE_NAME = "contacts.csv"


def load_contacts():
    """Load contacts from the file."""
    try:
        with open(FILE_NAME, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []


def save_contact(contact):
    """Save a new contact to the file."""
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Email", "Phone", "Address"])
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(contact)


def check_phone_exists(phone):
    """Check if a phone number already exists."""
    contacts = load_contacts()
    return any(contact["Phone"] == phone for contact in contacts)


def delete_contact(phone):
    """Delete a contact by phone number."""
    contacts = load_contacts()
    new_contacts = [contact for contact in contacts if contact["Phone"] != phone]
    if len(new_contacts) == len(contacts):
        return False

    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Email", "Phone", "Address"])
        writer.writeheader()
        writer.writerows(new_contacts)
    return True


def search_contacts(query):
    """Search contacts by any detail."""
    contacts = load_contacts()
    return [contact for contact in contacts if query in contact.values()]


def validate_name(name):
    """Validate that the name is a string."""
    return isinstance(name, str) and name.isalpha()


def validate_phone(phone):
    """Validate that the phone number is an integer."""
    return phone.isdigit()


def add_contact():
    """Add a new contact."""
    print("\nAdd New Contact")
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone Number: ").strip()
    address = input("Address: ").strip()

    if not validate_name(name):
        print("Error: Name must be a string containing only letters.")
        return
    if not validate_phone(phone):
        print("Error: Phone number must be numeric.")
        return
    if check_phone_exists(phone):
        print("Error: Phone number already exists.")
        return

    contact = {"Name": name, "Email": email, "Phone": phone, "Address": address}
    save_contact(contact)
    print("Contact added successfully!")


def view_contacts():
    """Display all contacts."""
    print("\nAll Contacts:")
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return

    print(f"{'Name':<20}{'Email':<30}{'Phone':<15}{'Address':<30}")
    print("=" * 95)
    for contact in contacts:
        print(f"{contact['Name']:<20}{contact['Email']:<30}{contact['Phone']:<15}{contact['Address']:<30}")


def search_contact():
    """Search for a specific contact."""
    query = input("Enter Name, Email, or Phone to search: ").strip()
    results = search_contacts(query)
    if results:
        print(f"{'Name':<20}{'Email':<30}{'Phone':<15}{'Address':<30}")
        print("=" * 95)
        for contact in results:
            print(f"{contact['Name']:<20}{contact['Email']:<30}{contact['Phone']:<15}{contact['Address']:<30}")
    else:
        print("No matching contacts found.")


def delete_contact_by_user():
    """Prompt the user to delete a contact."""
    phone = input("Enter the Phone Number of the contact to delete: ").strip()
    if delete_contact(phone):
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def display_menu():
    """Display the main menu and handle user input."""
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contacts")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact_by_user()
        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print("Welcome to the CLI Contact Book!")
    display_menu()