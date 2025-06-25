import random
import string

def get_password_length():
    """Gets a valid password length from the user."""
    while True:
        try:
            length = int(input("Enter the desired password length (must be a positive integer): "))
            if length > 0:
                return length
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_character_type_choice(prompt):
    """Gets a valid choice (yes/no) from the user for a character type."""
    while True:
        choice = input(prompt).lower()
        if choice in ['y', 'n', 'yes', 'no']:
            return choice.startswith('y')
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def generate_password():
    """Generates a password based on user-defined criteria."""
    print("--- Password Generator ---")

    length = get_password_length()

    use_uppercase = get_character_type_choice("Include uppercase letters? (y/n): ")
    use_lowercase = get_character_type_choice("Include lowercase letters? (y/n): ")
    use_numbers = get_character_type_choice("Include numbers? (y/n): ")
    use_special = get_character_type_choice("Include special characters? (y/n): ")

    char_pool = ''
    guaranteed_chars = []

    if use_uppercase:
        char_pool += string.ascii_uppercase
        guaranteed_chars.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        char_pool += string.ascii_lowercase
        guaranteed_chars.append(random.choice(string.ascii_lowercase))
    if use_numbers:
        char_pool += string.digits
        guaranteed_chars.append(random.choice(string.digits))
    if use_special:
        char_pool += string.punctuation
        guaranteed_chars.append(random.choice(string.punctuation))

    if not char_pool:
        print("\nError: You must select at least one character type.")
        return

    if length < len(guaranteed_chars):
        print(f"\nError: Password length must be at least {len(guaranteed_chars)} to include all selected character types.")
        return

    remaining_length = length - len(guaranteed_chars)
    
    password_list = guaranteed_chars + [random.choice(char_pool) for _ in range(remaining_length)]

    random.shuffle(password_list)
    password = "".join(password_list)

    print(f"\nYour generated password is: {password}")

if __name__ == "__main__":
    generate_password() 