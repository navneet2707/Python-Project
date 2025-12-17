import random
import string

# Take password length
length = int(input("Enter password length: "))

# Take password strength
print("Choose password strength:")
print("1. Weak")
print("2. Medium")
print("3. Strong")

strength = input("Enter choice (1, 2 or 3): ")

# Select characters based on strength
if strength == '1':
    chars = string.ascii_uppercase + string.digits
elif strength == '2':
    chars = string.ascii_letters + string.digits + string.punctuation
elif strength == '3':
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
else:
    print("Invalid choice")
    exit()

# Generate password
password = ""
for i in range(length):
    password += random.choice(chars)

# Display password
print("Generated password:", password)
