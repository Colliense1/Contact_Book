def view_all_contacts_func(contacts_book):
    if not contacts_book:
        print("Contacts Not Found" )
    else:
        print("Contacts Found: ")
        for index, contact in enumerate(contacts_book):
            print(f"{index+1}. { contact["name"] } - { contact["phone"] } - { contact["email"] }"
              
              #sep=" | ",
            )

