# Importing the required modules and classes
import argparse
from model import PhonebookEntry
from operations import *
from validation import *


def print_all():
    entries = search_entries("")
    for entry in entries:
        print(entry.id, entry.firstname, entry.lastname,
            entry.phone, entry.email, entry.address)


def main():
    # Setting up the argument parser
    parser = argparse.ArgumentParser(description="Phonebook Management System")

    # Adding arguments for each menu option
    parser.add_argument('--add', action='store_true', help='Add new entry')
    parser.add_argument('--search', action='store_true', help='Search entry')
    parser.add_argument('--update', action='store_true', help='Update entry')
    parser.add_argument('--delete', action='store_true', help='Delete entry')
    parser.add_argument('--exit', action='store_true', help='Exit')

    # Parsing the command-line arguments
    args = parser.parse_args()

    # Main loop for the phonebook management system
    while True:
        try:
            # Handling user choices based on parsed arguments
            if args.add:
                firstname = input("Enter first name: ")
                while not validate_input_string(firstname):
                    print(
                        "Invalid input! First name must be between 2 and 255 printable characters.")
                    firstname = input("Enter first name: ")

                lastname = input("Enter last name: ")
                while not validate_input_string(lastname):
                    print(
                        "Invalid input! Last name must be between 2 and 255 printable characters.")
                    lastname = input("Enter last name: ")

                phone = input("Enter phone number: ")
                while not is_valid_mobile_phone(phone):
                    print(
                        "Invalid phone number format! Please enter a 11-digit number.")
                    phone = input("Enter phone number: ")

                email = input("Enter email address: ")
                while not is_valid_email(email):
                    print("Invalid email format! Please enter a valid email address.")
                    email = input("Enter email address: ")

                address = input("Enter address: ")
                while not validate_input_string(address):
                    print(
                        "Invalid input! Address must be between 2 and 255 printable characters.")
                    address = input("Enter address: ")

                create_entry(firstname, lastname, phone, email, address)
                print("Entry added successfully!")

            elif args.search:
                query = input("Enter search query: ")
                entries = search_entries(query)
                for entry in entries:
                    print(entry.firstname, entry.lastname,
                        entry.phone, entry.email, entry.address)

            elif args.update:
                print_all()
                firstname = input("Enter first name: ")
                while not validate_input_string(firstname):
                    print(
                        "Invalid input! First name must be between 2 and 255 printable characters.")
                    firstname = input("Enter first name: ")

                lastname = input("Enter last name: ")
                while not validate_input_string(lastname):
                    print(
                        "Invalid input! Last name must be between 2 and 255 printable characters.")
                    lastname = input("Enter last name: ")

                phone = input("Enter phone number: ")
                while not is_valid_mobile_phone(phone):
                    print(
                        "Invalid phone number format! Please enter a 11-digit number.")
                    phone = input("Enter phone number: ")

                email = input("Enter email address: ")
                while not is_valid_email(email):
                    print("Invalid email format! Please enter a valid email address.")
                    email = input("Enter email address: ")

                address = input("Enter address: ")
                while not validate_input_string(address):
                    print(
                        "Invalid input! Address must be between 2 and 255 printable characters.")
                    address = input("Enter address: ")
                entry_id = int(input("Enter entry ID to update: "))
                data = {}
                data['firstname'] = firstname
                data['lastname'] = lastname
                data['phone'] = phone
                data['email'] = email
                data['address'] = address
                update_entry(entry_id, data)
                print("Entry updated successfully!")

            elif args.delete:
                print_all()
                entry_id = int(input("Enter entry ID to delete: "))
                delete_entry(entry_id)
                print("Entry deleted successfully!")

            elif args.exit:
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

            # Asking the user if they want to continue or exit
            user_input = input(
                "Do you want to perform another action? (yes/no): ").lower()
            if user_input == 'no':
                print("Exiting...")
                break

        except Exception as error_message:
            print(f"Error: {error_message}")


if __name__ == "__main__":
    main()
