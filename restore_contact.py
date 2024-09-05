from save_contact import save_contact_func
def restore_contact_func(contacts_book):
    contacts_book.clear()

    with open("contacts.csv", "r") as file_pointer:
        for line in file_pointer.readlines():
            line_splitted = line.strip().split(",")
            contact = {
                "name": line_splitted[0],
                "phone": line_splitted[1],
                "email": line_splitted[2],
            }
            contacts_book.append(contact)
    print("Contacts Restored.")
    save_contact_func(contacts_book)