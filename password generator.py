import random
import string

def generate_password(length, use_special_chars):
    # Define the character set based on user preference
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

    # Randomly select characters from the character set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Prompt the user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired length for your password: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    # Ask if the user wants special characters
    use_special_chars = input("Include special characters (y/n)? ").strip().lower() == 'y'

    # Generate the password
    password = generate_password(length, use_special_chars)
    
    # Display the generated password
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
