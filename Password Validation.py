from getpass import getpass
from operator import contains
from string import punctuation
from tokenize import Number

def password_validator(password):
    print("The password has must have minimum 6 and maximum 30 characters, at least one special character and no space\nIf NOT respect this conditions, the password is not avaible!")
    print("----------------------------------------------------")
    print(f"Your password: {password}")
    print("----------------------------------------------------")
    lng = len(password)

    if ' ' in password:
        return "Is space in your password\n Invalid!"
    if lng < 6:
        print(f"Too short, it has {lng}, and must have al leats 6 characters!")
    if lng > 30:
        print(f"Too long, it has {lng}, and must have maximum 300 characters!")
    if punctuation not in password:
        print("Don't have a special character!")
    if str(numbers) not in password:
        print("Don't have at least a number!")  
    if lng <= 7:
        print("Your password is to week!")


numbers = ['1', '2', '3', '4', '5']

answ = input("You want to see your password? ")
if answ.lower() == 'no' or answ.lower() == 'n':
    password = getpass("Enter your password: ")
else:
    password = input("Enter your password: ")

print(password_validator(password))