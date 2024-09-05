def save_contact_func(contacts_book):
    with open ("contacts.csv", "wt") as file_pointer:
        for contact in contacts_book:
            line = f"{ contact['name'] },{ contact['phone'] },{contact['email']}\n"
            file_pointer.write(line)

    print("Saved contact successfully...")