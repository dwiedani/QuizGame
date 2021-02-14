import json
import os.path
from g_objects.quiz import Quiz
from g_objects.user import User
import question_factory as question_factory

DATA_JSON = './data/data.json'
USER_JSON = './data/users.json'


class Database:

    def load_quiz_data(self):
        """
        Loads User JSON file and reads Data
        :return: Quiz[]
        """
        quiz_repository = []
        if os.path.isfile(DATA_JSON):
            file = open(DATA_JSON)
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
        """
        Saves a User to JSON or updates the Entry if allready exists
        :param new_quiz: Quiz
        """

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
        file = open(DATA_JSON, 'w')
        with file as outfile:
            json.dump(data, outfile)
        file.close()

    def load_user_data(self):
        """
        Loads User JSON file and reads Data
        :return: User[]
        """

        user_repository = []
        if os.path.isfile(USER_JSON):
            file = open(USER_JSON)
            with file as json_file:
                json_str = json.load(json_file)
                data = json.loads(json_str)
                for user in data:
                    user_object = User(**user)
                    user_repository.append(user_object)
            file.close()
        return user_repository

    def save_user(self, new_user):
        """
        Saves a User to JSON or updates the Entry if allready exists
        :param new_user: User
        """

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
        file = open(USER_JSON, 'w')
        with file as outfile:
            json.dump(data, outfile)
        file.close()
