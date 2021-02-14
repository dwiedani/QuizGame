import random
import uuid

class Quiz:
    questions = []

    def __init__(self, title, id=str(uuid.uuid4())):
        self.id = id
        self.title = title
        self.questions = []

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
