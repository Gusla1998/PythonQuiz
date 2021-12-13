import visual
import csv
import webbrowser


def create_table(file_info, working_directory):
    test_directory, test_anon = visual.return_test_by_name(file_info, working_directory)
    while test_directory == False:
        print('Wrong test name(or status), try again...')
        test_directory, test_anon = visual.return_test_by_name(file_info, working_directory)
    answers = visual.return_test_answers(test_directory, test_anon)
    questions = visual.return_test_questions(test_directory)
    sum = visual.sum_answers(answers, questions)

    file = 'table.csv'

    with open(file, 'w', newline='') as f:
        writ = csv.writer(f)
        writ.writerow(['Question', '1 answer', 'count', '2 answer', 'count', '3 answer', 'count', '4 answer', 'count'])
        for row in sum:
            groups = []
            groups.append(row)
            for point in sum[row]:
                for key in point:
                    groups.append(key)
                    groups.append(point[key])
            writ.writerow(groups)
    f.close()
    webbrowser.open_new(file)