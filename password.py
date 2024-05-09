import random
import string

def generate_password(length=12):
    """
    Generate a random password with the specified length.
    """
    # Define the characters to use for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the defined characters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password (default is 12): "))
    
    if length <= 0:
        print("Invalid length. Defaulting to 12 characters.")
        length = 12
    
    password = generate_password(length)
    print("Your random password is:", password)

if __name__ == "__main__":
    main()