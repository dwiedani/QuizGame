from g_objects.quiz import Quiz
from g_objects.user import User
from data.data import Data
import question_factory as question_factory
import re


def number_input_filter(message):
    input_str = input(message)
    while not re.match(r'^[ 0-9]+$', input_str):
        print('(!) only numbers allowed')
        input_str = input(message)
    return int(input_str)


def letter_input_filter(message):
    input_str = input(message)
    while not re.match(r'^[a-zA-Z]+$', input_str):
        print('(!) only letters allowed')
        input_str = input(message)
    return input_str


class Game:
    selected_quiz = None
    data = Data()
    current_user = None
    session_user = User('unregistered', '')

    def play_quiz(self):
        if self.selected_quiz:
            current_quiz = self.data.get_quiz_by_id(self.selected_quiz)
            print('*** Now playing:' + current_quiz.title + ' ***')
            while current_quiz.has_question():
                if current_quiz.do_question():
                    print('correct!')
                    if self.current_user:
                        self.current_user.correct_answer()
                        self.data.save_user(self.current_user)
                    else:
                        self.session_user.correct_answer()
                else:
                    print('incorrect!')
                if self.current_user:
                    self.current_user.question()
                    self.data.save_user(self.current_user)
                else:
                    self.session_user.question()
            if self.current_user:
                self.current_user.quiz_played()
                self.data.save_user(self.current_user)
            else:
                self.session_user.quiz_played()
            print('(!) Quiz "' + current_quiz.title + '" finished')
        else:
            print('(!) No Quiz selected')

    def create_quiz(self):
        title = input('Type Quiz title:')
        print('select quiz type')
        print('(1) public')
        print('(2) private')
        public_selection = number_input_filter('select option: ')

        if public_selection == 1:
            is_public = True
        else:
            is_public = False

        quiz = Quiz(title, self.current_user.id, is_public)

        self.data.save_quiz(quiz)
        self.selected_quiz = quiz.id
        print('(!) The Quiz: "' + self.data.get_quiz_by_id(
            self.selected_quiz).title + '" has been created and selected')

        question_count = number_input_filter('how many question would you like to add? (3-10):')

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
        quizzes = self.data.get_quiz_by_title(title)
        index = 0

        if len(quizzes) == 0:
            print('(!) Quiz "' + title + '" not found')
            return

        elif len(quizzes) > 1:
            print('(!) Multiple quizzes with title:"' + quizzes[0].title + '" found')
            self.print_quiz_list_indexed(quizzes)
            index = number_input_filter('select a quiz: ')

        if 0 <= index < len(quizzes):
            self.selected_quiz = quizzes[index].id
            if self.selected_quiz:
                print('(!) Quiz "' + quizzes[index].title + '" loaded')
        return

    def print_quiz_list(self, quiz_data=None):
        if not quiz_data:
            if self.current_user:
                quiz_data = self.data.get_quizes_by_user_id(self.current_user.id)
            else:
                quiz_data = self.data.get_public_quizes()

        for quiz in quiz_data:
            print('(' + quiz.title + ') questions:' + str(len(quiz.questions)))

    def print_quiz_list_indexed(self, quiz_data=None):
        if not quiz_data:
            if self.current_user:
                quiz_data = self.data.get_all_quizes()
            else:
                quiz_data = self.data.get_public_quizes()
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
                correct_answer = number_input_filter('Enter correct answer: ')
                question = question_factory.create_numeric_question(text, correct_answer)

            if question_type == '3':
                text = input('Enter question text: ')
                correct_answer = input('Enter correct answer: ')

                amount = 0
                while amount > 3 or amount < 1:
                    amount = number_input_filter('How many incorrect answers would you like to add?')

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

    def show_user_statistics(self):
        if self.current_user:
            stats = self.current_user.stats()
        else:
            stats = self.session_user.stats()
        print('Played quizzes: ' + str(stats['played']))
        print('Answered Questions: ' + str(stats['questions']))
        print('Correct Answers: ' + str(stats['correct_answers']))
        print('Quota: ' + str( round(stats['correct_answers']/stats['questions'] * 100,2)) + '%')


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
        username = letter_input_filter('username:')
        password = input('password:')
        re_password = input('confirm password:')
        if password == re_password:
            self.data.create_user(username, password)
        else:
            print('(!) your passwords are not equal')
