def update_contact_func(contacts_book):
    
    # Search --> Select --> Update
    search_item = input("Enter name of the contact to update: ")
    if not contacts_book:
        print("Item Not Found.")
    else:
        print("Item Found:")
        for index, contact in enumerate(contacts_book):
            if search_item.lower() == contact["name"].lower():

                print(f"{ index+1 }. { contact["name"] } - { contact["phone"] } - { contact["email"] }")

        selected_index = input("Which digit do you want to update? Ex:(1/2/3 etc.) ")
        selected_index = int(selected_index)

        update_name = input("Enter Update Name: ")
        update_phone = input("Enter Update Phone: ")
        update_email = input("Enter Update Email: ")

        contacts_book[selected_index-1].update(
            {
                "name": update_name,
                "phone": update_phone,
                "email": update_email,
            }
        )
        print("\nContact updated successfully...")