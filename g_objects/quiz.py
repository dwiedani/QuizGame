import random
import uuid

class Quiz:
    questions = []

    def __init__(self, title, id=None):
        if id == None:
            self.id = str(uuid.uuid4())
        else:
            self.id = id
        self.title = title
        self.questions = []

    def run(self):
        while self.has_question():
            if self.do_question():
                print('correct!')
            else:
                print('incorrect!')

    def add_question(self, question):
        self.questions.append(question)

    def do_question(self):
        if self.has_question():
            random.shuffle(self.questions)
            question = self.questions.pop()
            return question.ask()

    def has_question(self):
        if len(self.questions) != 0:
            return True
        return False
