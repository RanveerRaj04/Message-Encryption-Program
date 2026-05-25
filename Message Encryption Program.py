#Message Encryption Program
import random
import string

chars= string.punctuation + string.digits + string.ascii_letters + " "
chars=list(chars)
key  =chars.copy()
random.shuffle(key)
# print(f"chars = {chars}")
# print(f"key   = {key}")

def encrypt(text):
    encrypted_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        encrypted_text += key[index]

    print(f"Original text - {plain_text}")
    print(f"Encrypted text- {encrypted_text}")
    return encrypted_text
    

def decrypt(text):
    plain_text = ""

    for letter in encrypted_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"Encrypted text- {encrypted_text}")
    print(f"Original text - {plain_text}")
    return plain_text


plain_text = str(input("Enter the message :"))
encrypt(plain_text)

choice= (input("Would you like to decrypt any message? (Y/N):")).upper()
if choice == "Y":
    encrypted_text= str(input("Enter the message :"))
    decrypt(encrypted_text)

