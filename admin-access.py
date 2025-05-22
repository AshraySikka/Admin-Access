import hashlib
import getpass

AUTHORIZED_USERS = ['ashray', 'sikka']
STORED_PASSWORD_HASH = '0192023a7bbd73250516f069df18b500'

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def is_authorized_user(username):
    return username.lower() in AUTHORIZED_USERS

def check_credentials():
    attempts = 3
    while attempts > 0:
        username = input("Enter your username: ").strip()
        password = getpass.getpass("Enter your password: ")

        if is_authorized_user(username) and hash_password(password) == STORED_PASSWORD_HASH:
            print(f"✅ Access granted. Welcome, {username}!")
            return
        else:
            attempts -= 1
            print(f"❌ Access denied. Attempts left: {attempts}\n")

    print("🚫 Too many failed attempts. Exiting...")

if __name__ == "__main__":
    check_credentials()

