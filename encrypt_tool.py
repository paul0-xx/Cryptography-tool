from cryptography.fernet import Fernet

# Create a new secret key and save it to a file
key = Fernet.generate_key()
with open("mykey.key", "wb") as f:
    f.write(key)

# Load the key from the file
with open("mykey.key", "rb") as f:
    key = f.read()

fernet = Fernet(key)

# Ask user for a message
message = input("Enter your message: ")

# Encrypt the message
encrypted = fernet.encrypt(message.encode())
print("Encrypted message:", encrypted)

# Decrypt the message
decrypted = fernet.decrypt(encrypted).decode()
print("Decrypted message:", decrypted)
