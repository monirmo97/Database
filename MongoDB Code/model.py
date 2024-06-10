from mongoengine import Document, StringField, connect

connect('phonebook')

class PhonebookEntry(Document):
    firstname = StringField(required=True, max_length=255)
    lastname = StringField(required=True, max_length=255)
    phone = StringField(required=True, max_length=11)
    email = StringField(required=True, max_length=255)
    address = StringField(required=True, max_length=255)
