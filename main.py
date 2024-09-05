import create_contact, view_all_contacts, search_contact, update_contact, delete_contact, save_contact, restore_contact

contacts_book = []

print("\nWelcome To Contact Book...!")

menu_item = """
Your Options: 
1. Add Contact
2. View All Contacts
3. Search Contacts
4. Update Contact
5. Delete Contact
6. Save Contact
7. Restore Contact
8. Exit

"""
while True:
    print(menu_item)
    choice = input("Enter Your Choice: ")

    if choice == "1":
       create_contact.create_contact_func(contacts_book)
    elif choice == "2":
       view_all_contacts.view_all_contacts_func(contacts_book)
    elif choice == "3":
       search_contact.search_contacts_func(contacts_book)
    elif choice == "4":
       update_contact.update_contact_func(contacts_book)
    elif choice == "5":
       delete_contact.delete_contact_func(contacts_book)
    elif choice == "6":
       save_contact.save_contact_func(contacts_book)
    elif choice == "7":
       restore_contact.restore_contact_func(contacts_book)
    elif choice == "8":
       break
    else:
      print("Invalid choice. Please try again.")
    
print("Exit the program. Thank you!")

