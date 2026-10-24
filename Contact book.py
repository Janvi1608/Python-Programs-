Contacts={}
def add_contact():
    name =(input("Enter contact name "))
    phone_number = (input("Enter contact number : "))
    if len(phone_number)==10:
        Contacts[name]=phone_number
        print("Contact saved")
    else:
        print("Enter valid contact number")

def search_contact():
    name=input("Enter name:")
    if name in Contacts:
        for name , phone_number in Contacts.items() :
            print(f"Contact found \n {name} : {phone_number}")
    else:
        print("Contact does not exists")

def update_contact():
    name = input("enter contact name to update: ")
    if name in Contacts :
        new_phone_number=input("Enter new phone number: ")
        Contacts[name]=new_phone_number
        print("Contact updated successfully")
    else:
        print("Contact not found")

def display_contact():
    for name ,phone_number in Contacts.items() :
        print(f"Contact:\n{name} : {phone_number}")

while True:
    print(" \n  -~-~-~-~-CONTACT BOOK-~-~-~-~-   \n 1. Add contact \n 2. Search contact \n 3. Update contact \n 4. Display contacts")
    choice= input("Enter choice(1-4): ")
    if choice=="1":
        add_contact()
    elif choice=="2":
        search_contact()
    elif choice=="3":
        update_contact()
    elif choice=="4":
        display_contact()
        break
    else:
        print("Please select a choice(1-4)")
    
    