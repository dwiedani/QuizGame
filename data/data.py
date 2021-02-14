import json
import os.path
from g_objects.quiz import Quiz
import question_factory as question_factory


class Data:
    quiz_repository = []
    question_repository = []

    def __init__(self):
        self.load_quiz_data()

    def set_quiz(self, new_quiz):
        for quiz in self.quiz_repository:
            if new_quiz.title == quiz.title:
                return quiz
        self.quiz_repository.append(new_quiz)
        self.save_quiz_data()

        return new_quiz

    def get_quiz(self, title):
        for quiz in self.quiz_repository:
            if quiz.title == title:
                return quiz
        return False

    def print_quiz_list(self):
        for quiz in self.quiz_repository:
            print('(' + quiz.title + ') questions:' + str(len(quiz.questions)))

    def load_quiz_data(self):
        self.quiz_repository = []
        if os.path.isfile('./data/data.json'):
            with open('./data/data.json') as json_file:
                json_str = json.load(json_file)
                data = json.loads(json_str)
                for quiz in data:
                    quiz_object = Quiz(quiz['title'], quiz['id'])
                    questions = json.loads(quiz['questions'])
                    for question in questions:
                        question_object = question_factory.create_from_json(question)
                        quiz_object.questions.append(question_object)
                    self.quiz_repository.append(quiz_object)

    def save_quiz_data(self):
        quiz_data = []
        for quiz_item in self.quiz_repository:
            quiz = quiz_item.__dict__
            question_data = []
            for question_item in quiz_item.questions:
                question_data.append(json.dumps(question_item.__dict__))
            quiz['questions'] = json.dumps(question_data)
            quiz_data.append(quiz)
        data = json.dumps(quiz_data)
        with open('./data/data.json', 'w') as outfile:
            json.dump(data, outfile)
