import random
import string


def length_of_password():
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8): ").strip())
            if length >= 8:
                return length
            print("Error: Password length must be at least 8 characters.")
        except ValueError:
            print("Error: Please enter a valid whole number.")


def get_character_pool():
    while True:
        print("\nSelect character types to include (Choose at least 2):")

       
        pool = ""
        selected_types = 0
        guaranteed_chars = []

        choices = [
             (
                "Uppercase letters (A-Z)",
                string.ascii_uppercase,
                "Include uppercase letters? (y/n): ",
            ),
            (
                "Lowercase letters (a-z)",
                string.ascii_lowercase,
                "Include lowercase letters? (y/n): ",
            ),
            ("Numbers (0-9)", string.digits, "Include numbers? (y/n): "),
            ("Symbols (!@#$...)", string.punctuation, "Include symbols? (y/n): "),
        ]

        for name, chars, prompt in choices:
            if input(prompt).strip().lower() == "y":
                pool += chars
                selected_types += 1
              
                guaranteed_chars.append(random.choice(chars))

  
        if selected_types >= 2:
            return pool, guaranteed_chars

        print( f"\nError: You must select at least 2 character types. (You selected {selected_types})")
        print("Let's try again.\n")


def generate_password(length, pool, guaranteed_chars):
    remaining_length = length - len(guaranteed_chars)

    remaining_chars = [random.choice(pool) for _ in range(remaining_length)]

    password_list = guaranteed_chars + remaining_chars

    random.shuffle(password_list)

    return "".join(password_list)


def main():
    print("=== Welcome to the Random Password Generator ===")

    while True:
        length = length_of_password()

        pool, guaranteed_chars = get_character_pool()

        password = generate_password(length, pool, guaranteed_chars)
        print("\n" + "=" * 40)
        print(f"Your Generated Password: {password}")
        print("=" * 40 + "\n")

        another = input("Generate another password? (y/n): ").strip().lower()
        if another != "y":
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()