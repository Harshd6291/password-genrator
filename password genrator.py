import random
import string


def generate_password(length=12, use_digits=True, use_symbols=True):
    # Basic character set
    characters = string.ascii_letters  # a-z, A-Z

    if use_digits:
        characters += string.digits  # 0-9
    if use_symbols:
        characters += string.punctuation  # !@#$%^&*() etc.

    if not characters:
        return "No character set selected!"

    # Randomly choose characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# --- User Input Section ---
print("=== Password Generator ===")
length = int(input("Enter password length: "))
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Generate and show password
password = generate_password(length, use_digits, use_symbols)
print("\nGenerated Password:", password)

