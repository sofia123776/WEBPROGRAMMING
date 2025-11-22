#PASSWAORD GENERATOR
import random
import string

def password_generator(length=12):
    print("This is to help you come up with a unique and hard to guess password by an unauthorized personnel")
    if length < 4:
        raise ValueError ("password length should not be less than 4")

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    password = [random.choice(uppercase),random.choice(lowercase),random.choice(digits),random.choice(special)]
    All_chars= uppercase + lowercase + digits + special
    password += random.choices(All_chars,k = length-4)
    random.shuffle(password)
    return ''.join(password)
length = int(input("Enter the length of the password"))
password = password_generator(length)
print("Generated password: ",password)



    