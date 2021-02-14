import json
import os.path
from g_objects.quiz import Quiz
from g_objects.user import User
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
        result = []
        for quiz in quiz_repository:
            if quiz.title == title:
                result.append(quiz)
        return result

    def get_quiz_by_id(self, id):
        quiz_repository = self.load_quiz_data()
        for quiz in quiz_repository:
            if quiz.id == id:
                return quiz
        return False

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

    def load_user_data(self):
        user_repository = []
        if os.path.isfile('./data/users.json'):
            file = open('./data/users.json')
            with file as json_file:
                json_str = json.load(json_file)
                data = json.loads(json_str)
                for user in data:
                    user_object = User(**user)
                    user_repository.append(user_object)
            file.close()
        return user_repository

    def save_user(self, new_user):
        user_data = []
        user_repository = self.load_user_data()
        updated = False

        for i in range(len(user_repository)):
            if user_repository[i].id == new_user.id:
                user_repository[i] = new_user
                updated = True

        if updated == False:
            user_repository.append(new_user)

        for user_item in user_repository:
            user = user_item.__dict__
            user_data.append(user)
        data = json.dumps(user_data)
        file = open('./data/users.json', 'w')
        with file as outfile:
            json.dump(data, outfile)
        file.close()

    def get_user_by_username(self, username):
        users = self.load_user_data()
        for user in users:
            if user.username == username:
                return user
        return False

    def create_user(self, username, password):
        if not self.get_user_by_username(username):
            user = User(username, password)
            self.save_user(user)
            print('user with username: "' + username + '" created!')
        else:
            print('user with username: "' + username + '" already exists!')