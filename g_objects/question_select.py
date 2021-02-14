import random
from .question import Question


class QuestionSelect(Question):

    def __init__(self, question_type, text, correct_answer, incorrect_answers):
        super().__init__(question_type, text, correct_answer)
        self. incorrect_answers = incorrect_answers

    def ask(self):
        answers = self.incorrect_answers
        answers.append(self.correct_answer)
        random.shuffle(answers)
        index = 0

        print(self.text)
        for answer in answers:
            print('(' + str(index) + '). ' + answer)
            index += 1

        answer_input = 100
        while answer_input >= len(answers):
            answer_input = int(input())
        return self.validate(answers[answer_input])

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

        def incorrect_answers(self, incorrect_answers):
            self.incorrect_answers = incorrect_answers
            return self

        def build(self):
            return QuestionSelect(self.question_type, self.text, self.correct_answer, self.incorrect_answers)
