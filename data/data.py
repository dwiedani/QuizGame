import json
import os.path
from g_objects.quiz import Quiz
import question_factory as question_factory


class Data:
    quiz_list = []

    def __init__(self):
        self.load_quiz_data()

    def set_quiz(self, new_quiz):
        for quiz in self.quiz_list:
            if new_quiz.title == quiz.title:
                return quiz
        self.quiz_list.append(new_quiz)
        self.save_quiz_data()

        return new_quiz

    def get_quiz(self, title):
        for quiz in self.quiz_list:
            if quiz.title == title:
                return quiz
        return False

    def print_quiz_list(self):
        for quiz in self.quiz_list:
            print('(' + quiz.title + ') questions:' + str(len(quiz.questions)))

    def load_quiz_data(self):
        self.quiz_list = []
        if os.path.isfile('./data/data.txt'):
            with open('./data/data.txt') as json_file:
                json_str = json.load(json_file)
                data = json.loads(json_str)
                for quiz in data:
                    quiz_object = Quiz(quiz['title'])
                    questions = json.loads(quiz['questions'])
                    for question in questions:
                        question_object = question_factory.create_from_json(question)
                        quiz_object.questions.append(question_object)
                    self.quiz_list.append(quiz_object)

    def save_quiz_data(self):
        quiz_data = []
        for quiz_item in self.quiz_list:
            quiz = {'title': quiz_item.title}
            question_data = []
            for question_item in quiz_item.questions:
                question_data.append(json.dumps(question_item.__dict__))
            quiz['questions'] = json.dumps(question_data)
            quiz_data.append(quiz)
        data = json.dumps(quiz_data)
        with open('./data/data.txt', 'w') as outfile:
            json.dump(data, outfile)
