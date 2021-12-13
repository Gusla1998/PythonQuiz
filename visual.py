import matplotlib.colors as mcolors
import numpy as np
import matplotlib.pyplot as plt
import os


def return_test_by_name(file_info, working_directory):
    print('************Choose test*************')

    name = input('Name of questionnaire(with closed status):')
    test_name = ''
    test_status = ''

    with open(file_info, 'r') as file:
        for line in file:
            test_name = line.split(' ')[0]
            test_status = line.split(' ')[1]

            if test_name == name and test_status == 'closed':
                test_directory = working_directory + '/' + test_name
                file.close()
                test_anon = 'anon' if int(line.split(' ')[3]) else 'name'
                return test_directory, test_anon
    file.close()
    return False, False


def return_test_answers(test_directory, test_anon):
    answer_list = []
    for filename in os.listdir(test_directory):
        another_person = []
        if filename == 'test.txt':
            continue
        else:
            with open(test_directory + '/' + filename, 'r') as file:
                for line in file:
                    another_person.append(line.split('\n')[0])
            file.close()
            another_person.pop(0)
            if test_anon == 'name':
                another_person.pop(-1)
            answer_list.append(another_person)
    return answer_list


def return_test_questions(test_directory):
    test_file = test_directory + '/test.txt'
    test = []
    with open(test_file, 'r') as file:
        for line in file:
            test.append(line)
    return test


def sum_answers(answer_list, test):
    sum = {}
    index = 0
    for question in test:
        first = 0
        second = 0
        third = 0
        fourth = 0

        for i in range(0, len(answer_list), 1):
            if answer_list[i][index] == '1':
                first += 1
            elif answer_list[i][index] == '2':
                second += 1
            elif answer_list[i][index] == '3':
                third += 1
            else:
                fourth += 1

        answers = [
            {question.split(' : ')[1].split('\n')[0].split(' ')[0] : first},
            {question.split(' : ')[1].split('\n')[0].split(' ')[1] : second},
            {question.split(' : ')[1].split('\n')[0].split(' ')[2] : third},
            {question.split(' : ')[1].split('\n')[0].split(' ')[3] : fourth}
        ]
        sum[question.split(' : ')[0]] = answers
        index += 1

    return sum


def draw_gistogram(file_info, working_directory):
    test_directory, test_anon = return_test_by_name(file_info, working_directory)
    while test_directory == False:
        print('Wrong test name(or status), try again...')
        test_directory, test_anon = return_test_by_name(file_info, working_directory)
    answers = return_test_answers(test_directory, test_anon)
    questions = return_test_questions(test_directory)
    sum = sum_answers(answers, questions)
    for quest in sum:
        bc = mcolors.BASE_COLORS
        np.random.seed(123)
        groups = []
        counts = []
        for point in sum[quest]:
            for key in point:
                groups.append(key)
                counts.append(point[key])
        width = len(counts)*0.1
        colors = [["r", "b", "g"][int(np.random.randint(0, 3, 1))] for _ in counts]
        plt.bar(groups, counts, width=width, alpha=0.6, bottom=2, color=colors, edgecolor="k", linewidth=2)
        plt.ylabel('Count')
        plt.title(quest)
        plt.show()


def draw_circle(file_info, working_directory):
    test_directory, test_anon = return_test_by_name(file_info, working_directory)
    while test_directory == False:
        print('Wrong test name(or status), try again...')
        test_directory, test_anon = return_test_by_name(file_info, working_directory)
    answers = return_test_answers(test_directory, test_anon)
    questions = return_test_questions(test_directory)
    sum = sum_answers(answers, questions)
    for quest in sum:
        groups = []
        counts = []
        for point in sum[quest]:
            for key in point:
                groups.append(key)
                counts.append(point[key])
        fig, ax = plt.subplots()
        ax.pie(counts, labels=groups, autopct='%1.1f%%', shadow=True,
               wedgeprops={'lw': 1, 'ls': '--', 'edgecolor': "k"}, rotatelabels=True)
        ax.axis("equal")
        plt.title(quest)
        plt.show()