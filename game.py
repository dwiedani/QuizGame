from g_objects.quiz import Quiz
from data.data import Data
from g_objects.question import Question
from copy import deepcopy


class Game:
    selected_quiz = None
    data = Data()

    def play_quiz(self):
        self.data.load_quiz_data()
        if self.selected_quiz:
            current_quiz = deepcopy(self.selected_quiz)
            current_quiz.title += 'copy'
            print('*** Now playing:' + current_quiz.title + ' ***')
            while current_quiz.has_question():
                if current_quiz.do_question():
                    print('correct!')
                else:
                    print('incorrect!')
            print('(!) Quiz "' + current_quiz.title + '" finished')
        else:
            print('(!) No Quiz selected')

    def create_quiz(self):
        print('Type Quiz title:')
        title = input()
        quiz = Quiz(title)
        self.data.set_quiz(quiz)
        self.selected_quiz = quiz
        print('(!) The Quiz: "' + self.selected_quiz.title + '" has been created and selected')

    def select_quiz(self):
        self.data.load_quiz_data()
        print('Select a Quiz:')
        self.data.print_quiz_list()
        title = input()
        self.selected_quiz = self.data.get_quiz(title)
        if self.selected_quiz:
            print('(!) Quiz "' + self.selected_quiz.title + '" loaded')
        else:
            print('(!) Quiz "' + title + '" not found')

    def create_question(self):
        if self.selected_quiz:
            question = Question()
            self.selected_quiz.add_question(question.build())
            self.data.save_quiz_data()
        else:
            print('(!) No Quiz selected')
