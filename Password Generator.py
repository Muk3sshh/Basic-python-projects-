import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator")
    print("==================")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Password length should be at least 1.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        password = generate_password(length)
        print(f"Generated Password: {password}")
        another = input("Do you want to generate another password? (yes/no): ").lower()
        if another != 'yes':
            break

    print("Thank you for using the password generator. Goodbye!")

if __name__ == "__main__":
    main()
