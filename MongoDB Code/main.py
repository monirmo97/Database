from operations import *
import argparse


def print_all():
    """
    Print all entries in the phonebook.
    """
    entries = search_entries("")
    for entry in entries:
        print(entry.id, entry.firstname, entry.lastname,
            entry.phone, entry.email, entry.address)


def main():
    """
    Main function for the Phonebook Management System.
    """
    parser = argparse.ArgumentParser(description="Phonebook Management System")

    # Define command-line arguments
    parser.add_argument('--add', action='store_true', help='Add new entry')
    parser.add_argument('--search', action='store_true', help='Search entry')
    parser.add_argument('--update', action='store_true', help='Update entry')
    parser.add_argument('--delete', action='store_true', help='Delete entry')
    parser.add_argument('--exit', action='store_true', help='Exit')

    args = parser.parse_args()

    while True:
        try:
            if args.add:
                # Add a new entry
                create_entry_from_input()

            elif args.search:
                # Search for entries
                query = input("Enter search query: ")
                entries = search_entries(query)
                for entry in entries:
                    print(entry.id, entry.firstname, entry.lastname,
                        entry.phone, entry.email, entry.address)

            elif args.update:
                # Update an entry
                print_all()
                update_entry_from_input()

            elif args.delete:
                # Delete an entry
                print_all()
                delete_entry_by_id()

            elif args.exit:
                # Exit the program
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

            user_input = input(
                "Do you want to perform another action? (yes/no): ").lower()
            if user_input == 'no':
                print("Exiting...")
                break

        except Exception as error_message:
            print(f"Error: {error_message}")


if __name__ == "__main__":
    main()
