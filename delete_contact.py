from save_contact import save_contact_func

def delete_contact_func(contacts_book):
    # search --> select --> delete
    search_item = input("Enter name of the contact to delete: ")
    if not contacts_book:
        print("Item Not Found")
    else:
        print("Item Found.")
        for index, contact in enumerate(contacts_book):
            if search_item.lower() in contact["name"].lower():
                print(f"{ index+1 }. { contact["name"] } - { contact["phone"] } - { contact["email"] }")
        selected_index = input("Which digit do you want to delete? Ex:(1/2/3 etc.) ")
        selected_index = int(selected_index)

        confirm = input("Do you want to delete this contact? (yes/no): ")
        
        if confirm.lower() == 'yes':
            contacts_book.pop(selected_index-1)
            print(f"Contact '{contact['name']}' Deleted Successfully...")
            print("And")
            save_contact_func(contacts_book)
            return
        else:
            print("Contact Delete Cancelled.")
            return