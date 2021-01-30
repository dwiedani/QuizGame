import random

class Question:
    text = ''
    correct_answer = ''
    incorrect_answers = []

    def build(self):
        print('Type question:')
        question = input()
        print('Type correct answer:')
        correct_answer = input()
        print('How many incorrect answers would you like to add?')
        amount = 100
        while(amount > 3 or amount < 1):
            amount = int(input())
        incorrect_answers = []
        for i in range(amount):
            print('type a incorrect answer:')
            incorrect_answer = str(input())
            incorrect_answers.append(incorrect_answer)
        self.text = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
        return self

    def set(self, text, correct_answer, incorrect_answers):
        self.text = text
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers

    def ask(self):
        answers = self.incorrect_answers
        answers.append(self.correct_answer)
        random.shuffle(answers)
        index = 0

        for answer in answers:
            print('(' + str(index) + '). ' + answer)
            index += 1

        answer_input = 100
        while(answer_input >= len(answers)):
            answer_input = int(input())
        return self.validate(answers[answer_input])

    def validate(self, answer):
        if (answer == self.correct_answer):
            return True
        return False