from g_objects.quiz import Quiz
from data.data import Data
import question_factory as question_factory
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
                    if self.current_user:
                        self.current_user.correct_answer()
                        self.current_user.question()
                        self.data.save_user(self.current_user)
                else:
                    print('incorrect!')
                    if self.current_user:
                        self.current_user.question()
                        self.data.save_user(self.current_user)
            if self.current_user:
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
        print('(!) The Quiz: "' + self.data.get_quiz_by_id(
            self.selected_quiz).title + '" has been created and selected')

        #Question creation loop
        question_count = self.number_input_filter('how many question would you like to add? (3-10):')

        if question_count > 10:
            question_count = 10
        elif question_count < 3:
            question_count = 3

        print('starting creation of ' + str(question_count) + ' questions')

        for i in range(question_count):
            self.create_question()

    def select_quiz(self):
        print('Select a Quiz:')
        self.print_quiz_list()
        title = input()
        quizes = self.data.get_quiz_by_title(title)

        if len(quizes) == 0:
            print('(!) Quiz "' + title + '" not found')
            return

        if len(quizes) == 1:
            index = 0

        elif len(quizes) > 1:
            print('(!) Multiple quizes with title:"' + quizes[0].title + '" found')
            self.print_quiz_list_indexed(quizes)
            index = self.number_input_filter('select a quiz: ')

        self.selected_quiz = quizes[index].id
        if self.selected_quiz:
            print('(!) Quiz "' + quizes[index].title + '" loaded')
        return

    def print_quiz_list(self, quiz_data=None):
        if not quiz_data:
            quiz_data = self.data.load_quiz_data()
        for quiz in quiz_data:
            print('(' + quiz.title + ') questions:' + str(len(quiz.questions)))

    def print_quiz_list_indexed(self, quiz_data=None):
        if not quiz_data:
            quiz_data = self.data.load_quiz_data()
        index = 0
        for quiz in quiz_data:
            print('(' + str(index) + ')' + quiz.title + ' questions: ' + str(len(quiz.questions)))
            index += 1

    def create_question(self):
        if self.selected_quiz:
            quiz = self.data.get_quiz_by_id(self.selected_quiz)

            if len(quiz.questions) >= 10:
                return

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
                correct_answer = self.number_input_filter('Enter correct answer: ')
                question = question_factory.create_numeric_question(text, correct_answer)

            if question_type == '3':
                text = input('Enter question text: ')
                correct_answer = input('Enter correct answer: ')

                amount = 0
                while amount > 3 or amount < 1:
                    amount = self.number_input_filter('How many incorrect answers would you like to add?')

                incorrect_answers = []

                for i in range(amount):
                    print('type a incorrect answer:')
                    incorrect_answer = str(input())
                    incorrect_answers.append(incorrect_answer)

                question = question_factory.create_selection_question(text, correct_answer, incorrect_answers)
            quiz.add_question(question)
            self.data.save_quiz(quiz)
        else:
            print('(!) No Quiz selected')
        return

    def number_input_filter(self, message):
        input_str = input(message)
        while not re.match(r'^[ 0-9]+$', input_str):
            print('(!) only numbers allowed')
            input_str = input(message)
        return int(input_str)

    def letter_input_filter(self, message):
        input_str = input(message)
        while not re.match(r'^[a-zA-Z]+$', input_str):
            print('(!) only letters allowed')
            input_str = input(message)
        return input_str

    def show_user_statistics(self):
        if self.current_user:
            stats = self.current_user.stats()
            print('Played Quizes: ' + str(stats['played']))
            print('Answered Questions: ' + str(stats['questions']))
            print('Correct Answers: ' + str(stats['correct_answers']))

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
        username = self.letter_input_filter('username:')
        password = input('password:')
        re_password = input('confirm password:')
        if password == re_password:
            self.data.create_user(username,password)
        else:
            print('(!) your passwords are not equal')
