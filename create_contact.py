def create_contact_func(contacts_book):
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email, 
    }
    contacts_book.append(contact)

    print("\nContact Created Successfully...")
    return