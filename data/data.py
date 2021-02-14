from g_objects.user import User
from .database import Database


class Data:

    def __init__(self):
        self.db = Database()

    def save_quiz(self, quiz):
        self.db.save_quiz(quiz)

    def save_user(self, user):
        self.db.save_user(user)

    def get_all_quizes(self):
        return self.db.load_quiz_data()

    def get_quizes_by_user_id(self, user_id):
        quiz_data = self.db.load_quiz_data()
        quizes = []
        for quiz in quiz_data:
            if quiz.is_public:
                quizes.append(quiz)
            elif quiz.user_id == user_id:
                quizes.append(quiz)
        return quizes

    def get_public_quizes(self):
        quiz_data = self.db.load_quiz_data()
        public_quizes = []
        for quiz in quiz_data:
            if quiz.is_public:
                public_quizes.append(quiz)
        return public_quizes

    def get_quiz_by_title(self, title):
        quiz_repository = self.db.load_quiz_data()
        result = []
        for quiz in quiz_repository:
            if quiz.title == title:
                result.append(quiz)
        return result

    def get_quiz_by_id(self, id):
        quiz_repository = self.db.load_quiz_data()
        for quiz in quiz_repository:
            if quiz.id == id:
                return quiz
        return False

    def get_user_by_username(self, username):
        users = self.db.load_user_data()
        for user in users:
            if user.username == username:
                return user
        return False

    def create_user(self, username, password):
        if not self.get_user_by_username(username):
            user = User(username, password)
            self.db.save_user(user)
            print('user with username: "' + username + '" created!')
        else:
            print('user with username: "' + username + '" already exists!')
