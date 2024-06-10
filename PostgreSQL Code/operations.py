from model import PhonebookEntry


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
    entry = PhonebookEntry.create(
        firstname=firstname, lastname=lastname, phone=phone, email=email, address=address)
    return entry


def read_entry(entry_id):
    """
    Read an entry from the phonebook by ID.

    Parameters:
    - entry_id (int): ID of the entry to be read.

    Returns:
    - PhonebookEntry: The retrieved entry.
    """
    entry = PhonebookEntry.get_by_id(entry_id)
    return entry


def update_entry(entry_id, data):
    """
    Update an entry in the phonebook by ID with the provided data.

    Parameters:
    - entry_id (int): ID of the entry to be updated.
    - data (dict): Dictionary containing the fields to be updated.

    Returns:
    - None
    """
    entry = PhonebookEntry.get_by_id(entry_id)
    for key, value in data.items():
        setattr(entry, key, value)
    entry.save()


def delete_entry(entry_id):
    """
    Delete an entry from the phonebook by ID.

    Parameters:
    - entry_id (int): ID of the entry to be deleted.

    Returns:
    - None
    """
    entry = PhonebookEntry.get_by_id(entry_id)
    entry.delete_instance()


def search_entries(query):
    """
    Search for entries in the phonebook based on the provided query.

    Parameters:
    - query (str): Search query.

    Returns:
    - QuerySet: Set of entries matching the query.
    """
    entries = (PhonebookEntry
               .select()
               .where(
                   (PhonebookEntry.firstname.contains(query)) |
                   (PhonebookEntry.lastname.contains(query)) |
                   (PhonebookEntry.phone.contains(query)) |
                   (PhonebookEntry.email.contains(query)) |
                   (PhonebookEntry.address.contains(query))
               ))
    return entries
