from model import PhonebookEntry
from validation import *


def create_entry(firstname, lastname, phone, email, address):
    """
    Create a new entry in the phonebook.

    Parameters:
    - firstname (str): First name of the entry.
    - lastname (str): Last name of the entry.
    - phone (str): Phone number of the entry.
    - email (str): Email address of the entry.
    - address (str): Address of the entry.

    Returns:
    - PhonebookEntry: The created entry.
    """
    entry = PhonebookEntry(
        firstname=firstname, lastname=lastname, phone=phone, email=email, address=address)
    entry.save()
    return entry


def read_entry(entry_id):
    """
    Read an entry from the phonebook by ID.

    Parameters:
    - entry_id (str): ID of the entry to be read.

    Returns:
    - PhonebookEntry or None: The retrieved entry or None if not found.
    """
    try:
        entry = PhonebookEntry.objects.get(id=entry_id)
        return entry
    except PhonebookEntry.DoesNotExist:
        return None


def update_entry(entry_id, data):
    """
    Update an entry in the phonebook by ID with the provided data.

    Parameters:
    - entry_id (str): ID of the entry to be updated.
    - data (dict): Dictionary containing the fields to be updated.

    Returns:
    - PhonebookEntry or None: The updated entry or None if not found.
    """
    entry = read_entry(entry_id)
    if entry:
        for key, value in data.items():
            setattr(entry, key, value)
        entry.save()
        return entry
    return None


def delete_entry(entry_id):
    """
    Delete an entry from the phonebook by ID.

    Parameters:
    - entry_id (str): ID of the entry to be deleted.

    Returns:
    - bool: True if the entry is deleted, False otherwise.
    """
    entry = read_entry(entry_id)
    if entry:
        entry.delete()
        return True
    return False


def search_entries(query):
    """
    Search for entries in the phonebook based on the provided query.

    Parameters:
    - query (str): Search query.

    Returns:
    - QuerySet: Set of entries matching the query.
    """
    entries = PhonebookEntry.objects.filter(
        __raw__={'$or': [
            {'firstname': {'$regex': query, '$options': 'i'}},
            {'lastname': {'$regex': query, '$options': 'i'}},
            {'phone': {'$regex': query, '$options': 'i'}},
            {'email': {'$regex': query, '$options': 'i'}},
            {'address': {'$regex': query, '$options': 'i'}}
        ]}
    )
    return entries


def create_entry_from_input():
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


def update_entry_from_input():
    entry_id = input("Enter entry ID to update: ")

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

    entry = read_entry(entry_id)
    if entry:
        data = {
            'firstname': firstname,
            'lastname': lastname,
            'phone': phone,
            'email': email,
            'address': address
        }
        update_entry(entry_id, data)
        print("Entry updated successfully!")
    else:
        print("Entry not found.")


def delete_entry_by_id():
    entry_id = input("Enter entry ID to delete: ")
    entry = read_entry(entry_id)
    if entry:
        delete_entry(entry_id)
        print("Entry deleted successfully!")
    else:
        print("Entry not found.")
