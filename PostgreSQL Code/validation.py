import re

# Function to check if email is in valid format


def is_valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+$', email) is not None

# Function to check if mobile phone number is in valid format


def is_valid_mobile_phone(phone):
    return re.match(r'^\d{11}$', phone) is not None

# Function to validate input string based on length and allowed characters


def validate_input_string(input_string, min_length=2, max_length=255):
    return min_length <= len(input_string) <= max_length and input_string.isprintable()
