import random
import string

def generate_password(length, uppercase, special_characters):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if special_characters:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")
    length = int(input("Enter the length of the password: "))
    uppercase = input("Include uppercase characters? (yes/no): ").lower() == 'yes'
    special_characters = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, uppercase, special_characters)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
