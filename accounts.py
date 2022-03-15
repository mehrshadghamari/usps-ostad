from users import users_list
from validators import (
    username_validator,
    password_validator,
    email_validator,
    city_validator,
    match_password,
) 


def login():
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username in users_list:
        if password in users_list[username]['password']:
            print('Welcome')
        else:
            print('Invalid password.')
    else:
        print('User does not exist.')


def register():
    while True:
        username = input('Enter your username: ')
        if not username_validator(username): continue
        
        password = input('Enter your password: ')
        if not password_validator(password): continue
        
        confirm_password = input('Confirm password: ')
        if not match_password(password, confirm_password): continue
        
        email = input('Enter your email: ')
        if not email_validator(email): continue

        city = input('Enter your City: ')
        if not city_validator(city): continue
        
        break
        
    users_list.update({username: {'password': password, 'city': city, 'email': email}})
