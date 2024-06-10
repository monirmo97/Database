This is a Python program that allows you to manage a phonebook database using MongoDB. You can add, search, update, and delete entries in the phonebook. You can also exit the program at any time.

## Installation

To run this program, you need to have Python 3 installed on your system.


You can install requirements.txt with pip command:

pip install -r requirements.txt


You also need to have MongoDB installed and configured on your system.

Usage
To run the program, navigate to the directory where the program is located and execute the following command:

python main.py

The program will display a menu with the following options:

•  --add: Add new entry

•  --search: Search entry

•  --update: Update entry

•  --delete: Delete entry

•  --exit: Exit

You can choose an option by typing the corresponding argument, such as --add or --search, and pressing enter.

Depending on the option you choose, the program will prompt you to enter some information, such as the first name, last name, phone number, email address, or address of the entry you want to add, search, update, or delete.

The program will perform the requested operation and display the result or an error message if something goes wrong.

You can perform multiple operations by choosing different options from the menu.

To exit the program, type --exit and press enter.

Examples
Here are some examples of how to use the program with different options:

•  To add a new entry to the phonebook, type --add and press enter. Then, enter the first name, last name, phone number, email address, and address of the entry you want to add. The program will add the entry to the phonebook and print a success message.

--add
Enter first name: Alice
Enter last name: Smith
Enter phone number: 1234567890
Enter email address: alice@example.com
Enter address: 123 Main Street
Entry added successfully!


