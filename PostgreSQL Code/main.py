import psycopg2

def create_connection():
    try:
        # Replace the placeholders with your PostgreSQL connection details
        connection = psycopg2.connect(
            database="phonebook",
            user="hw4_q1",
            password="mo1841372",
            host="127.0.0.1",
            port="5432"
        )
        return connection
    except psycopg2.Error as e:
        print("Error: Unable to connect to the database.")
        print(e)
        return None

def add_entry(connection, name, last_name, phone_number, address):
    try:
        with connection.cursor() as cursor:
            # SQL query to insert a new entry into the phonebook table
            sql = "INSERT INTO phonebook (name, last_name, phone_number, address) VALUES (%s, %s, %s, %s);"
            cursor.execute(sql, (name, last_name, phone_number, address))
            connection.commit()
            print("Entry added successfully!")
    except psycopg2.Error as Error:
        print("Error: Unable to add entry.")
        print(Error)
        
def main():
    # Connect to the PostgreSQL database
    connection = create_connection()

    try:
        if connection:
            # Get user input for a new entry
            name = input("Enter name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter phone number: ")
            address = input("Enter address: ")

            # Add the entry to the phonebook
            add_entry(connection, name, last_name, phone_number, address)

    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("\nOperation canceled by the user.")

    finally:
        # Close the database connection in the finally block to ensure it's closed even in case of an exception
        if connection:
            connection.close()

if __name__ == "__main__":
    main()
