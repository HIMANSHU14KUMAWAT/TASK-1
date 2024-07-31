import string
import random
def generate_password(length=12):
    # Define the possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password includes at least one of each type of character
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)


# Generate and print a password
print(generate_password(12))