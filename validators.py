import re


def username_validator(username):
    pattern = '^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$'
    if bool(re.fullmatch(pattern, username)):
        return True
    print('Invalid username. ')
    

def password_validator(password):
    pattern = '^(?=.*\d)(?=.*[A-Za-z0-9@#$%^&+=])(?=.*[A-Z])(?!.*(.)\1).{8}$'
    if bool(re.fullmatch(pattern, password)):
        return True
    print('Invalid password.')


def email_validator(email):
    pattern = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if bool(re.fullmatch(pattern, email)):
        return True
    print('Invalid email. ')


def city_validator(city):
    pattern = "^[a-z]+$"
    if bool(re.fullmatch(pattern, city)):
        return True
    print('Invalid city.')
    

def match_password(password, confirm_password):
    if confirm_password == password:
        return True
    print('Passwords does not match.')

