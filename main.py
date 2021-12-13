import login
import tests
import interviewee
import visual


option = input('***Type 1 if you - interviewee, type 2 if you - psychologist:')

file_login = 'data/login.txt'
dirname = 'data'


if option == '1':
    interviewee.open_test(file_login, dirname)
elif option == '2':
    tests.tests_form()
