import random
import string

print("=====PASSWORD GENETATOR=====")
length = int(input("Enter Password Lenght:"))

characters = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password = ", password)