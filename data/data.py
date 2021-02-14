import json
import os.path
from g_objects.quiz import Quiz
import question_factory as question_factory


class Data:

    def __init__(self):
        self.load_quiz_data()

    def create_quiz(self, new_quiz):
        if not self.get_quiz_by_id(new_quiz.id):
            self.save_quiz(new_quiz)
            return new_quiz
        return self.get_quiz_by_id(new_quiz.id)

    def get_quiz_by_title(self, title):
        quiz_repository = self.load_quiz_data()
        for quiz in quiz_repository:
            if quiz.title == title:
                return quiz
        return False

    def get_quiz_by_id(self, id):
        quiz_repository = self.load_quiz_data()
        for quiz in quiz_repository:
            if quiz.id == id:
                return quiz
        return False

    def print_quiz_list(self):
        quiz_repository = self.load_quiz_data()
        for quiz in quiz_repository:
            print('(' + quiz.title + ') questions:' + str(len(quiz.questions)))

    def load_quiz_data(self):
        quiz_repository = []
        if os.path.isfile('./data/data.json'):
            file = open('./data/data.json')
            with file as json_file:
                json_str = json.load(json_file)
                data = json.loads(json_str)
                for quiz in data:
                    quiz_object = Quiz(quiz['title'], quiz['id'])
                    questions = json.loads(quiz['questions'])
                    for question in questions:
                        question_object = question_factory.create_from_json(question)
                        quiz_object.questions.append(question_object)
                    quiz_repository.append(quiz_object)
            file.close()
        return quiz_repository


    def save_quiz(self, new_quiz):
        quiz_data = []
        quiz_repository = self.load_quiz_data()
        updated = False

        for i in range(len(quiz_repository)):
            if quiz_repository[i].id == new_quiz.id:
                quiz_repository[i] = new_quiz
                updated = True

        if updated == False:
            quiz_repository.append(new_quiz)

        for quiz_item in quiz_repository:
            quiz = quiz_item.__dict__
            question_data = []
            for question_item in quiz_item.questions:
                question_data.append(json.dumps(question_item.__dict__))
            quiz['questions'] = json.dumps(question_data)
            quiz_data.append(quiz)
        data = json.dumps(quiz_data)
        file = open('./data/data.json', 'w')
        with file as outfile:
            json.dump(data, outfile)
        file.close()
