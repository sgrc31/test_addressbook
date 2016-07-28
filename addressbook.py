#!/usr/bin/env python3

import csv

contact_list = {}

class Contact:
    def __init__(self, first, last, mail):
        self.first = first
        self.last = last
        self.mail = mail
        contact_list[self.first] = self
        print('Contact created and added\n')

    def show_contact(self):
        print('    Name: {}'.format(self.first))
        print('    Surname: {}'.format(self.last))
        print('    Email: {}'.format(self.mail))

    def delete_contact(self):
        del contact_list[self.first]
        self = None

    def edit_contact(self, first=None, last=None, mail=None):
        self.first = first or self.first
        self.last = last or self.last
        self.mail = mail or self.mail
        print('Contact updated\n')

    @staticmethod
    def show_all():
        print('Listing all contacts')
        for x, y in contact_list.items():
            print('Contact {}'.format(x))
            print(y.show_contact())
        else:
            print('For a total of {} contacts'.format(len(contact_list.items())))

    @staticmethod
    def write_to_file():
        with open('data.csv', 'w') as file:
            output_writer = csv.writer(file)
            for x, y in contact_list.items():
                output_writer.writerow([y.first, y.last, y.mail])
        print('Contacts saved to disk\n')


if __name__ == '__main__':
    print('Addressbook v0.1')
    while True:
        print('Select an option\n'
              '1 > Show all contacts\n'
              '2 > Add a contact\n'
              '3 > Delete a contact\n'
              '4 > Edit a contact\n'
              '5 > Save on disk'
              )
        user_choice = input()
        if user_choice is '1':
            if len(contact_list.items()) > 0:
                Contact.show_all()
            else:
                print('You have no contacts\n')
        elif user_choice is '2':
            name = input('Type contact first name\n')
            last = input('Type contact last name\n')
            mail = input('Type contact mail\n')
            Contact(name, last, mail)
        elif user_choice is '3':
            if len(contact_list.items()) > 0:
                to_delete = input('Contact to delete\n')
                try:
                    contact_list[to_delete].delete_contact()
                except KeyError:
                    print('No such contact, try again\n')
            else:
                print('No contacts avaible for deletion yet\n')
        elif user_choice is '4':
            if len(contact_list.items()) > 0:
                to_edit = input('Contact to edit\n')
                try:
                    contact_list[to_edit]
                    name = input('Type contact first name\n')
                    last = input('Type contact last name\n')
                    mail = input('Type contact mail\n')
                    contact_list[to_edit].edit_contact(name, last, mail)
                    contact_list[name] = contact_list.pop(to_edit)
                except KeyError:
                    print('No such contact, try again\n')
            else:
                print('No contacts to edit\n')
        elif user_choice is '5':
            Contact.write_to_file()
        else:
            print('Invalid option, try again\n')  
