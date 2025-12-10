#  Simple address book using dictionary.
address_book = {}

print("Simple Address Book Program")

while True:
    print("\nMenu:")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    # 1. Add a contact
    if choice == '1':
        name = input("Enter name: ")
        if name in address_book:
            print(f"Error: Contact '{name}' already exists.")
        else:
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address_book[name] = {'phone': phone, 'email': email}
            print(f"Contact '{name}' added.")
    
    # 2. View all contacts
    elif choice == '2':
        if not address_book:
            print("Address book is empty.")
        else:
            print("\n--- Current Contacts ---")
            for name, details in address_book.items():
                print(f"Name: {name}")
                print(f"  Phone: {details['phone']}")
                print(f"  Email: {details['email']}")
                print("-" * 20)
    
    # 3. Search for a contact
    elif choice == '3':
        name = input("Enter name to search: ")
        if name in address_book:
            details = address_book[name]
            print(f"\nContact Found:")
            print(f"  Name: {name}")
            print(f"  Phone: {details['phone']}")
            print(f"  Email: {details['email']}")
        else:
            print(f"Contact '{name}' not found.")

    # 4. Delete a contact
    elif choice == '4':
        name = input("Enter name to delete: ")
        try:
            del address_book[name]
            print(f"Contact '{name}' deleted.")
        except KeyError:
            print(f"Error: Contact '{name}' not found.")
            
    # 5. Exit
    elif choice == '5':
        print("Exiting address book program.")
        break
    
    # Invalid choice
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")



