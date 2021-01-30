from quiz import Quiz
from data import Data
from question import Question

class Game:

    current_quiz = None
    data = Data()

    def play_quiz(self):
        self.data.load_quiz_data()
        if (self.current_quiz):
            print('*** Now playing:' + self.current_quiz.title + ' ***')
            while (self.current_quiz.has_question()):
                if (self.current_quiz.do_question()):
                    print('correct!')
                else:
                    print('incorrect!')
            print('(!) Quiz "' + self.current_quiz.title + '" finished')
        else:
            print('(!) No Quiz selected')

    def create_quiz(self):
        print('Type Quiz title:')
        title = input()
        quiz = Quiz(title)
        self.data.save_quiz(quiz)
        self.current_quiz = quiz
        print('(!) The Quiz: "' + self.current_quiz.title + '" has been created and selected')

    def select_quiz(self):
        self.data.load_quiz_data()
        print('Select a Quiz:')
        self.data.print_quiz_list()
        title = input()
        self.current_quiz = self.data.get_quiz(title)
        if (self.current_quiz):
            print('(!)' + self.current_quiz.title + ' Quiz loaded')
        else:
            print('(!) Quiz "' + title + '" not found')

    def create_question(self):
        if (self.current_quiz):
            self.current_quiz.add_question(Question().build())
            self.data.save_quiz_data()
        else:
            print('(!) No Quiz selected')