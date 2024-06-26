import json

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        try:
            with open('contact_book.json', 'r') as f:
                self.contacts = [Contact(**contact) for contact in json.load(f)]
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open('contact_book.json', 'w') as f:
            json.dump([vars(contact) for contact in self.contacts], f)

    def add_contact(self, name, phone_number, email, address):
        new_contact = Contact(name, phone_number, email, address)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully.")
        self.save_contacts()

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for i, contact in enumerate(self.contacts):
                print(f"{i+1}. Name: {contact.name}, Phone Number: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")

    def search_contact(self, search_term):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                if search_term in contact.name or search_term in contact.phone_number or search_term in contact.email or search_term in contact.address:
                    print(f"Name: {contact.name}, Phone Number: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
                    return
            print("Contact not found.")

    def update_contact(self, index, name=None, phone_number=None, email=None, address=None):
        if index < 1 or index > len(self.contacts):
            print("Invalid contact index.")
            return
        contact = self.contacts[index-1]
        if name:
            contact.name = name
        if phone_number:
            contact.phone_number = phone_number
        if email:
            contact.email = email
        if address:
            contact.address = address
        print(f"Contact updated successfully.")
        self.save_contacts()

    def delete_contact(self, index):
        if index < 1 or index > len(self.contacts):
            print("Invalid contact index.")
            return
        del self.contacts[index-1]
        print(f"Contact deleted successfully.")
        self.save_contacts()

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            search_term = input("Enter search term: ")
            contact_book.search_contact(search_term)
        elif choice == "4":
            index = int(input("Enter the index of the contact to update: "))
            name = input("Enter new name (leave blank to keep the same): ")
            phone_number = input("Enter new phone number (leave blank to keep the same): ")
            email = input("Enter new email (leave blank to keep the same): ")
            address = input("Enter new address (leave blank to keep the same): ")
            contact_book.update_contact(index, name if name else None, phone_number if phone_number else None, email if email else None, address if address else None)
        elif choice == "5":
            index = int(input("Enter the index of the contact to delete: "))
            contact_book.delete_contact(index)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()