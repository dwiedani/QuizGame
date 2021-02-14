from g_objects.quiz import Quiz
from data.data import Data
import question_factory as question_factory
from copy import deepcopy
import re


class Game:
    selected_quiz = None
    data = Data()
    current_user = None

    def play_quiz(self):
        if self.selected_quiz:
            current_quiz = self.data.get_quiz_by_id(self.selected_quiz)
            print('*** Now playing:' + current_quiz.title + ' ***')
            while current_quiz.has_question():
                if current_quiz.do_question():
                    print('correct!')
                    self.current_user.correct_answer()
                    self.current_user.question()
                    self.data.save_user(self.current_user)
                else:
                    print('incorrect!')
                    self.current_user.question()
                    self.data.save_user(self.current_user)
            self.current_user.quiz_played()
            self.data.save_user(self.current_user)
            print('(!) Quiz "' + current_quiz.title + '" finished')
        else:
            print('(!) No Quiz selected')

    def create_quiz(self):
        print('Type Quiz title:')
        title = input()
        quiz = Quiz(title)
        self.data.create_quiz(quiz)
        self.selected_quiz = quiz.id
        print('(!) The Quiz: "' + self.data.get_quiz_by_id(self.selected_quiz).title + '" has been created and selected')

    def select_quiz(self):
        print('Select a Quiz:')
        self.data.print_quiz_list()
        title = input()
        quiz = self.data.get_quiz_by_title(title)
        if quiz:
            self.selected_quiz = quiz.id
            if self.selected_quiz:
                print('(!) Quiz "' + quiz.title + '" loaded')
        else:
            print('(!) Quiz "' + title + '" not found')

    def create_question(self):
        if self.selected_quiz:
            print('What type of Question?')
            print('(1). Exact String')
            print('(2). Exact Number')
            print('(3). Selection')
            question_type = input()

            question = None

            if question_type == '1':
                text = input('Enter question text: ')
                correct_answer = input('Enter correct answer: ')
                question = question_factory.create_exact_question(text, correct_answer)

            if question_type == '2':
                text = input('Enter question text: ')
                answer_input = input('Enter correct answer: ')
                while not re.match(r'^[ 0-9]+$', answer_input):
                    answer_input = input('Enter correct answer: ')
                correct_answer = int(answer_input)
                question = question_factory.create_numeric_question(text, correct_answer)

            if question_type == '3':
                text = input('Enter question text: ')
                correct_answer = input('Enter correct answer: ')

                amount = 0
                while amount > 3 or amount < 1:
                    answer_input = input('How many incorrect answers would you like to add?')
                    while not re.match(r'^[ 0-9]+$', answer_input):
                        answer_input = input('How many incorrect answers would you like to add?')
                    amount = int(answer_input)

                incorrect_answers = []

                for i in range(amount):
                    print('type a incorrect answer:')
                    incorrect_answer = str(input())
                    incorrect_answers.append(incorrect_answer)

                question = question_factory.create_selection_question(text, correct_answer, incorrect_answers)

            quiz = self.data.get_quiz_by_id(self.selected_quiz)
            quiz.add_question(question)
            self.data.save_quiz(quiz)
        else:
            print('(!) No Quiz selected')

    def login(self):
        username = input('username:')
        password = input('password:')
        user = self.data.get_user_by_username(username)
        if user:
            if password == user.password:
                self.current_user = user
        else:
            print('(!) username and/or password are incorrect')


    def register(self):
        print('*** User-registration ***')
        username = input('username:')
        while not re.match(r'^[a-zA-Z]+$', username):
            print('(!) only Letters are allowed')
            username = input('username:')
        password = input('password:')
        re_password = input('confirm password:')
        if password == re_password:
            self.data.create_user(username,password)
        else:
            print('(!) your passwords are not equal')
