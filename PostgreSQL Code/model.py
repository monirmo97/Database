from peewee import PostgresqlDatabase, CharField, Model
import configparser

# Read database configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

db_name = config.get('database', 'name')
db_user = config.get('database', 'user')
db_password = config.get('database', 'password')
db_host = config.get('database', 'host')

# Create a PostgresqlDatabase instance with the collected details
db = PostgresqlDatabase(db_name, user=db_user,
                        password=db_password, host=db_host)


class PhonebookEntry(Model):
    firstname = CharField()
    lastname = CharField()
    phone = CharField()
    email = CharField()
    address = CharField()

    class Meta:
        database = db


# Connect to the database and create tables
db.connect()
db.create_tables([PhonebookEntry])
