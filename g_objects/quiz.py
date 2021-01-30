import random

class Quiz:
    questions = []

    def __init__(self, title):
        self.title = title
        self.questions = []

    def run(self):
        while self.has_question():
            if (self.do_question()):
                print('correct!')
            else:
                print('incorrect!')


    def add_question(self, question):
        self.questions.append(question)

    def do_question(self):
        if self.has_question():
            random.shuffle(self.questions)
            question = self.questions.pop()
            print(question.text)
            return question.ask()

    def has_question(self):
        if (len(self.questions) != 0):
            return True
        return False