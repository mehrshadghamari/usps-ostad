from accounts import login, register


while True:
    user_command = input('Enter 0 for Login; Enter 1 for Register; Enter q for quit;(0/1/q):')
    if user_command == 'q':
        exit()
    
    if user_command == '0':
        login()
    elif user_command == '1':
        register()

# try except : --> handle user_command invalid input