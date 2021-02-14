import uuid


class User:

    def __init__(self, username, password, id=str(uuid.uuid4()), played=0, questions=0, correct_answers=0):
        self.id = id
        self.username = username
        self.password = password
        self.played = played
        self.questions = questions
        self.correct_answers = correct_answers

    def correct_answer(self):
        self.correct_answers += 1

    def quiz_played(self):
        self.played += 1

    def question(self):
        self.questions += 1

    def stats(self):
        stats = {}
        stats['played'] = self.played
        stats['questions'] = self.questions
        stats['correct_answers'] = self.correct_answers
        return stats
