There are two main modules:
1) tests.py - logic of psycholog interface
2) interviewee.py - logic of interviewee interface, using module webbrowser to open pdf for print

tests.py - includes helping modules:
1)login.py - module for creating and sign in psycho-workers, includes methods for sign in, sign up( creates directory for each user, information about users are in data directory in login.txt file)
2)visual.py - module that takes data from tests and visualize them with two type of diagramm(gistogram, circle-diagram), using module os, matplotlib, numpy
3)create_table.py - module that takes data from tests and output csv-table with this data, using module csv, webbrowser

At start program asks user if user work with programm in interviewee or psycho mode.

Interviewee mode allow user only to choose psycholog and test for passing through.
Then your are able to print your results with .pdf file or quit.
If test assume inputting personal data, user asked for privacy policies, and if user 
disagree with this statements his name turns to anon.

Psycholog mode allow user to create test(tests creates in user's directory in data, test results in test directory), change questions in test, change test status(work-in-progress(user can change answers) --> active (interviewee allowed to pass through the test, user not allowed to change questions) --> closed(user allow to import result to csv or draw it)), draw result of test with circle diagram or gistogramm(in following way: name of question, how many answers for each variant of answer), and put results inot csv table the same way.