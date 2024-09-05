def search_contacts_func(contacts_book):
    search_item = input("Enter name to search: ")
    if not contacts_book:
        print("Contact Not Found.")
    else:
        print("Contact Found:")
        for index, contact in enumerate(contacts_book):
            if search_item.lower() in contact["name"].lower():
                print(f"{ index +1 }. { contact["name"] } - { contact["phone"] } - { contact["email"] }")
    