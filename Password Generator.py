import random
from string import punctuation

chars = '!#$%&()*+,-./:;<=>?@[\]^_`{|}~1234567890abcdefghijklmopqrstvwxyzABCDEFGHIJKLMOPQRSTVWXYZ'
chars2 = '~1234567890abcdefghijklmopqrstvwxyzABCDEFGHIJKLMOPQRSTVWXYZ'

def password_generator():
    print("--------------------------------------------------")
    lng_passwrd = int(input("How long do you want the password?: "))
    cou_password = int(input("How many password do you want?: "))
    special = str(input("You want to have a special characters?"))

    for x in range(0, cou_password):
        password = ""
        for i in range(0, lng_passwrd):
            password_char = random.choice(chars)
            password = password + password_char
        print(f"Your password:", password)
    

password_generator()