import os


def login_create_ierarchy():
    dirname = 'data'
    if os.path.exists(dirname):
        pass
    else:
        os.mkdir("data")

    file_login = 'data/login.txt'
    if os.path.exists(file_login):
        file = open(file_login, 'a')
    else:
        file = open(file_login, 'w')
    file.close()

    return file_login, dirname


def sign_up(file_login, dirname):
    print("**********Sign up***********")
    login = input("Create login: ")

    with open(file_login, 'r') as file:
        for line in file:
            if line.split(':')[0] == login:
                print('Login is used, try another....')
                return False

    password = input("Create password: ")
    directory = dirname + "/" + login

    file = open(file_login, 'a')
    file.write(login + ":" + password + '\n')
    file.close()

    os.mkdir(directory)
    info_file = directory + "/info.txt"
    file = open(info_file, 'w')
    file.close()

    print("*********Sign up complited**********")


def sign_in(file_login, dirname):
    print("*********Sign in**********")
    login = input("Login: ")
    password = input("Password: ")

    with open(file_login, 'r') as file:
        for line in file:
            ch_login = line.split(':')[0]
            ch_password = line.split(':')[1].split('\n')[0]

            if ch_login == login and ch_password == password:
                print("Welcome: ", login)
                working_directory = dirname + "/" + login
                return working_directory

    print("*****Wrong login/password, try again or sign up*****")
    return False


def login_page():
    file_login, dirname = login_create_ierarchy()
    option = input('Type 1 to sign in, type 2 to sign up:')
    working_directory = ""

    if (option == '1'):
        working_directory = sign_in(file_login, dirname)
        while not working_directory:
            working_directory = sign_in(file_login, dirname)
    elif (option == '2'):
        while sign_up(file_login, dirname) == False:
            pass
        login_page()

    file_info = working_directory + '/info.txt'

    return file_info, working_directory