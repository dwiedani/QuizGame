import uuid
class Question:

    def __init__(self, question_type, text, correct_answer, id=None):
        if id == None:
            self.id = str(uuid.uuid4())
        else:
            self.id = id
        self.text = text
        self.question_type = question_type
        self.correct_answer = correct_answer

    def ask(self):
        print(self.text)
        answer_input = input()
        return self.validate(answer_input)

    def validate(self, answer):
        if answer == self.correct_answer:
            return True
        return False

    class Builder:
        text = ''
        correct_answer = None

        def question_type(self, question_type):
            self.question_type = question_type
            return self

        def text(self, text):
            self.text = text
            return self

        def correct_answer(self, correct_answer):
            self.correct_answer = correct_answer
            return self

        def build(self):
            return Question(self.question_type, self.text, self.correct_answer)
