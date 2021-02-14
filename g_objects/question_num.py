from .question import Question
import re


class QuestionNum(Question):

    def __init__(self, question_type, text, correct_answer):
        super().__init__(question_type, text, correct_answer)

    def ask(self):
        print(self.text)
        answer_input = input()
        while not re.match(r'^[ 0-9]+$', answer_input):
            answer_input = input()
        answer_input = int(answer_input)
        return self.validate(answer_input)

    class Builder:

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
            return QuestionNum(self.question_type, self.text, self.correct_answer)
