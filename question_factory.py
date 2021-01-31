from g_objects.question import Question
from g_objects.question_num import QuestionNum
from g_objects.question_select import QuestionSelect
import json


def create_selection_question(text, correct_answer, incorrect_answers):
    builder = QuestionSelect.Builder()
    return builder.text(text).correct_answer(correct_answer).incorrect_answers(incorrect_answers).build()


def create_exact_question(text, correct_answer):
    builder = Question.Builder()
    return builder.text(text).correct_answer(correct_answer).build()


def create_numeric_question(text, correct_answer):
    builder = QuestionNum.Builder()
    return builder.text(text).correct_answer(correct_answer).build()

def create_from_json(question_data):
    question_data = json.loads(question_data)
    if 'incorrect_answers' in question_data:
        return create_selection_question(
            question_data['text'],
            question_data['correct_answer'],
            question_data['incorrect_answers'])
    elif isinstance(question_data['correct_answer'], int):
        return create_numeric_question(question_data['text'], question_data['correct_answer'])
    else:
        return create_exact_question(question_data['text'], question_data['correct_answer'])
