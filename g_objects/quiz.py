import random
import uuid


class Quiz:
    questions = []

    def __init__(self, title, user_id, is_public=False, id=str(uuid.uuid4())):
        self.id = id
        self.title = title
        self.user_id = user_id
        self.questions = []
        self.is_public = is_public

    def add_question(self, question):
        self.questions.append(question)

    def do_question(self):
        if self.has_question():
            random.shuffle(self.questions)
            question = self.questions.pop()
            return question.ask()

    def set_public(self, is_public):
        self.is_public = is_public

    def has_question(self):
        if len(self.questions) != 0:
            return True
        return False
