import json

def load_contacts_from_file(filename):
    with open(filename, 'r') as file:
        contacts = json.load(file)
    return contacts

filename = "contactlist.txt"
contacts = load_contacts_from_file(filename)

def add_contact(contacts):
    _name = input('''Please enter the contact first and last name:
                  ''')
    _email = input('''Please enter the contact email:
                  ''')
    _number = input('''Please enter the contact number:
                  ''')
    newContact = {"name": _name,
                  "email": _email,
                  "phone": _number}
    contacts.append(newContact)
    print('You have successfully added a new contact to the system!')
    
def view_contacts(contacts):
    print('Contact List:')
    for contact in contacts:
        print(contact)
        
def update_contact(contacts):
    chooseContact = input('''Please enter the name of the contact you would like to update:
                          ''')
    updateEmail = input('''Please enter the updated contact email:
                         ''')
    updateNumber = input('''Please enter the updated contact number:
                         ''')
    for contact in contacts:
        if contact["name"] == chooseContact:
            contact["email"] = updateEmail
            contact["phone"] = updateNumber
    print('You have successfully updated a contact in the system!')
            
def remove_contact(contacts):
     chooseRemove = input('''Please enter the name of the contact you would like to delete:
                          ''')
     for contact in contacts:
         if contact["name"] == chooseRemove:
             contacts.remove(contact)
             print('You have successfully deleted a contact from the system!')
             
def save_contacts_to_file(contacts, filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)
        print('You have successfully saved your contact changes to the system!')

def exit_system():
    print('''Thank you for using our Contact Management System!
            Have a great day!''')

while True:
    menuOptions = int(input('''Welcome to the Contact Management System!
                            What would you like to do?
                            Enter 1 to view your contact list
                            Enter 2 to add a contact
                            Enter 3 to delete a contact
                            Enter 4 to update a contact
                            Enter 5 to save your changes and exit the system
                            '''))

    if menuOptions == 1:
        view_contacts(contacts)
    elif menuOptions == 2:
        add_contact(contacts)
    elif menuOptions == 3:
        remove_contact(contacts)
    elif menuOptions == 4:
        update_contact(contacts)
    elif menuOptions == 5:
        save_contacts_to_file(contacts, filename)
        exit_system()
        break
    else:
        print('''I'm sorry, but you have entered an invalid option.
            Please re-enter a valid option.''')

   