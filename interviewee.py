import os
from fpdf import FPDF
import webbrowser


def psycho_list(file_login, dirname):
    print('*****List of our psychologists*****')
    with open(file_login, 'r') as file:
        for line in file:
            ch_login = line.split(':')[0]
            print(ch_login)

    psych_name = input('Choose psychologist, whose test you want to do:')
    with open(file_login, 'r') as file:
        for line in file:
            ch_login = line.split(':')[0]
            if ch_login == psych_name:
                working_directory = dirname + "/" + psych_name
                return working_directory


def test_list(psych_directory):
    file_test = psych_directory + '/info.txt'
    print('*****List of psychologist`s tests*****')
    with open(file_test, 'r') as file:
        for line in file:
            if line.split(' ')[1] == 'active':
                print(line.split(' ')[0])

    test_name = input('Choose test, which you want to do(or press enter to skip):')
    with open(file_test, 'r') as file:
        for line in file:
            if line.split(' ')[0] == test_name:
                test_directory = psych_directory + "/" + test_name
                test_anon = 'anon' if int(line.split(' ')[3]) else 'name'
                return test_directory, test_name, test_anon
    return False, False, False


def do_test(test_directory, name):
    test_file = test_directory + '/test.txt'

    answer_file = test_directory + '/' + name + '.txt'
    open(answer_file, 'w').write(name + '\n')
    print('*****Give the answer to question, typing number of answer******')
    with open(answer_file, 'a') as ans_file:
        with open(test_file, 'r') as file:
            for line in file:
                print(line.split(' : ')[0])
                print('1)' + line.split(' : ')[1].split(' ')[0])
                print('2)' + line.split(' : ')[1].split(' ')[1])
                print('3)' + line.split(' : ')[1].split(' ')[2])
                print('4)' + line.split(' : ')[1].split(' ')[3])

                answer = input('answer: ')
                ans_file.write(answer + '\n')
        file.close()
    ans_file.close()
    print('*****Thanks for answering, goodbye!******')
    return answer_file


def next_number_for_anon(test_directory):
    i = 0
    for filename in os.listdir(test_directory):
        if filename == 'test.txt':
            continue
        else:
            if int(filename.split('.txt')[0]) > i:
                i = int(filename.split('.txt')[0])
    i = i + 1
    return i


def print_result_pdf(test_file, answer_file, test_anon):
    pdf = FPDF()
    pdf.add_page()


    pdf.set_font("Arial", size=12)

    ans_arr = []
    with open(answer_file, 'r') as a_file:
        for line in a_file:
            ans_arr.append(line)
    a_file.close()

    name = 'anon'
    agreement = 'n'
    if test_anon == 'name':
        agreement = ans_arr[-1]
        if agreement == 'y':
            name = ans_arr[0]
        ans_arr.pop(-1)
    ans_arr.pop(0)
    i = 0

    pdf.set_font("Arial", size=20)
    pdf.cell(200, 10, txt="Your test result: " + name, ln=1, align="C")
    with open(test_file, 'r') as t_file:
        for line in t_file:
            text = line.split(' : ')[0] + ' Your answer: ' + line.split(' : ')[1].split('\n')[0].split(' ')[int(ans_arr[i])-1]
            pdf.cell(50, 10, txt=text, ln=1, align="L")
            i += 1
    text = ' Your agreement to publish result: ' + agreement
    pdf.cell(50, 10, txt=text, ln=1, align="L")
    a_file.close()
    pdf.output("last.pdf")
    webbrowser.open_new(r'last.pdf')


def open_test(file_login, dirname):
    psych_directory = psycho_list(file_login, dirname)
    test_directory, test_name, test_anon = test_list(psych_directory)
    while test_directory == False:
        psych_directory = psycho_list(file_login, dirname)
        test_directory, test_name, test_anon = test_list(psych_directory)

    if test_anon == 'name':
        name = input('Input your name: ')
        answer_file = do_test(test_directory, name)
        agreement = input('Is you agree with processing of personal data - y, disagree - n:')
        open(answer_file, 'a').write(agreement)
    else:
        file_num = next_number_for_anon(test_directory)
        answer_file = do_test(test_directory, str(file_num))

    is_pdf = input('Do you want to print files(y/n):')

    test_file = test_directory + '/' + 'test.txt'
    if is_pdf == 'y':
        print_result_pdf(test_file, answer_file, test_anon)
