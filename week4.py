import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(characters) for i in range(length))
    return result_str
def generate_passwords(num_passwords, length):
    passwords = []
    for i in range(num_passwords):
        password = generate_password(length)
        passwords.append(password)
    return passwords
if __name__ == "__main__":
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of the passwords: "))
    passwords = generate_passwords(num_passwords, password_length)
    for password in passwords:
        print("Random password: ", password)