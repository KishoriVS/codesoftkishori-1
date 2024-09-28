class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address


class ContactManager:
    def __init__(self):
        self.contacts = []


    def add_contact(self):
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        self.contacts.append(Contact(name, phone_number, email, address))
        print("Contact added successfully!")


    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("\nContact List:")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact.name} - {contact.phone_number}")
    def search_contact(self):
        query = input("Enter name or phone number to search: ")
        found = False
        for contact in self.contacts:
            if query in (contact.name, contact.phone_number):
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}")
                found = True
                break
        if not found:
            print("Contact not found.")
    def update_contact(self):
        self.view_contacts()
        index = int(input("Enter contact number to update: ")) - 1
        if index < 0 or index >= len(self.contacts):
            print("Invalid contact number.")
            return
        contact = self.contacts[index]
        contact.name = input(f"Enter new name ({contact.name}): ") or contact.name
        contact.phone_number = input(f"Enter new phone number ({contact.phone_number}): ") or contact.phone_number
        contact.email = input(f"Enter new email ({contact.email}): ") or contact.email
        contact.address = input(f"Enter new address ({contact.address}): ") or contact.address
        print("Contact updated successfully!")


    def delete_contact(self):
        self.view_contacts()
        index = int(input("Enter contact number to delete: ")) - 1
        if index < 0 or index >= len(self.contacts):
            print("Invalid contact number.")
            return
        del self.contacts[index]
        print("Contact deleted successfully!")


def main():
    manager = ContactManager()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            manager.add_contact()
        elif choice == "2":
            manager.view_contacts()
        elif choice == "3":
            manager.search_contact()
        elif choice == "4":
            manager.update_contact()
        elif choice == "5":
            manager.delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


        
       


