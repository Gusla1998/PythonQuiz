import login
import os
import visual
import create_table



def show_your_test(file_info):
    print('*********Your test************')
    with open(file_info, 'r') as file:
        for test in file:
            print(test)


def create_test(file_info, working_directory):
    print('****Create new questionnaire - questions  with 4 answers***')

    answer_count = 4
    another_question = ""
    status = "work-in-progress"

    name = input('*Create name of questionnaire:')
    anon = input('*Type 1 to anon,type 0 with name:')
    question_count = int(input('*Type question count:'))

    test_directory = working_directory + '/' + name
    os.mkdir(test_directory)
    file_test = test_directory + '/test.txt'
    with open(file_test, 'w') as file:
        for i in range(0, question_count, 1):
            question = input('Create question:')
            another_question += question + ' :'
            for j in range(0, answer_count, 1):
                answer = input('Create answer:')
                another_question += ' ' + answer
            file.write(another_question + '\n')
            another_question = ''

    print('****Creation complited*****')

    open(file_info, 'a').write(name + ' ' + status + ' is_anonymous: ' + anon)


def return_test_by_name(file_info, working_directory):
    print('****Choose test, you want to change***')

    name = input('Name of questionnaire(with work-in-progress status):')
    test_name = ''
    test_status = ''

    with open(file_info, 'r') as file:
        for line in file:
            test_name = line.split(' ')[0]
            test_status = line.split(' ')[1]

            if test_name == name and test_status == 'work-in-progress':
                test_directory = working_directory + '/' + test_name
                file.close()
                return test_directory

    file.close()
    return False


def read_test(test_file):
    i = 1
    test = {}
    with open(test_file, 'r') as file:
        for line in file:
            print(str(i) + ")" + line.split(' : ')[0])
            test[i] = line
            i += 1
    return test


def change_test(file_info, working_directory):
    answer_count = 4
    another_question = ''

    test_directory = return_test_by_name(file_info, working_directory)

    while test_directory == False:
        print('Wrong test name(or status), try again...')
        test_directory = return_test_by_name(file_info, working_directory)

    test_file = test_directory + "/test.txt"

    test = read_test(test_file)
    quest_number = input('Type number of questions you want to change, with comma:').split(',')

    with open(test_file, 'w') as file:
        for i in range(1, len(test) + 1, 1):
            flag = False
            for num in quest_number:
                if int(num) == i:
                    flag = True
                    break
            if flag:
                print('Change question number ' + str(i))
                question = input('Create question:')
                another_question += question + ' :'
                for j in range(0, answer_count, 1):
                    answer = input('Create answer:')
                    another_question += ' ' + answer
                file.write(another_question + '\n')
                another_question = ''
                flag = False
            else:
                file.writelines(test[i])

    print('****Changing completed*****')


def change_test_status(file_info):
    print('****Choose test, which status you want to change by next schema***')
    print('**** 1)work-in-progress --> 2)active --> 3)closed ***')

    name = input('Name of questionnaire: ')
    test_name = ''
    test_status = ''
    list_test = []
    i = 0

    flag = False
    with open(file_info, 'r') as file:
        for line in file:
            test_name = line.split(' ')[0]
            list_test.append(line)
            if test_name == name:
                test_status = line.split(' ')[1]
                flag = True
            i += 1
    file.close()

    if not flag:
        print('Wrong test name, try again...')
        return False
    else:
        if test_status == 'work-in-progress':
            with open(file_info, 'w') as file:
                for line in list_test:
                    test_name = line.split(' ')[0]
                    if test_name == name:
                        file.write(test_name + ' ' + 'active' + ' ' + line.split(' ')[2] + ' ' + line.split(' ')[3])
                    else:
                        file.write(line)
            file.close()
            print('Now ' + name + ' is active.')
        elif test_status == 'active':
            with open(file_info, 'w') as file:
                for line in list_test:
                    test_name = line.split(' ')[0]
                    if test_name == name:
                        file.write(test_name + ' ' + 'closed' + ' ' + line.split(' ')[2] + ' ' + line.split(' ')[3])
                    else:
                        file.write(line)
            file.close()
            print('Now ' + name + ' is closed.')
        else:
            print('status has already closed')


def tests_form():
    file_info, working_directory = login.login_page()
    show_your_test(file_info)

    option = input('If you want to create test - 1, '
                   'change test - 2, \n'
                   'change test status - 3, '
                   'request test visualization - 4,\n'
                   'import test result to csv - 5,'
                   'quit - 6: ')

    while True:
        if option == '1':
            create_test(file_info, working_directory)
        elif option == '2':
            change_test(file_info, working_directory)
        elif option == '3':
            change_test_status(file_info)
        elif option == '4':
            figure = input('Type 1 to visualize with gystogram , 2 - with circle:')
            if figure == '1':
                visual.draw_gistogram(file_info, working_directory)
            elif figure == '2':
                visual.draw_circle(file_info, working_directory)
        elif option == '5':
            create_table.create_table(file_info, working_directory)
        elif option == '6':
            break
        show_your_test(file_info)
        option = input('If you want to create test - 1, '
                       'change test - 2, \n'
                       'change test status - 3, '
                       'request test visualization - 4,'
                       'import test to csv - 5,\n'
                       'quit - 6: ')