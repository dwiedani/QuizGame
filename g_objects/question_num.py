from .question import Question
import re


class QuestionNum(Question):

    def __init__(self, text, correct_answer):
        super().__init__(text, correct_answer)
        self.correct_answer = correct_answer

    def ask(self):
        print(self.text)
        answer_input = input()
        while not re.match(r'^[ 0-9]+$', answer_input):
            answer_input = input()
        answer_input = int(answer_input)
        return self.validate(answer_input)

    class Builder:
        text = ''
        correct_answer = None

        def text(self, text):
            self.text = text
            return self

        def correct_answer(self, correct_answer):
            self.correct_answer = correct_answer
            return self

        def build(self):
            return QuestionNum(self.text, self.correct_answer)
